---
title: "vmware复制出来的ubuntu虚拟机dhcp获取不到新IP的问题"
date: 2020-11-19T17:21:50+08:00
tags: [
    "vmware", "ubuntu"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

需要修改`/etc/netplan/50-cloud-init.yaml`,将工作网卡上加入以下设定
```
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: yes
      dhcp-identifier: mac // 这是新加的
```

* 参考：https://unix.stackexchange.com/questions/419321/why-are-my-cloned-linux-vms-fighting-for-the-same-ip
