---
title: "Linux快速生成用于测试的指定大小文件"
date: 2020-06-30T17:38:50+08:00
tags: [
    "linux", "test"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

* 生成一个3M的文件
```
dd if=/dev/zero of=/tmp/testfile bs=1M count=3
```
