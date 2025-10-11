---
title: "打开网络共享时提示：不允许一个用户使用一个以上用户名与一个服务器或共享资源的多重连接"
date: 2020-10-30T14:25:35+08:00
tags: [
    "windows"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

win19打开网络共享时若出现以下提示
![](http://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCE57aafc7c23cd48a48aeaf395f3d6d1c8/136)
则需要断开已有的网络共享链接后再试,用下面的指令
```
net use * /del /y
```
