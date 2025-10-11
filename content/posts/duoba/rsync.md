---
title: "rsync技术"
date: 2020-03-23T13:35:04+08:00
tags: [
    "rsync",
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## windows用rsysc同步到linux(ubuntu 18.04)

### server端

```
root@doduo:~# cat /etc/rsyncd.conf
# sample rsyncd.conf configuration file

# GLOBAL OPTIONS

#motd file=/etc/motd
#log file=/var/log/rsyncd
# for pid file, do not use /var/run/rsync.pid if
# you are going to run rsync out of the init.d script.
# The init.d script does its own pid file handling,
# so omit the "pid file" line completely in that case.
# pid file=/var/run/rsyncd.pid
#syslog facility=daemon
#socket options=

# MODULE OPTIONS

[www]

	comment = public archive
	path = /var/www/html
	use chroot = yes
#	max connections=10
	lock file = /var/lock/rsyncd
# the default for read only is yes...
	read only = false
	list = yes
	uid = www-data
	gid = www-data
#	exclude = 
#	exclude from = 
#	include =
#	include from =
	auth users = www
	secrets file = /etc/rsyncd.secrets
	strict modes = yes
#	hosts allow = *
#	hosts deny =
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
#	log format = %t: host %h (%a) %o %f (%l bytes). Total %b bytes.
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz
	
	# 避免各种权限问题
	incoming chmod = Du=rwx,Dgo=rx,Fu=rwx,Fgo=rx 

```

### client端

#### 客户端下载安装

* [windows客户端cwRsync下载](https://www.itefix.net/cwrsync-free-edition)
* 解压后添加rsync.exe所在目录到path环境变量



#### 同步指令

```
rsync.exe  -azvP --password-file=passwd --progress public/* www@123.57.245.83::www
```

## 参考资料:

[Rsync 故障排查整理](https://www.cnblogs.com/wang-xd/p/6551402.html)