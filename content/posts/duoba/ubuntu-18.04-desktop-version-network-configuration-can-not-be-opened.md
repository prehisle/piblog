---
title: "ubuntu 18.04桌面版网络配置打不开"
date: 2020-06-27T13:42:27+08:00
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

### ubuntu 18.04桌面版网络配置打不开

```
sudo apt-get install --reinstall --purge gnome-control-center
```

再不行就参考[Ubuntu 18.04 Ethernet not managed](https://askubuntu.com/questions/1115117/ubuntu-18-04-ethernet-not-managed)

```
superuser@SuperTower:~$ cat /etc/NetworkManager/NetworkManager.conf 
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true

[device]
wifi.scan-rand-mac-address=no


superuser@SuperTower:~$ cat /usr/lib/NetworkManager/conf.d/10-globally-managed-devices.conf
[keyfile]
unmanaged-devices=*,except:type:wifi,except:type:wwan


superuser@SuperTower:~$ cat /etc/NetworkManager/conf.d/10-globally-managed-devices.conf
[keyfile]
unmanaged-devices=none
```

记得要重启生效