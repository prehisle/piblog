---
title: "linux网络调试常用指令"
date: 2020-11-11T17:28:34+08:00
tags: [
    "linux"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

### 清空arp缓存
```
ip -s -s neigh flush all
```

### SNAT
```
iptables -t nat -I POSTROUTING -s 192.168.23.232/32 -j SNAT --to 192.168.23.1
```

### shell设置当前目录为环境变量
```
export PYTHONPATH=$(pwd)
```

### iptables日志调试
```
iptables -t mangle -I PREROUTING -p udp --dport 5060 -j log
```