---
title: "解决/var/lib/docker/volumes占用巨大空间"
date: 2020-09-11T09:33:29+08:00
tags: [
    "docker"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

```
# 查看docker空间占用
docker system df
# 查看volumes空间占用
sudo du -s -h /var/lib/docker/volumes/* | sort -nr
# 清理volume
docker volume prune -f
```

