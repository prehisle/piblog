---
title: "Ipsec使用证书认证"
date: 2020-03-24T10:23:33+08:00
tags: [
    "ipsec"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---





## 尝试

### win7客户端

* 按文档里配置win7客户端，返回错误809,服务端错误“with unencrypted notification NO_PROPOSAL_CHOSEN”，未能解决，放弃。

* 有人说c/s两端都在同一个局域网段是无法使用证书连接的，未验证非同网段情况

### openwrt19.07客户端

用openwrt19.07里的libreswan作为客户端尝试

使用配置

```
conn vpn.example.com
        left=%defaultroute
        leftcert=win7client.example.com
        leftid=%fromcert
        leftrsasigkey=%cert
        leftsubnet=0.0.0.0/0
        leftmodecfgclient=yes
        right=vpn.example.com
        rightsubnet=0.0.0.0/0
        rightid=@vpn.example.com
        rightrsasigkey=%cert
        narrowing=yes
        ikev2=insist
        rekey=yes
        fragmentation=yes
        mobike=yes
        auto=add
        dpddelay=30
        dpdtimeout=120
        dpdaction=clear
```

报错

```
root@OpenWrt:~# ipsec auto --add vpn.example.com
036 MOBIKE kernel support missing for netkey interface: CONFIG_XFRM_MIGRATE && CONFIG_NET_KEY_MIGRATE
```

将mobike=yes关闭，报另一个错

```
002 "vpn.example.com"[3] 192.168.23.32 #7: received INTERNAL_IP4_ADDRESS 192.168.66.1
002 "vpn.example.com"[3] 192.168.23.32 #7: received INTERNAL_IP4_DNS 114.114.114.114
003 "vpn.example.com"[3] 192.168.23.32 #7: ERROR: netlink response for Add SA esp.6608fc4b@192.168.23.32 included errno 2: No such file or directory
002 "vpn.example.com"[3] 192.168.23.32 #7: setup_half_ipsec_sa() hit fail:
036 "vpn.example.com"[3] 192.168.23.32 #7: encountered fatal error in state STATE_PARENT_I2
```

[参考这里](https://github.com/hwdsl2/setup-ipsec-vpn/issues/102#issuecomment-274357372)决定放弃，试其他

### 尝试非官方搞法

* [文档链接](https://gitee.com/zgmgt/setup-ipsec-vpn/blob/56a96603f916737f1769ed1898fbb66aee21a024/docs/ikev2-howto-zh.md)

* win10尝试失败

* win7再次尝试成功,能正常连接的配置如下

  [注册表修改](https://github.com/hwdsl2/setup-ipsec-vpn/blob/master/docs/clients-zh.md#windows-错误-809)

  ```
  root@OLYM-SW:~# cat /etc/ipsec.d/ikev2-cp.conf 
  conn ikev2-cp
    left=192.168.23.32
    leftcert=192.168.23.32
    leftid=@192.168.23.32
    leftsendcert=always
    leftsubnet=0.0.0.0/0
    leftrsasigkey=%cert
    right=%any
    rightaddresspool=192.168.43.10-192.168.43.250
    rightca=%same
    rightrsasigkey=%cert
    modecfgdns1=8.8.8.8
    #modecfgdns2=8.8.4.4
    narrowing=yes
    dpddelay=30
    dpdtimeout=120
    dpdaction=clear
    auto=add
    ikev2=insist
    rekey=no
    pfs=no
    fragmentation=yes
    #forceencaps=yes
    ike=aes256-sha2,aes128-sha2,aes256-sha1,aes128-sha1,aes256-sha2;modp1024,aes128-sha1;modp1024
    phase2alg=aes_gcm-null,aes128-sha1,aes256-sha1,aes128-sha2,aes256-sha2  
    ms-dh-downgrade=yes
    #mobike=yes
  
  ```

  ```
  root@OLYM-SW:~# certutil -L -d sql:/etc/ipsec.d
  
  Certificate Nickname                                         Trust Attributes
                                                               SSL,S/MIME,JAR/XPI
  
  Example CA                                                   CTu,u,u
  192.168.23.32                                                u,u,u
  winclient                                                    u,u,u
  
  ```
 

  
  ![image-20200324210741891](https://note.youdao.com/yws/public/resource/41112cc5871c7abf8ae2c90c3f174804/xmlnote/a7c8d4f6340c4fb0_124b4e56f64a48449d70768bbfa81f3d/23448)
  
  
  
  ![image-20200324210758832](https://note.youdao.com/yws/public/resource/41112cc5871c7abf8ae2c90c3f174804/xmlnote/b3140fe84c8b8610_6167f958aef649718465b9c8fe50402e/23449)


  ![image-20200324210815873](https://note.youdao.com/yws/public/resource/41112cc5871c7abf8ae2c90c3f174804/xmlnote/image-20200324210815873_a92455ff24a14e2388ea3bb25ec3a2d6/23432)

  ![image-20200324211014001](https://note.youdao.com/yws/public/resource/41112cc5871c7abf8ae2c90c3f174804/xmlnote/image-20200324211014001_2d56db03186b4d84ac0b8674f472cc01/23433)

  ![image-20200324211049291](https://note.youdao.com/yws/public/resource/41112cc5871c7abf8ae2c90c3f174804/xmlnote/image-20200324211049291_dd07d4e9ff2041f195c6a356b3d63023/23434)

  

### 200326 再次尝试

按[LibreSwan IPsec IKEv2 VPN on RHEL 8 Beta Server and Windows 10 Client](https://dc77312.wordpress.com/2019/01/09/libreswan-ipsec-ikev2-vpn-on-rhel-8-beta-server-and-windows-10-client/)里的步骤来，win7/win10都一次成功

与之前的尝试，不同的地方有

1. 证书生成时多加一项选择

   ```
    1 - Client Auth
   ```

2. libreswan配置文件不同

   ```
   conn roadwarrior
     left=192.168.23.32
     leftcert=192.168.23.32
     leftid=@192.168.23.32
     leftsourceip=192.168.23.32
     leftsendcert=always
     leftsubnet=0.0.0.0/0
     leftrsasigkey=%cert
     right=%any
     rightaddresspool=10.9.0.2-10.9.0.254
     rightca=%same
     rightrsasigkey=%cert
     modecfgdns="1.1.1.1,1.0.0.1"
     narrowing=yes
     dpddelay=30
     dpdtimeout=120
     dpdaction=clear
     auto=add
     ikev2=insist
     rekey=no
     fragmentation=yes
     ike=aes256-sha2_512;modp2048,aes128-sha2_512;modp2048,aes256-sha1;modp1024,aes128-sha1;modp1024
   ```
   
3. windows上的连接配置不同

   * 数据加密选“可选加密”，经测试这里选其他都报“13868：策略匹配错误”
   * 高级设置中的"移动性"开启，经测试这个开关不影响
   * 

## 技术点

### 开启日志

```
root@OLYM-SW:~# cat /etc/ipsec.conf
config setup
	protostack=netkey
	# 加入以下配置
	plutodebug=all

```

### 查看日志

```
logread -f
```



## 问题点

### ipsec initnss报错certutil: not found

```
root@OpenWrt:~# ipsec initnss
Initializing NSS database

/usr/sbin/ipsec: line 377: certutil: not found
Failed to initialize nss database sql:/etc/ipsec.d

```

需安装libnss，[更多参考](https://github.com/openwrt/packages/blob/master/libs/nss/Makefile)

```
root@OpenWrt:~# opkg install libnss
```





## 参考资料

[FAQ-IKEv1和IKEv2有哪些区别](https://support.huawei.com/enterprise/zh/knowledge/EKB1000052323)

[VPN server for remote clients using IKEv2](https://libreswan.org/wiki/VPN_server_for_remote_clients_using_IKEv2)

[ipsec.conf - IPsec configuration and connections](https://libreswan.org/man/ipsec.conf.5.html)

[Setup IKEv2/Windows 10](https://github.com/hwdsl2/setup-ipsec-vpn/issues/106)

[ 如何配置 IKEv2 VPN: Windows 7 和更新版本](https://gitee.com/zgmgt/setup-ipsec-vpn/blob/56a96603f916737f1769ed1898fbb66aee21a024/docs/ikev2-howto-zh.md)

[Windows IKEv2 Error 809](https://swan.libreswan.narkive.com/bB2k6alL/windows-ikev2-error-809)

[ Windows 错误 809](https://gitee.com/zgmgt/setup-ipsec-vpn/blob/56a96603f916737f1769ed1898fbb66aee21a024/docs/clients-zh.md#故障排除)

[win7/8 IKEv2 VPN证书导入和正确使用方法](https://www.zxar520.com/webseo/841.html)

[windows使用ikev2遇到的坑，及批处理batch脚本和powershell脚本](https://www.willnet.net/index.php/archives/113/)

## 参考项目

[setup-ipsec-vpn](https://gitee.com/zgmgt/setup-ipsec-vpn)

**[setup-ipsec-vpn github](https://github.com/hwdsl2/setup-ipsec-vpn)**





