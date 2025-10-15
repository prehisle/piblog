import os
import sys
import re
import datetime
import subprocess
from urllib.parse import quote

import requests


ALLOWED_CATEGORIES = {"duoba", "duoma", "duoduo"}
CONTENT_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content", "posts")


def get_session_inner(proxy: str = "") -> requests.Session:
    """
    Create a requests session with optional HTTP/HTTPS proxy.
    Set verify False to be tolerant to local mitm proxies.
    """
    session = requests.session()
    if proxy:
        session.proxies = {
            "http": proxy,
            "https": proxy,
        }
    session.verify = False
    return session


def get_session() -> requests.Session:
    # Assume a local proxy may exist; if not, direct session still works
    proxy = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy") or "http://127.0.0.1:10808"
    return get_session_inner(proxy)


def google_translate(sl: str, tl: str, q: str) -> str:
    """
    Very lightweight call to Google's translate endpoint used by web UI.
    This is best-effort and may fail; caller should handle exceptions.
    """
    session = get_session()
    url = "https://clients5.google.com/translate_a/t"

    # 准备URL参数，'client'参数是必需的
    params = {
        "client": "dict-chrome-ex",
        "sl": sl,
        "tl": tl,
        "q": q
    }
    # 设置一个常见的User-Agent来模拟浏览器行为
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    r = requests.get(url, params=params, headers=headers)
    print(r.text)
    r.raise_for_status()  # 如果请求失败（如4xx或5xx错误）则抛出异常
    data = r.json()
    # Expect [[ [ translated_text, source, ... ] , ... ], ...]
    return data[0]


def translate_zh_to_en(text: str) -> str:
    try:
        return google_translate("zh-CN", "en", text)
    except Exception:
        return ""


def slugify(text: str) -> str:
    text = text.lower()
    # Replace any non alphanumeric with dash
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # Collapse dashes
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def build_unique_slug(category: str, base_slug: str) -> str:
    """
    Ensure the slug is unique under content/posts/<category>/.
    If exists, append -2, -3, ...
    """
    category_dir = os.path.join(CONTENT_ROOT, category)
    os.makedirs(category_dir, exist_ok=True)

    candidate = base_slug or datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    index = 1
    while True:
        filename = f"{candidate}.md" if index == 1 else f"{candidate}-{index}.md"
        full_path = os.path.join(category_dir, filename)
        if not os.path.exists(full_path):
            return os.path.splitext(filename)[0]
        index += 1


def try_hugo_new(category: str, slug: str) -> tuple[bool, str]:
    rel_path = f"posts/{category}/{slug}.md"
    try:
        proc = subprocess.run(["hugo", "new", rel_path], capture_output=True, text=True, check=False)
        # Hugo prints created path to stdout; still compute expected absolute path
        abs_path = os.path.join(CONTENT_ROOT, category, f"{slug}.md")
        return proc.returncode == 0 and os.path.exists(abs_path), abs_path
    except FileNotFoundError:
        # Hugo not installed / not in PATH
        abs_path = os.path.join(CONTENT_ROOT, category, f"{slug}.md")
        return False, abs_path




def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: python scripts/new_post.py <duoba|duoma|duoduo> \"中文标题\"")
        return 2

    category = argv[1].strip().lower()
    if category not in ALLOWED_CATEGORIES:
        print(f"Error: category must be one of {sorted(ALLOWED_CATEGORIES)}")
        return 2

    title = argv[2].strip()

    # Build slug from translation, fallback to time-based
    translated = translate_zh_to_en(title)
    base_slug = slugify(translated) if translated else ""
    slug = build_unique_slug(category, base_slug)

    ok, path = try_hugo_new(category, slug)
    assert ok
    print(path)
    return 0


if __name__ == "__main__":
    #  python .\scripts\new_post.py duoba "2025年第一篇"
    if len(sys.argv) < 2:
        sys.argv.append("duoba")
        sys.argv.append("2025年第一篇")
    sys.exit(main(sys.argv))
