---
title: "ubuntu18.04_docker初试"
date: 2020-04-29T15:30:57+08:00
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

### ubuntu18.04 docker初试
#### 安装
```
sudo apt-get install docker
```

#### 启停

```
sudo service docker start
sudo service docker stop
```

#### 列出镜像

```
docker images
```

#### 搜索镜像

```
docker search nginx
```

#### 拉取镜像

```
docker pull centos:7
```

#### 设置加速镜像源到阿里云镜像加速器
[阿里云镜像加速器](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors?accounttraceid=4f496d6442044048963cd3f519654b44fjdt)

#### 删除镜像

```
docker rmi 602e111c06b6
```

`602e111c06b6`为`docker images`里的`IMAGE ID `

#### 创建与启动容器

##### 交互式容器

```
docker run -it --name=mycentos centos /bin/bash
```

##### 守护式容器

```
docker run -di --name=mycentos2 centos
```

#### 查看容器

* 查看正在运行容器：

```undefined
 docker ps
```

* 查看所有的容器（启动过的历史容器）：

```undefined
 docker ps –a
```

*  查看最后一次运行的容器：

```undefined
 docker ps –l
```

* 查看停止的容器

```undefined
 ocker ps -f status=exited
```

#### 启停容器

```
docker start mycentos2
docker stop mycentos2
```

#### 查看容器信息

```
 docker inspect mycentos2
```

#### 查看容器IP地址

```
docker inspect --format='{{.NetworkSettings.IPAddress}}' mycentos2
```

#### 删除容器

```
docker rm  mycentos
```

#### 登录守护式容器

```
docker exec -it mycentos /bin/bash
```

#### 文件拷贝

```
docker cp testdisk.log mycentos:/home
docker cp  mycentos:/root/abcde .
```

#### 目录挂载

```
docker run -di -v /home/prehisle/tmp:/home/tmp --name=mycentos2 centos
```

若报`Permission denied`,加入`--privileged=true`

```
 docker run -d -i --privileged=true -v /home/html:/home/vhtml --name=mycentos4 centos:7
```

#### 查询镜像tag

在[hub.docker.com](https://hub.docker.com/)搜索再查看`Tags`,如[centos的tag链接](https://hub.docker.com/_/centos?tab=tags)


### 参考

* [容器部署解决方案Docker](https://www.jianshu.com/p/e7071fbe00c4)
* [修改Docker容器启动配置参数](https://blog.csdn.net/qq_35119422/article/details/85869361)
* [基于docker部署mysql的数据持久化问题](https://www.jianshu.com/p/530d00f97cbf)
* [Docker：Docker Compose 详解](https://www.jianshu.com/p/658911a8cff3)
* [「走进k8s」Docker三剑客之Docker Compose（七）](https://www.jianshu.com/p/9b9887fdd398)
* [你必须知道的Dockerfile](https://www.cnblogs.com/edisonchou/p/dockerfile_inside_introduction.html)
* [Docker三剑客之Docker Swarm](https://www.cnblogs.com/zhujingzhi/p/9792432.html)
* [Docker三剑客之Docker Compose](https://www.cnblogs.com/zhujingzhi/p/9786622.html)
* [docker桥接网络](https://blog.csdn.net/qq_41772936/article/details/81192369)
* [「走进k8s」Docker 网络模式（六）](https://www.jianshu.com/p/42522b90d780)
* https://docs.docker.com/compose/
* [docker、docker-compose、docker swarm和k8s的区别](https://www.jianshu.com/p/2a9ae69c337d)

* [深刻理解Docker镜像大小](https://www.cnblogs.com/claireyuancy/p/7029126.html)
* [k8s简介](https://www.jianshu.com/p/502544957c88)
* [创建自己的Docker基础镜像](https://www.cnblogs.com/cocowool/p/make_your_own_base_docker_image.html)

* [如何选择Docker基础镜像](https://blog.csdn.net/nklinsirui/article/details/80967677)
* [容器技术Docker、Docker-Compose、k8s的演变](https://blog.csdn.net/jjzhoujun2010/article/details/103945989)