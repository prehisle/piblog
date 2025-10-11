---
title: "kvm硬盘扩容"
date: 2020-04-28T12:49:13+08:00
tags: [
    "kvm", "resize", "qemu-img"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## 母机

```
qemu-img resize /home/kvm/kvmimg/GD2_TG2.img +100G
```
若出现错误，可以用下面的命令修复
```
qemu-img check -r all /home/kvm/kvmimg/GD2_NS2.img
```

## 子机

```
fdisk -l
fdisk /dev/vda
  p
  n
  回车
  回车
  ...
  w
reboot
pvcreate /dev/vda3
用lvs或vgs指令查看VG
vgextend {你的VG} /dev/vda3
lvextend -l +100%FREE /dev/centos/root
resize2fs /dev/centos/root # 报错后改用下面的命令
xfs_growfs /dev/mapper/centos-root
df -h
```



参考：

* [KVM虚拟磁盘扩容， qemu-img resize](https://blog.wiloon.com/?p=12049)

* [Linux resize2fs: Bad magic number in super-block错误的解决方法](https://blog.csdn.net/qq_22083251/article/details/80417097)