---
title: "Python备忘"
date: 2020-03-28T18:33:01+08:00
tags: [
    "python"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---


### 报error: invalid command 'bdist_wheel'

```
pip install wheel
```

### 时间转换

[Python获取秒级时间戳与毫秒级时间戳](https://www.cnblogs.com/fangbei/p/python-time.html)

### ubuntu18.04使用pip安装某包时报错

![image-20200401153406748](http://note.youdao.com/yws/public/resource/41112cc5871c7abf8ae2c90c3f174804/xmlnote/image-20200401153406748_4d9d6a45b0f34a249060fa6f5ce92a44/23489)

```
prehisle@ubuntu:~/tmp/tyoudaoimg$ pip install -i https://pypi.org/simple youdaopic==0.0.9
Collecting youdaopic==0.0.9
  Could not find a version that satisfies the requirement youdaopic==0.0.9 (from versions: 0.0.1)
No matching distribution found for youdaopic==0.0.9

```

改用pip3安装成功

### windows下pip安装包时报错`basetsd.h`未找到

```
Build error on Win 10: Cannot open include file: 'basetsd.h': No such file or directory
```

参考:https://github.com/Azure/azure-iot-sdk-python/issues/82

```
Launch Microsoft Visual C++ Build Tools setup again and also select windows 8.1 / 10 SDK depending upon your OS:
https://stackoverflow.com/a/42624713/4063622
```

### windows下`auto-py-to-exe`报`tkinter not found`

```
G:\2020\youdaopic\build>auto-py-to-exe
Error: tkinter not found
For linux, you can install tkinter by executing: "sudo apt-get install python3-tk"
```

重新安装python，勾选安装`tcl/tk and IDLE`

### 报错`No module named PIL`

```
pip install image
```

### `open`报`UnicodeDecodeError`

```
UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 23: illegal multibyte sequence
```

加入参数`encoding`，如下

```
open(filename, 'r', encoding="utf-8")
```

### 使用kill命令发送ctrl+c(KeyboardInterrupt)结束python程序
```
kill -SIGINT 23354
```

### logging.basicConfig中配置了logging.INFO,logging.info仍不生效的问题
* 需要把logging.basicConfig调到输出第一条log之前,可以放在import logging之后