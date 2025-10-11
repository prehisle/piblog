---
title: "ubuntu18.04 root权限下的pycharm输入中文"
date: 2021-02-06T11:02:36+08:00
tags: [
    "pycharm", "输入法"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

在`pycharm.sh`中添加以下内容
```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```
