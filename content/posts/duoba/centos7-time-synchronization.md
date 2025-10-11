---
title: "centos7 时间同步设置"
date: 2020-06-27T13:18:45+08:00
tags: [
    "备忘"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

### centos7 时间同步

```
# 安装
yum install chrony
# 启用
systemctl start chronyd
systemctl enable chronyd
# 设置亚洲时区
timedatectl set-timezone Asia/Shanghai
# 启用NTP同步
timedatectl set-ntp yes
```

参考：

* [centos7之关于时间和日期以及时间同步的应用](https://www.cnblogs.com/lei0213/p/8723106.html)