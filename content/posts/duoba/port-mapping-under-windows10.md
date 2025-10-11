---
title: "windows10下端口映射"
date: 2020-09-02T16:08:00+08:00
tags: [
    "windows10"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

#### 显示当前映射的端口
```
netsh interface portproxy show all
```

#### 添加一个映射端口
```
netsh interface portproxy add v4tov4 listenport=10022 listenaddress=* connectport=22 connectaddress=192.168.100.1 protocol=tcp
```

#### 删除一个映射端口
```
netsh interface portproxy del v4tov4 listenport=10022 listenaddress=*
```

#### 常见问题
* 查端口指令
```
NETSTAT.EXE -antp tcp|findstr LISTENING|findstr 22
```
如果没有监听映射的端口，请检查是否开户了IP Help服务
