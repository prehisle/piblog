---
title: "代理设置大全"
date: 2020-03-24T15:29:18+08:00
tags: [
    "常用"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## linux terminal下设置代理

```
export http_proxy="http://127.0.0.1:10809"
export https_proxy="http://127.0.0.1:10809"
```

| 系统          | 是否有效 |
| ------------- | :--------: |
| Openwrt 19.07 | :(far fa-check-square fa-fw):       |
| MINGW64       | :(far fa-check-square fa-fw):        |
| Ubuntu 18.04  | :(far fa-check-square fa-fw):        |


## ubuntu 18.04下apt-get设置代理
```
sudo apt-get upgrade -o Acquire::http::proxy="http://127.0.0.1:10809"
```

## curl设置代理

```
sudo curl --proxy http://127.0.0.1:10809 -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

## git设置代理
```
git config --global http.proxy socks://192.168.23.12:10808
git config --global https.proxy socks://192.168.23.12:10808
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## windows cmd下设置代理

使用http模式

```
set http_proxy=http://127.0.0.1:10809
set https_proxy=http://127.0.0.1:10809
```

或socks模式

```
set http_proxy=socks://192.168.23.12:1081
set https_proxy=socks://192.168.23.12:1081
```

| 命令         | http模式 | socks模式                     |
| ------------ | -------- | ----------------------------- |
| ridk install | √        | ×                             |
| pip install  | √        | ×                             |
| PowerShell   | ×        | ×                             |
| cmd          | √        | √(执行curl访问google.com失败) |
| cmd git      | ×        | √                             |

## windows PowerShell设置代理

```
$regPath = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
$proxy = 'http://127.0.0.1:10809'

function Clear-Proxy {
    Set-ItemProperty -Path $regPath -Name ProxyEnable -Value 0
    Set-ItemProperty -Path $regPath -Name ProxyServer -Value ''
    Set-ItemProperty -Path $regPath -Name ProxyOverride -Value ''

    [Environment]::SetEnvironmentVariable('http_proxy', $null, 'User')
    [Environment]::SetEnvironmentVariable('https_proxy', $null, 'User')
}

function Set-Proxy {

    Set-ItemProperty -Path $regPath -Name ProxyEnable -Value 1
    Set-ItemProperty -Path $regPath -Name ProxyServer -Value $proxy
    Set-ItemProperty -Path $regPath -Name ProxyOverride -Value '<local>'

    [Environment]::SetEnvironmentVariable('http_proxy', $proxy, 'User')
    [Environment]::SetEnvironmentVariable('https_proxy', $proxy, 'User')
}

```

**Set-Proxy**开代理，**Clear-Proxy**关代理，这种方法实际是修改的系统代理，设了以后要记得改回来

参考：[给 Windows 的终端配置代理](https://zcdll.github.io/2018/01/27/proxy-on-windows-terminal/) 