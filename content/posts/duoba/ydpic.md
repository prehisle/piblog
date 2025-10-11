---
title: "Ydpic发布"
date: 2020-04-19T19:16:33+08:00
tags: [
    "ydpic", "python"
]
categories: [
    "技术"
]
author: "prehisle"
toc: true
autoCollapseToc: true
---


## 项目介绍

将`有道云笔记`免费版作为图库使用的小工具，可与`Typora`完美结合

## 效果演示

![ydpic效果演示](https://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/demo_9589e25443f44233b727daa09dfc1623/23)

## 快速上手（WINDOWS）

### 下载软件

| 下载链接                                                     | 说明         |
| ------------------------------------------------------------ | ------------ |
| [码云](https://gitee.com/prehisle/ydpic/attach_files/376879/download) | 有限速50KB/S |
| [蓝奏云](https://prehisle.lanzous.com/iblefxe)               | 推荐         |

### 配置

#### 准备`有道云笔记`账号密码

略

#### 准备`有道云笔记`分享笔记的链接

1. 登录网页版有道云笔记

   [有道云笔记官网](https://note.youdao.com/)

2. 随便分享一个文档,复制分享链接,后面会用到,如下图

   ![获取分享文档链接](https://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/share_note_e64c8a0bd8a24e79b1d472690d5207cb/24)

#### 配置`ydpic`

1. 解压下载的软件

   略

2. 初始化配置文件

用`cmd`进入解压后的文件夹，执行

```
ydpic.exe init
```

在当前目录生成初始配置文件`config.ini`，如图：

![image-20200406195016680](https://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/init_config_922be5aea07a4ad491bb852065617db7/25)

3. 修改配置

打开`config.ini`配置有道云笔记账号密码及分享文档链接，如下图

![image-20200406195112829](https://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/config_4a2c6819d307488c99f7a4591e1d4d42/26)



### 集成到Typora

* 在`Typora`菜单`文件`->`偏好设置..`->`图像`->`自定义命令`中填入，

  ```
  "{ydpic解压路径}\ydpic.exe" upload -c "{ydpic解压路径}\config.ini"
  ```

* 点击`验证图片上传选项`进行上传测试，测试成功大功告成如下图

  ![typora_test](https://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/typora_test_b8d3eeb1d2f545cbb3c5122b6cc4f0d6/27)

## 支持系统

| 系统         | 测试结果 |
| ------------ | -------- |
| win7         | √        |
| win10        | √        |
| ubuntu 18.04 | √        |
| xp           | x        |

## 项目起源

* 免费版的有道云笔记在编写markdown格式的笔记时不支持直接粘贴图片，必须把图片上传到图床后再把url粘贴回来，多有不便
* Typora写Markdown体验实在是爽,但把带有图片的文档发到Blog时需要手动将图片传到图床，麻烦
* 有道云笔记的html格式的笔记可以直接粘贴图片
* Typora支持调用命令行程序上传图片获取url
* 遂写程序模拟上传图片的过程并获取图片url

## 已知问题

* 开启`link_resourceId = True`且上传路径中包含中文的图片时，由于有道云笔记对中文url的支持有问题，故在返回的url中将中文替换成了`_`，这将导致本地图片与图片无法对应上
* 为支持python3.6，直接运行ydpic会报错
  `AttributeError: 'Namespace' object has no attribute 'func'`，请忽略这个错误，不影响实际使用，要看帮助请执行·ydpic -h
  ·。[问题参考](https://github.com/python/typeshed/issues/2415) 
* 有道云笔记做了防盗链，在img标签中加入`referrerPolicy="no-referrer"`可正常显示图片