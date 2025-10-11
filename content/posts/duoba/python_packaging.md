---
title: "Python程序打包技术学习笔记"
date: 2020-04-01T17:52:50+08:00
tags: [
    "打包", "学习笔记"
]
categories: [
    "python",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## 相关备忘点

### 编译

```
python setup.py build
```

### 安装

```
python setup.py install
```

### 开发模式安装

```
python setup.py develop
```

在修改代码后可以立即使用，不用重新安装

### 打一个源码包

```
python setup.py sdist
```

生成funniest-0.1.tar.gz的源码包

### 从源码包安装

```
tar -zxvf funniest-0.1.tar.gz
python setup.py install
```

若报错`error: can't create or remove files in install directory·`，是因为没有权限改安装命令为`sudo python3 setup.py install`即可

### 依赖不在PyPI中的包的处理

```
setup(
    ...
    dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
    ...
)
```

### 使用setup.py执行单元测试

```
python setup.py test
```

它会自动查找源码目录包含子目录下的所有测试用例，以`test`开头的文件

### 安装命令到系统

有两种方式：

* 使用单独的脚本文件，如windows下的bat脚本，linux下的shell脚本.在`setup`添加

  ```
  scripts=['bin/a.cmd'],
  ```

* 使用包中的某个函数,在`setup`中添加

  ```
  entry_points = {
  	'console_scripts': ['funniest-joke=funniest.command_line:main'],
  }
  ```

### 卸载使用`python setup.py install`安装 的包

```
pip uninstall funniest -y
```

### 发布到pip时打包非py文件(资源文件)

1. 在`setup()`中加入`include_package_data=True`

2. 新建文件`MANIFEST.in`来指定要打包的文件,内容如下

   ```
   include README.rst
   include docs/*.txt
   include funniest/data.json
   ```

## 参考资料

* [教程中文版](https://python-packaging-zh.readthedocs.io/zh_CN/latest/minimal.html)
* [教程英文原版](https://python-packaging.readthedocs.io/en/latest/)

![image-20200505144144242](G:\2020\doduo\content\posts\imgs\image-20200505144144242.png)