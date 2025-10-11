---
title: "openwrt failsafe模式修改root密码"
date: 2020-09-29T15:24:45+08:00
tags: [
    "openwrt"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

* 进入`failsafe`模式后，使用`passwd`修改密码会提示文件只读，这时需要先执行`mount_root`再修改