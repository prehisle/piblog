---
title: "win10指令备忘"
date: 2020-11-20T11:28:24+08:00
tags: [
    "win10"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

### 打开win10的启动目录
```
shell:Common Startup
```

### IE启动时最大化
```
iexplore.exe -k
```

### chrome启动最大化
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" -kiosk http://127.0.0.1:8080/index.html#/home
```

### VMware自启动
```
"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" start "D:\Virtual Machines\Ubuntu64\Ubuntu64.vmx" nogui
```

### win10专业版没有自支登录选项
用`Control Userpasswords2`命令进入配置界面
如图：
![](https://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCE09a9436d95a440489307c235c8ae6f63/141)
需要修改注册表,将下的的内容保存到.reg文件后双击导入
```
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\PasswordLess\Device];
"DevicePasswordLessBuildVersion"=dword:00000000
```
之后可以看到自动登录选项可以配置了,如图
![](https://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCE2171565b968846218a08b4c0c2e105d3/142)


### 查看系统信息，安装时间等
```
systeminfo
```