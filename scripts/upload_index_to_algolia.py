import json
import os

# Algolia Python SDK v3 import path

# Optional: load environment variables from .env at project root
try:
    from dotenv import load_dotenv

    # Resolve .env path relative to this script's repo root
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(repo_root, ".env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
except ImportError:
    # python-dotenv not installed; continue with existing environment
    pass

# Read required environment variables
ALGOLIA_APP_ID = os.getenv("ALGOLIA_APP_ID")
ALGOLIA_ADMIN_KEY = os.getenv("ALGOLIA_ADMIN_KEY")
ALGOLIA_INDEX_FILE = os.getenv("ALGOLIA_INDEX_FILE", os.path.join("public", "algolia.json"))
ALGOLIA_INDEX_NAME = os.getenv("ALGOLIA_INDEX_NAME")

if not ALGOLIA_APP_ID or not ALGOLIA_ADMIN_KEY or not ALGOLIA_INDEX_NAME:
    raise RuntimeError(
        "Missing ALGOLIA_APP_ID / ALGOLIA_ADMIN_KEY / ALGOLIA_INDEX_NAME in environment (.env or shell).")

from algoliasearch.search.client import SearchClientSync

objects = json.load(open(ALGOLIA_INDEX_FILE, "rb"))

# Connect and authenticate with your Algolia app using your app ID and write API key
_client = SearchClientSync(ALGOLIA_APP_ID, ALGOLIA_ADMIN_KEY)

# Save records in Algolia index
_client.save_objects(
    index_name=ALGOLIA_INDEX_NAME,
    objects=objects,
)
