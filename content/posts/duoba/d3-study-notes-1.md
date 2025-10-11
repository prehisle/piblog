---
title: "d3学习笔记"
date: 2020-09-09T09:46:09+08:00
tags: [
    "d3"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---



### Let’s Make a Bar Chart

* Part 1

  * Chaining Methods

  * d3.scaleLinear

  * canvas or SVG中，y坐标是向下的

  * ```
    y = d3.scaleLinear()
        .domain(d3.extent(data, d => d.value)).nice()
        .range([height - margin.bottom, margin.top])
    ```

    nice()做最小最大边界取整的数

  * Piecewise scales 分段比例尺

  * `d3.ticks(-1, 1, 10)`

    ```
    Array(11) [
      0: -1
      1: -0.8
      2: -0.6
      3: -0.4
      4: -0.2
      5: 0
      6: 0.2
      7: 0.4
      8: 0.6
      9: 0.8
      10: 1
    ]
    ```

    

* Part 2

  * text-anchor="end" 文本最后一个字符对应当前文件一初始位置
  * text中的y属性表示文本的baseline,即底部位置
  * domain数据值 range屏幕像素坐标值 

* Part 3

* Part 4

  ```
  yAxis = g => g
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y).ticks(null, "%"))
      .call(g => g.select(".domain").remove()) // 删除y轴线，如下图1
  xAxis = g => g
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x).tickSizeOuter(0)) // 删除x轴外线，如下图2
  ```

  ![image-20200910163121606](http://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCEd3e1ae5434d540fd98a1131ec24fe521/129)

### learn-d3

* ```
  viewof mu = Scrubber(d3.ticks(-5, 5, 200), {
    format: x => `mu = ${d3.format("+.2f")(x)}`,
    autoplay: true, // 自动播放
    alternate: true // 来回重放
  })
  ```

  ![image-20200910175855051](http://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCEd99280a5033947559d2a5da8e4ea3946/130)

* 引入外部模块

  ```
  import {chart as chart3, margin, width} with {x, values3 as data, height} from "@d3/histogram"
  ```

* 取最大最小值

  ```
  d3.extent(data, d => d.date)
  ```

* 局部代码块

  ```
  sum = {
    let s = 0;
    for (let i = 0; i < 10; ++i) {
      s += i;
    }
    return s;
  } // 外部大括号可看成一个立即执行的代码块，返回执行后的结果
  ```

* stoke-dasharray和stroke-dashoffset

  ![image-20200911121638767](http://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCE80f72e34e05741f0bd39420b578f3405/131)

  * stroke-dashoffset="3"，偏移正数，虚线整体左移

  * stroke-dashoffset="-3"，偏移负数，虚线整体右移

* d3-ease，淡入淡出

* Object.assign方法用于对象的合并，将源对象（source）的所有可枚举属性，复制到目标对象（target）。

* d3.rollup(athletes, v => v.length, d => d.sport) // 分组，后放到数组里作为v, 返回每组和第二个参数的返回值， 参考https://observablehq.com/@d3/d3-group

* flatMap()方法对原数组的每个成员执行一个函数，相当于执行Array.prototype.map(),然后对返回值组成的数组执行flat()方法。该方法返回一个新数组，不改变原数组。

  ```
  // 相当于 [[2, 4], [3, 6], [4, 8]].flat()
  [2, 3, 4].flatMap((x) => [x, x * 2])
  // [2, 4, 3, 6, 4, 8]
  123
  ```

  flatMap()只能展开一层数组。

* d3.pairs

  ```
  prices = [100, 110, 112, 115, 123, 122, 127]
  changes = d3.pairs(prices, (a, b) => (b - a) / a)
  ==
  changes = Array(6) [0.1, 0.01818181818181818, 0.026785714285714284, 0.06956521739130435, -0.008130081300813009, 0.040983606557377046]
  Or, as percentages: +10.0%, +1.8%, +2.7%, +7.0%, -0.8%, +4.1%.
  ```

  

* https://observablehq.com/@d3/easing
* https://www.tutorialsteacher.com/d3js/animation-with-d3js
* https://github.com/d3/d3/wiki/Tutorials