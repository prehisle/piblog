---
    title: "Git常用"
    date: 2020-03-30T17:26:58+08:00
    tags: [
        "git", "常用"
    ]
    categories: [
        "技术",
    ]
    author: "prehisle"
    toc: true
    autoCollapseToc: true
---

### 修改全局名称及邮箱
当发现提交时的**用户名**不对时，用下面的指令修改  
```
git config --global user.name "prehisle"
git config --global user.email prehisle@gmail.com

```

### git commit message编写

```
<type>(<scope>): <subject>
// 空一行
<body>
// 空一行
<footer>
```

```
feat：新功能（feature）
fix：修补bug
docs：文档（documentation）
style： 格式（不影响代码运行的变动）
refactor：重构（即不是新增功能，也不是修改bug的代码变动）
test：增加测试
chore：构建过程或辅助工具的变动
```

参考：[Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)