---
title: "解决vscode'系统上禁止运行脚本'问题"
date: 2020-08-15T12:39:36+08:00
tags: [
    "vscode"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

在`vscode`的控制台`terminal`中执行`ps1`脚本，可能会报错:
```
flourish : 无法加载文件 C:\Users\demon\AppData\Roaming\npm\flourish.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 1
+ flourish new my_template
+ ~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
解决办法是:
1. 进入`powershell`
2. 执行
```
set-ExecutionPolicy RemoteSigned
```
3. 选`Y`
