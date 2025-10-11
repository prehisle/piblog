---
title: "python 16进制字符串与二进制数据互转"
date: 2020-08-24T11:38:19+08:00
tags: [
    "python"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

### hexstr to bin
```python
bytes.fromhex("aabbcc")
b'\xaa\xbb\xcc'
```
或
```python
binascii.unhexlify("aabbcc")
b'\xaa\xbb\xcc'
```
### bin to hexstr
```python
binascii.hexlify(b'\xaa\xbb\xcc')
b'aabbcc'
```
或
```python
b'\xde\xad\xbe\xef'.hex()
'deadbeef'
```