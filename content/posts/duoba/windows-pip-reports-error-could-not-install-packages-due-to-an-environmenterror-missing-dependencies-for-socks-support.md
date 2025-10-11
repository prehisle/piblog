---
title: "Windows下pip报ERROR: Could not install packages due to an EnvironmentError: Missing dependencies for SOCKS support."
date: 2020-06-27T14:00:30+08:00
tags: [
    "python", "pip"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## Windows下pip报ERROR: Could not install packages due to an EnvironmentError: Missing dependencies for SOCKS support.

执行下面的命令设置代理

```
set http_proxy=http://127.0.0.1:8001
set https_proxy=https://127.0.0.1:8001
```