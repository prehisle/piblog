---
title: "Ubuntu 18.04调整swap分区"
date: 2020-06-27T13:45:03+08:00
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

### Ubuntu 18.04调整swap分区

```
prehisle@ubuntu:~$ cat /proc/sys/vm/swappiness
60
prehisle@ubuntu:~$ sudo sysctl vm.swappiness=10
vm.swappiness = 10
prehisle@ubuntu:~$ vi /etc/sysctl.conf
```

增加一行

```
vm.swappiness=10 
```

参考：[在Ubuntu 18.04系统中增加和删除SWAP交换分区的方法](http://8u.hn.cn/linuxjc/12271.html)