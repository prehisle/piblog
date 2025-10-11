---
title: "win10系统主机路由添加删除"
date: 2021-03-05T21:58:46+08:00
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

## 查看路由接口号
```
C:\WINDOWS\system32>route print -4
===========================================================================
接口列表
 18...00 ff b1 52 a3 ed ......TAP-Windows Adapter V9
 19...b0 25 aa 27 b2 69 ......Realtek PCIe GbE Family Controller
 23...7c 76 35 e3 d5 2e ......Microsoft Wi-Fi Direct Virtual Adapter
 13...7e 76 35 e3 d5 2d ......Microsoft Wi-Fi Direct Virtual Adapter #2
 21...00 50 56 c0 00 01 ......VMware Virtual Ethernet Adapter for VMnet1
 20...00 50 56 c0 00 08 ......VMware Virtual Ethernet Adapter for VMnet8
 17...7c 76 35 e3 d5 2d ......Intel(R) Wireless-AC 9462
 16...7c 76 35 e3 d5 31 ......Bluetooth Device (Personal Area Network)
  1...........................Software Loopback Interface 1
===========================================================================
```
上面接口列表中的18,19,23,13就是接口号，添加主机路由时对应的参数if

## 增加主机路由
```
route add 192.168.23.104 mask 255.255.255.255 10.17.251.79 if 18
```

## 删除主机路由
```
route delete 192.168.23.104
```