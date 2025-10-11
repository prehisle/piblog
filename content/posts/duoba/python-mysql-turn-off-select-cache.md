---
title: "python mysql之关掉select缓存"
date: 2020-08-04T14:37:17+08:00
tags: [
    ""
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

工作中需要写程序判断某条记录是否存在。
调了半天都没弄好，现象是明明删除了某条记录，但在程序中还是能查到。
后在google中查是不是缓存引起的，却查到一个选项`autocommit`,设置为`True`后确实能修复我的问题，上代码

```python
import mysql.connector

from autotest.utils.common import RetryException, call_until_success


class GWDBHelper:
    def __init__(self, host="172.22.40.61", user="root", password="root", database="gw"):
        self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.mydb.autocommit = True  # 就是这个选项

    def is_sip_id_exist(self, sip_id):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM t_ipc_info WHERE sip_id=%s"
        val = (sip_id,)
        mycursor.execute(sql, val)
        mycursor.fetchone()
        row_count = mycursor.rowcount
        return row_count > 0

    @call_until_success(try_times=0, sleep_time=10)
    def wait_sip_id_exist(self, sip_id):
        if not self.is_sip_id_exist(sip_id):
            raise RetryException()
```