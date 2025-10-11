---
title: "Ipsec基础知识"
date: 2020-03-26T08:53:37+08:00
tags: [
    "ipsec",
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

## 名词解释
### AH
IPsec Authentication Header IPsec 认证头协议（IPsec AH）是 IPsec 体系结构中的一种主要协议，它为 IP 数据报提供无连接完整性与数据源认证，并提供保护以避免重播情况。

###  ESP 
IPsec Encapsulating Security Payload 封装安全负载,且ESP加密采用的是对称密钥加密算法，能够提供无连接的数据完整性验证、数据来源验证和抗重放攻击服务

### IKE 
Internet key exchange,Internet密钥交换协议

### SA 
Security Association 安全关联，通讯两端建立的联系

### SPI
是为了唯一标识SA而生成的一个32位整数，包涵在AH头和EsP头中

### SPD 
安全策略数据库

### SAD 
安全关联数据库

### PSK
预共享密钥

### PSK
预共享密钥

### EAP
可扩展的身份验证协议

### ISAKMP
Internet Security Association and Key Management Protocol

### IKE SA
ISAKMP Security Association（IKE SA）,IKE SA 要保护的对象是与密钥有关的，IKE 并不直接关心用户数据，并且IKE SA是为安全协商IPsec SA 服务的

### IPsec SA
分为IKE SA 和IPsec SA，两个SA 分别定义了如何保护密钥以及如何保护数据，其实这两个SA 都是由IKE 建立起来的，所以将IKE 的整个运行过程分成了两个Phase



:wq