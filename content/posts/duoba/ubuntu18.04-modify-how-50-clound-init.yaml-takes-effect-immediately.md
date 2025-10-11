---
title: "ubuntu18.04修改50-clound-init.yaml怎样立即生效"
date: 2020-07-08T14:49:14+08:00
tags: [
    "ubuntu"
]
categories: [
    "技术",
]
keywords: ["ubuntu18.04", "50-clound-init.yaml" , "重启网络"]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## ubuntu18.04修改50-clound-init.yaml怎样立即生效，不需要重启网络
```
ip addr flush dev ens37
```

