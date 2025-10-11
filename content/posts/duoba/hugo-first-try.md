---
title: "Hugo初试"
date: 2020-03-01T17:44:04+08:00
tags: [
    "Hugo",
]
categories: [
    "技术",
]

author: "prehisle"
toc: true
autoCollapseToc: true
---


## 安装

### 安装choco

```
Set-ExecutionPolicy Bypass -Scope Process
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

### 安装hugo

```
choco install hugo-extended -confirm
```



## 基本使用

### 创建新站

```
hugo new site hugo2
```

### 初始化git

```
cd hugo2
git init
```

### 安装主题Book

```
git submodule add https://github.com/alex-shpak/hugo-book themes/book
hugo server --minify --theme book
```


### 创建新文章

`hugo new posts/hugo.md`

### 启动服务器

`hugo server -D`

### hugo-book主题开启KaTeX、Mermaid

```
# Needed for mermaid/katex shortcodes
[markup]
[markup.goldmark.renderer]
  unsafe = true
```

### hugo-book启用中文搜索

```
languageCode = "cn"
defaultContentLanguage = 'cn'
[languages]
[languages.cn]
  languageName = 'Chinaese'
  contentDir = 'content'
  weight = 1
```

