---
title: "Openssl知识点"
date: 2020-03-25T20:39:18+08:00

tags: [
    "openssl"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

#### 文件格式

只有pfx格式的数字证书是包含有私钥的，cer格式的数字证书里面只有公钥没有私钥

##### .pfx

- 存放公钥和私钥
- 主要用于windows平台，浏览器可以使用，也是包含证书和私钥，获取私钥需要密码才可以

##### .der

- 二进制编码的证书
- DER扩展用于二进制DER编码证书。这些文件也可能带有CER或CRT扩展名
- 经常使用.cer用作扩展名，所有类型的认证证书和私钥都可以存储为DER格式

##### .pem

- ASCII(Base64)编码的证书
- 有类似"-----BEGIN CERTIFICATE-----" 和 "-----END CERTIFICATE-----"的头尾标记
- PEM格式通常用于数字证书认证机构（Certificate Authorities，CA），扩展名为.pem, .crt, .cer, and .key

##### .cer,.crt

- 证书文件，可以是DER编码，也可以是PEM编码。CRT是微软型式的证书

- 存放公钥，没有私钥

##### .key

用于PCSK#8的公钥和私钥。这些公钥和私钥可以是DER编码或者PEM编码。



#### 名称解释

##### X.509

证书文档，根据RFC 5280标准编码并签发



#### 格式转换


 可以使用OpenSSL命令行工具在不同证书格式之间的转换

##### PEM to DER

```
   openssl x509 -outform der -in certificate.pem -out certificate.der
```

##### PEM to PFX 

```
  openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile CACert.crt
```

##### DER to PEM

```
   openssl x509 -inform der -in certificate.cer -out certificate.pem
```

##### PFX to PEM

```
   openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes   
```

  （PFX转PEM后certificate.cer文件包含认证证书和私钥，需要把它们分开存储才能使用。）



#### 知识点

1. 使用公钥操作数据属于加密
2. 使用私钥对原文的摘要操作属于签名
3. 公钥和私钥可以互相加解密
4. 不同格式的证书之间可以互相转换
5. 公钥可以对外公开，但是私钥千万不要泄露，要妥善保存