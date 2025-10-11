---
title: "d3,Observable备忘1"
date: 2020-10-17T15:24:45+08:00
tags: [
    "D3", "Observable"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

### 在Observable备忘引入附件图片并说明
```
md`<figure>
  <img src="${await FileAttachment("changing-stuff@1.jpg").url()}" style="width: 274px; height: 360px;">
  <figcaption>A legitimate learning strategy. Image: [DEV Community](https://twitter.com/thepracticaldev)</figcaption>
</figure>`
```


### 最最大值，中间值，最小值 
```
d3 = require("d3@6")
[d3.min(values), d3.median(values), d3.max(values)]
```

### 直接生成直方图
```
import {chart as chart1} with {values as data} from "@d3/histogram"
```

### 随便一个范围内的值
2000个mu值到上下2区间的值
```
values3 = Float64Array.from({length: 2000}, d3.randomNormal(mu, 2))
```

### 定义一个横坐标
-10, 10范围，定义起止坐标
```
x = d3.scaleLinear([-10, 10], [margin.left, width - margin.right])
```

### 加载附件中的数据
```
FileAttachment("temperature.csv")
```

### 解析附件csv为json对象
```
d3.csvParse(await FileAttachment("temperature.csv").text())
```

### 解析附件csv为json对象,并自动转换数据类型
```
d3.csvParse(await FileAttachment("temperature.csv").text(), d3.autoType)
```

### 反转字符串
```
[...name].reverse().join("")
```

### 定义一个经计算动态得出的变量
```
sum = {
  let s = 0;
  for (let i = 0; i < 10; ++i) {
    s += i;
  }
  return s;
}
```

### 解析csv,自定义字段解析函数
```
data = {
  const text = await FileAttachment("temperature.csv").text();
  const parseDate = d3.utcParse("%Y-%m-%d");    // 定义日期解析函数(格式化)
  return d3.csvParse(text, ({date, temperature}) => ({
    date: parseDate(date),
    temperature: +temperature   // 转换字符串为数值
  }));
}
```

### 取列表中的最小最大值 
```
d3.extent(data, d => d.date)
```

### 提取取列表对象中的某个字段值
```
temperatures = data.map(d => d.temperature)
```

### 一行生成直方图
```
import {chart as temperatureHistogram} with {temperatures as data, height} from "@d3/histogram"
```

### 定义比例尺
```
x = d3.scaleLinear()
    .domain([0, d3.max(fruits, d => d.count)]) // 数据范围
    .range([margin.left, width - margin.right]) // 像素坐标范围
    .interpolate(d3.interpolateRound)

y = d3.scaleBand()
    .domain(fruits.map(d => d.name))
    .range([margin.top, height - margin.bottom])
    .padding(0.1)       // 条形图间的空白间隔占比
    .round(true)
```