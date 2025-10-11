---
title: "js备忘1"
date: 2020-10-25T18:20:10+08:00
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

#### JavaScript Array some，map 方法
some() 方法用于检测数组元素中是否有元素符合指定条件。 
map() 方法返回一个新数组，数组中的元素为原始数组元素调用函数处理后的值。  
```
color = {
  const scale = d3.scaleOrdinal(d3.schemeTableau10);
  if (data.some(d => d.category !== undefined)) { // 是否有某个元素定义了category
    const categoryByName = new Map(data.map(d => [d.name, d.category])) // 用map遍历构造健值对，用new Map构建映射表
    scale.domain(Array.from(categoryByName.values())); //values取Map对象的value迭代器，再用Array.from还原数组
    return d => scale(categoryByName.get(d.name)); // 通过d.name取颜色序号
  }
  return d => scale(d.name);
}
```
 