---
title: "js动态修改zIndex"
date: 2020-08-19T14:52:21+08:00
tags: [
    "js"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

```javascript
document.querySelectorAll('.bg-near-white').forEach(item=>{
	item.style.zIndex=-1;
});
```