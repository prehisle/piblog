---
title: "Docker初试2"
date: 2020-04-30T14:24:21+08:00
tags: [
    "docker"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

### 试创建java环境镜像

#### 创建一个目录专门用于制作镜像

```
mkdir dk_java
cd dk_java
```

#### 复制jdk发布包到当前目录

```
cp  /mnt/hgfs/share_disk/dms_dh_0417/dms/dms_server/jdk-8u91-linux-x64.tar.gz .
```

#### 创建Dockerfile

```
FROM centos:centos7
MAINTAINER sToa
ADD jdk-8u91-linux-x64.tar.gz /home
ENV JAVA_HOME /home/jdk1.8.0_91
ENV JRE_HOME /home/jdk1.8.0_91/jre
ENV PATH $JAVA_HOME/bin:$PATH
```

#### 使用Dockerfile构建jdk1.8镜像

```
docker build -t jdk1.8 .
```

#### 启动新构建的镜像

```
 docker run -di --name=jdk1.8 jdk1.8
```

#### ssh到运行的容器

```
docker exec -it jdk1.8 /bin/bash
```

#### 确认java环境配置成功

```
java -version
```

#### 参考

* [使用Docker构建jdk1.8镜像](https://www.cnblogs.com/ztone/p/10558803.html)

### 使用mysql5.7镜像

#### 在`initdb.d`放置初始化数据库脚本

#### 创建启动容器

```
docker run --name test -v /home/prehisle/tmp/dk_mysql/initdb.d/:/docker-entrypoint-initdb.d -it -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=dms mysql:5.7.22
```

#### 连接数据库

```
mysql -uroot -p
```



### 使用nginx镜像



#### 参考：

* [官方文档](https://hub.docker.com/_/nginx?tab=description&page=1&name=1.16)



### 使用docker-compose

### 安装

```
sudo curl --proxy http://127.0.0.1:10809 -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### 启

```
docker-compose up
```

#### 停

```
docker-compose stop
```

#### 删除

```
docker-compose rm
```



#### 参考

* [Docker之Mysql数据持久化](https://blog.csdn.net/qq_38239730/article/details/90484304)
* [Docker Hub MySQL官方镜像实现首次启动后初始化库表](https://blog.csdn.net/loiterer_y/article/details/82984549)
* [Docker构建MySQL镜像并初始化](https://blog.csdn.net/Wonderful_sky/article/details/94312357)
* https://hub.docker.com/_/mysql
* [使用Docker搭建MySQL服务](https://www.cnblogs.com/sablier/p/11605606.html)
* [docker-compose 一键部署 mysql-nginx-tomcat](https://www.jianshu.com/p/a445242cc4d2)
* https://blog.csdn.net/Wonderful_sky/article/details/94312357
* [Docker 入门教程 阮一峰](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
* [Docker 微服务教程](http://www.ruanyifeng.com/blog/2018/02/docker-wordpress-tutorial.html)
* [Docker Compose官方文档](https://docs.docker.com/compose/)
* [docker-compose 中volumes参数说明](https://blog.csdn.net/AV_woaijava/article/details/86685950)
* [一分钟看懂Docker的网络模式和跨主机通信](https://www.a-site.cn/article/169899.html)
* [Docker 网络模式、配置桥接网络](https://blog.csdn.net/weixin_34138056/article/details/92234635)