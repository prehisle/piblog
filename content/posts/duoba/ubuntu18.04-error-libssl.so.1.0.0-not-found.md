---
title: "ubuntu18.04报错libssl.so.1.0.0未找到"
date: 2020-04-03T15:23:45+08:00
tags: [
    "linux", "备忘"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---



### ubuntu18.04报错libssl.so.1.0.0未找到

* 报错信息

```
error while loading shared libraries: libssl.so.1.0.0: cannot open shared object file: No such file or directory
```

* 解决办法

  先卸载，再安装，如下

```
sudo apt-get remove libssl1.0.0
sudo apt-get install libssl1.0.0:amd64  
```

