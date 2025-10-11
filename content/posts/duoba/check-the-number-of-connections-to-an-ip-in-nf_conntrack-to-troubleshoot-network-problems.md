---
title: "查看nf_conntrack中某个ip的连接数量,排查网络问题"
date: 2020-08-28T10:00:15+08:00
tags: [
    "iptables", "nf_conntrack"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

外网网络卡成翔了，排除哪个ip把带宽占满了
```
cat /proc/net/nf_conntrack | grep 192.168.23.20 | wc -l
```