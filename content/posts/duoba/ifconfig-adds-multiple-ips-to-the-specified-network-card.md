---
title: "ifconfig给指定网卡增加IP"
date: 2020-06-27T13:43:43+08:00
tags: [
    ""
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## ifconfig给指定网卡增加IP

```
ifconfig eth1:2 10.10.20.15 netmask 255.255.255.0
```

删除ip用

```
ip addr delete 10.10.20.15 dev eth1:2
```
