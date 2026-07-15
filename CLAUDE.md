# CLAUDE.md

本文件指导 Claude Code（及其他 AI agent）维护本博客。**先读它再动手**。

## 这是什么

个人技术博客「多多小站」，线上 <https://blog.share4y.cn>。

- **技术栈**：Hugo（extended）+ [LoveIt](https://github.com/dillonzq/LoveIt) 主题（**git submodule**，位于 `themes/LoveIt`）。
- **托管**：GitHub Pages。**内容在本地写，push 到 `master` 后由 GitHub Actions 自动构建部署**——不自建服务器托管（见下「发布」）。
- **默认分支**：`master`（`.github/workflows/deploy.yml` 触发分支为 `main`/`master`）。

## 写一篇新文章

**放哪**：`content/posts/` 下三个分区——`duoba/`（技术，绝大多数在这）、`duoduo/`（书法/生活）、`duoma/`。技术文一律进 `duoba/`。

**形态**：**页面包**（近期约定）——建目录 `content/posts/duoba/<英文-slug>/index.md`，配图直接丢进同目录用相对路径 `![](图名.png)` 引用。

**frontmatter**：TOML `+++`，与 `archetypes/default.md` 一致：

```toml
+++
date = '2026-07-15T15:40:00+08:00'   # RFC3339，带 +08:00 时区；未来日期不会被构建
draft = true                          # 草稿；定稿改 false 才会发布
title = '文章标题'
+++
```

`tags = [...]` / `categories = [...]` 可选。也可 `hugo new posts/duoba/<slug>/index.md` 生成骨架（archetype 默认 `draft = true`）。

**URL 规律**：`hugo.toml` 里 `[Permalinks] posts = ":year/:month/:contentbasename"`，所以线上地址是 `/<年>/<月>/<slug>/`。例：2026-07 的 `relay-model-authenticity-blind-test` → `/2026/07/relay-model-authenticity-blind-test/`。

## 发布

1. `draft = false`。
2. `git add` 该文章目录 + `git commit` + `git push` 到 `master`。
3. GitHub Actions（`Build and Deploy Hugo to GitHub Pages`）自动跑：Hugo 构建 → 更新 Algolia 搜索索引 → 部署到 Pages。**约 2–4 分钟**上线。
4. 验证：`curl -sL -o /dev/null -w "%{http_code}" <文章URL>` 应 200；或看 Actions run 结论。

commit subject 用平白描述即可；结尾带 `Co-Authored-By` trailer。

## 站内搜索（Algolia）

搜索走 **Algolia**（曾用过 lunr，中文检索效果差，已换回）。

- **前端配置**：`hugo.toml` 的 `[languages.zh-cn.params.search]` → `type = "algolia"`，其下 `[...search.algolia]` 有 `index` / `appID` / `searchKey`。**App ID 和 searchKey 是公开只读值**，可以明文提交。
- **索引上传**：CI 每次部署跑 `scripts/upload_index_to_algolia.py`，把 Hugo 生成的 `public/index.json`（来自 `hugo.toml` 的 `[outputs] home = [..., "JSON"]`）推到 Algolia。**Admin Key（写密钥）存仓库 secret `ALGOLIA_ADMIN_KEY`**，绝不提交进代码。
- **⚠️ 别让应用休眠**：Algolia 免费版会**回收长期不活动的应用**（历史上就这么坏过一次：应用被删→域名解析不了→搜索全废）。好在每次发文触发的索引上传都算活动——**保持偶尔发文即可**；连续大半年不发才有被回收风险（回收前一般发预警邮件）。
- **爆炸半径已隔离**：`deploy.yml` 里 Algolia 上传步是 `continue-on-error: true`——即使 Algolia 再出问题，也只是搜索索引不更新，**站点照常部署**，不会像当初那样连带冻住整站。

## 坑

- **主题是 submodule**：本地新 clone 后主题目录是空的；CI 用 `submodules: true` checkout 没问题，但本地要 `hugo server` 预览须先 `git submodule update --init --depth 1 themes/LoveIt`。
- **构建产物不提交**：`.gitignore` 已忽略 `/public/`、`/resources/`、`/.env`——别把它们加进来。
- **本地预览是可选项**：发布链路是 push→CI，不依赖本地 Hugo。要预览再装 `hugo extended` + 初始化 submodule + `hugo server -D`（`-D` 显示草稿）。
