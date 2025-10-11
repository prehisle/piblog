---
title: "d3,Observable备忘3"
date: 2020-10-24T10:31:38+08:00
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

## 动画
与在纸上绘制的图形不同，计算机图形不必是静态的。就像科学怪人的怪物一样，它们可以通过动画来栩栩如生！ ✨
### 生成一个控制按钮
```
viewof replay = html`<button>Replay`
```
![](http://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCEa86462d7035f4634acd56be0413fa192/134)

### 逐步画完的拆线图
```
replay, html`<svg viewBox="0 0 ${width} ${height}">
  ${d3.select(svg`<path d="${line(data)}" fill="none" stroke="steelblue" stroke-width="1.5" stroke-miterlimit="1" stroke-dasharray="0,1"></path>`).call(reveal).node()}  // reveal函数控制动画过程
  ${d3.select(svg`<g>`).call(xAxis).node()}
  ${d3.select(svg`<g>`).call(yAxis).node()}
</svg>`
```
```
reveal = path => path.transition()
    .duration(5000)
    .ease(d3.easeLinear)
    .attrTween("stroke-dasharray", function() {
      const length = this.getTotalLength();
      return d3.interpolate(`0,${length}`, `${length},${length}`); // 代表隐藏部分的起止
    })
```

### 手动控制逐步画完的拆线图
* 可手动调整的范围输入框
```
viewof t = Scrubber(d3.ticks(0, 1, 100), { // 0->1,分成100份
  autoplay: false,
  loop: false,
  initial: 50, // 初始值为50
  format: x => `t = ${x.toFixed(3)}` // 标签格式化为3位小数
})
```
* 配合的画图代码
```
html`<svg viewBox="0 0 ${width} ${height}">
  <path d="${line(data)}" fill="none" stroke="steelblue" stroke-width="1.5" stroke-miterlimit="1" stroke-dasharray="${lineLength * t},${lineLength}"></path>
  ${d3.select(svg`<g>`).call(xAxis).node()}
  ${d3.select(svg`<g>`).call(yAxis).node()}
</svg>`
```
    * 估计stroke-dasharray代表为曲线忽略的部分
    
### 三种制作动画的方法
1. 使用D3’s transitions
2. 使用时间t,当t改变时整个图重绘，这种方法效率低，但更易于缩写
3. 使用循环yield，每秒生成60次
```
{
  replay2;

  const path = svg`<path d="${line(data)}" fill="none" stroke="steelblue" stroke-width="1.5" stroke-miterlimit="1">`;

  const chart = html`<svg viewBox="0 0 ${width} ${height}">
    ${path}
    ${d3.select(svg`<g>`).call(xAxis).node()}
    ${d3.select(svg`<g>`).call(yAxis).node()}
  </svg>`;

  for (let i = 0, n = 300; i < n; ++i) {
    const t = (i + 1) / n; // 0到1的t值，动画持续时间=300/60,即每秒60帧
    path.setAttribute("stroke-dasharray", `${t * lineLength},${lineLength}`);
    yield chart;
  }
}
```

### 综合示例
```
chart = {
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, height]);

  const zx = x.copy(); // x, but with a new domain.

  const line = d3.line()
      .x(d => zx(d.date))
      .y(d => y(d.close));

  const path = svg.append("path")
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("stroke-miterlimit", 1)
      .attr("d", line(data));

  const gx = svg.append("g")
      .call(xAxis, zx);

  const gy = svg.append("g")
      .call(yAxis, y);

  return Object.assign(svg.node(), { // 将update置入到svg.node()中，以便可以用chart.update来调用
    update(domain) {
      const t = svg.transition().duration(750);
      zx.domain(domain);
      gx.transition(t).call(xAxis, zx);
      path.transition(t).attr("d", line(data));
    }
  });
}
```

## Joins
### 用svg展示一组字符
1. 使用代码
```
chart1 = {
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, 33])
      .attr("font-family", "sans-serif")
      .attr("font-size", 10)
      .style("display", "block");

  svg.selectAll("text")
    .data(alphabet)
    .join("text")
      .attr("x", (d, i) => i * 17)
      .attr("y", 17)
      .attr("dy", "0.35em")
      .text(d => d);

  return svg.node();
}
```
2. 使用html标签
```
html`<svg viewBox="0 0 ${width} 33" font-family="sans-serif" font-size="10" style="display: block;">
  ${alphabet.map((d, i) => svg`<text x="${i * 17}" y="17" dy="0.35em">${d}</text>`)}
</svg>`
```
以上两种方法结果相同

### 延迟执行+数组乱序
```
randomLetters = {
  while (true) {
    yield d3.shuffle(alphabet.slice())
      .slice(Math.floor(Math.random() * 10) + 5)
      .sort(d3.ascending);
    await Promises.delay(1000);
  }
}
```

### join实例: 随机字母数组数据展示
```
chart2 = {
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, 33])
      .attr("font-family", "sans-serif")
      .attr("font-size", 10)
      .style("display", "block");

  let text = svg.selectAll("text");

  return Object.assign(svg.node(), {
    update(letters) {   // 将update方法置入svg.node()，也就是置入chart2
      text = text
        .data(letters)
        .join("text")
          .attr("x", (d, i) => i * 17)
          .attr("y", 17)
          .attr("dy", "0.35em")
          .text(d => d);
    }
  });
}
```
```
chart2.update(randomLetters)
```

### 关于SVG之ViewBox，translate
* ViewBox定义为svg有效可视作图区域左上角及右下角的坐标
* ViewBox内部坐标单位为svg width,height与ViewBox尺寸的比例
* translate中的坐标是在ViewBox坐标第中的偏移

### join(enter, update, exit)
```
chart3 = {
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, 33])
      .attr("font-family", "sans-serif")
      .attr("font-size", 10)
      .style("display", "block");

  let text = svg.selectAll("text");

  return Object.assign(svg.node(), {
    update(letters) {
      text = text
        .data(letters, d => d)
        .join(
          enter => enter.append("text") // enter是新加入的元素
            .attr("y", 17)
            .attr("dy", "0.35em")
            .text(d => d),
          update => update, // update为可能需要更新的元素
          exit => exit.remove() // exit为需移除的元素
        )
          .attr("x", (d, i) => i * 17);
    }
  });
}
```
以下为上例加入动画
```
chart4 = {
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, 33])
      .attr("font-family", "sans-serif")
      .attr("font-size", 10)
      .style("display", "block");

  let text = svg.selectAll("text");

  return Object.assign(svg.node(), {
    update(letters) {
      const t = svg.transition().duration(750);

      text = text
        .data(letters, d => d)
        .join(
          enter => enter.append("text")
            .attr("y", -7)
            .attr("dy", "0.35em")
            .attr("x", (d, i) => i * 17)
            .text(d => d),
          update => update,
          exit => exit
            .call(text => text.transition(t).remove()
              .attr("y", 100))
        )
          .call(text => text.transition(t)
            .attr("y", 17)
            .attr("x", (d, i) => i * 17));
    }
  });
}
```

### 一个列表选择框实例
```
viewof agedata = {
  const form = html`<form style="display: flex; align-items: center; min-height: 33px; font: 12px var(--sans-serif);"><select name=i>${data.ages.map(age => Object.assign(html`<option>`, {textContent: age}))}</select><div style="margin-left: 0.5em;">Age group</div>`;
  form.i.onchange = () => form.dispatchEvent(new CustomEvent("input"));
  form.oninput = () => {
    form.value = data // 选择好后顺带把数据处理好
      .filter(d => d.age === form.i.value)
      .sort((a, b) => d3.descending(a.value, b.value));
  };
  form.oninput();
  return form;
}
```

## Interaction，交互
### 悬停提示
```
html`<svg viewBox="0 0 ${width} ${height}">
  <path d="${line(data)}" fill="none" stroke="steelblue" stroke-width="1.5" stroke-miterlimit="1"></path>
  <g fill="none" pointer-events="all">
    ${d3.pairs(data, (d, b) => svg`<rect x="${x(d.date)}" height="${height}" width="${x(b.date) - x(d.date)}">
      <title>${formatDate(d.date)}
${formatClose(d.close)}</title>
    </rect>`)}
  </g>
  ${d3.select(svg`<g>`).call(xAxis).node()}
  ${d3.select(svg`<g>`).call(yAxis).node()}
</svg>`
```
### 线上实心圆提示
![](http://note.youdao.com/yws/public/resource/40e7acccfd342428f39d3dc7cca9ce31/xmlnote/WEBRESOURCE2e1a04a891d249f1b8bd2d6412c4c8f1/135)
```
{
  const tooltip = new Tooltip();
  return html`<svg viewBox="0 0 ${width} ${height}">
  <path d="${line(data)}" fill="none" stroke="steelblue" stroke-width="1.5" stroke-miterlimit="1"></path>
  ${d3.select(svg`<g>`).call(xAxis).node()}
  ${d3.select(svg`<g>`).call(yAxis).node()}
  <g fill="none" pointer-events="all">
    ${d3.pairs(data, (a, b) => Object.assign(svg`<rect x="${x(a.date)}" height="${height}" width="${x(b.date) - x(a.date)}"></rect>`, {
    onmouseover: () => tooltip.show(a),
    onmouseout: () => tooltip.hide()
  }))}
  </g>
  ${tooltip.node}
</svg>`;
}
```

### 自定义tooltip
```
class Tooltip {
  constructor() {
    this._date = svg`<text y="-22"></text>`;
    this._close = svg`<text y="-12"></text>`;
    this.node = svg`<g pointer-events="none" display="none" font-family="sans-serif" font-size="10" text-anchor="middle">
  <rect x="-27" width="54" y="-30" height="20" fill="white"></rect>
  ${this._date}
  ${this._close}
  <circle r="2.5"></circle>
</g>`;
  }
  show(d) {
    this.node.removeAttribute("display");
    this.node.setAttribute("transform", `translate(${x(d.date)},${y(d.close)})`);
    this._date.textContent = formatDate(d.date);
    this._close.textContent = formatClose(d.close);
  }
  hide() {
    this.node.setAttribute("display", "none");
  }
}
```
使用
```
{
  const tooltip = new Tooltip();

  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, height]);

  svg.append("path")
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("stroke-miterlimit", 1)
      .attr("d", line(data));

  svg.append("g")
      .call(xAxis);

  svg.append("g")
      .call(yAxis);

  svg.append("g")
      .attr("fill", "none")
      .attr("pointer-events", "all")
    .selectAll("rect")
    .data(d3.pairs(data))
    .join("rect")
      .attr("x", ([a, b]) => x(a.date))
      .attr("height", height)
      .attr("width", ([a, b]) => x(b.date) - x(a.date))
      .on("mouseover", (event, [a]) => tooltip.show(a))
      .on("mouseout", () => tooltip.hide());

  svg.append(() => tooltip.node);

  return svg.node();
}
```

### 提升效率，用mousemove坐标计算提示信息
```
{
  const tooltip = new Tooltip();
  return Object.assign(html`<svg viewBox="0 0 ${width} ${height}">
  <path d="${line(data)}" fill="none" stroke="steelblue" stroke-width="1.5" stroke-miterlimit="1"></path>
  ${d3.select(svg`<g>`).call(xAxis).node()}
  ${d3.select(svg`<g>`).call(yAxis).node()}
  ${tooltip.node}
</svg>`, {
    onmousemove: event => tooltip.show(bisect(data, x.invert(event.offsetX))),   // x.invert
    onmouseleave: () => tooltip.hide()
  });
}
```
```
bisect = {
  const bisectDate = d3.bisector(d => d.date).left;
  return (data, date) => {  // 找出距离最近的数据
    const i = bisectDate(data, date, 1);
    const a = data[i - 1], b = data[i];
    return date - a.date > b.date - date ? b : a;
  };
}
```

### 交互用范围选择框、文本输入框、下拉列表框
```
viewof number = html`<input type="range" min="0" max="100" step="1">`
```
```
viewof name = html`<input type="text" placeholder="Type a name!">`
```
```
viewof fruit = html`<select>
  <option value="apple">Apple</option>
  <option value="orange" selected>Orange</option>
  <option value="banana">Banana</option>
</select>`
```

### 图表触发input事件,作为其他cell的输入
```
viewof hover = {
  return Object.assign(html`<svg viewBox="0 0 ${width} ${height}">
  <path d="${line(data)}" fill="none" stroke="steelblue" stroke-width="1.5" stroke-miterlimit="1"></path>
  ${d3.select(svg`<g>`).call(xAxis).node()}
  ${d3.select(svg`<g>`).call(yAxis).node()}
</svg>`, {
    value: null,
    onmousemove: event => {
      event.currentTarget.value = bisect(data, x.invert(event.offsetX));
      event.currentTarget.dispatchEvent(new CustomEvent("input"));
    }, 
    onmouseleave: event => {
      event.currentTarget.value = null;
      event.currentTarget.dispatchEvent(new CustomEvent("input"));
    }
  });
}
```

### d3.group, d3.rollup
* 有数组
``` js
athletes = [
  {name: "Floyd Mayweather", sport: "Boxing", nation: "United States", earnings: 285},
  {name: "Lionel Messi", sport: "Soccer", nation: "Argentina", earnings: 111},
  {name: "Cristiano Ronaldo", sport: "Soccer", nation: "Portugal", earnings: 108},
  {name: "Conor McGregor", sport: "MMA", nation: "Ireland", earnings: 99},
  {name: "Neymar", sport: "Soccer", nation: "Brazil", earnings: 90},
  {name: "LeBron James", sport: "Basketball", nation: "United States",  earnings: 85.5},
  {name: "Roger Federer", sport: "Tennis", nation: "Switzerland", earnings: 77.2},
  {name: "Stephen Curry", sport: "Basketball", nation: "United States", earnings: 76.9},
  {name: "Matt Ryan", sport: "Football", nation: "United States", earnings: 67.3},
  {name: "Matthew Stafford", sport: "Football", nation: "United States", earnings: 59.5}
]
```
#### d3.group单分组
```
athletesBySport = d3.group(athletes, d => d.sport)
```
* 得到一个Map,以sport为key,value为所有属于key的元素列表，如
```
athletesBySport = Map(6) {
  "Boxing" => Array(1) [
  0: Object {name: "Floyd Mayweather", sport: "Boxing", nation: "United States", earnings: 285}
]
  "Soccer" => Array(3) [
  0: Object {name: "Lionel Messi", sport: "Soccer", nation: "Argentina", earnings: 111}
  1: Object {name: "Cristiano Ronaldo", sport: "Soccer", nation: "Portugal", earnings: 108}
  2: Object {name: "Neymar", sport: "Soccer", nation: "Brazil", earnings: 90}
]
  "MMA" => Array(1) [Object]
  "Basketball" => Array(2) [Object, Object]
  "Tennis" => Array(1) [Object]
  "Football" => Array(2) [Object, Object]
  <prototype>: Map {Symbol(Symbol.toStringTag): "Map", Symbol(Symbol.iterator): ƒ()}
}
```
#### d3.group多分组
```
athletesByNationSport = d3.group(athletes, d => d.nation, d => d.sport)
```
* 得到一个Map,以第一个分组为key,value为以第二个分组为key,value为所有属于第二个分组key的元素列表，如
```
athletesByNationSport = Map(6) {
  "United States" => Map(3) {
  "Boxing" => Array(1) [Object]
  "Basketball" => Array(2) [
  0: Object {name: "LeBron James", sport: "Basketball", nation: "United States", earnings: 85.5}
  1: Object {name: "Stephen Curry", sport: "Basketball", nation: "United States", earnings: 76.9}
]
  "Football" => Array(2) [Object, Object]
  <prototype>: Map {Symbol(Symbol.toStringTag): "Map", Symbol(Symbol.iterator): ƒ()}
}
  "Argentina" => Map(1) {"Soccer" => Array(1)}
  "Portugal" => Map(1) {"Soccer" => Array(1)}
  "Ireland" => Map(1) {"MMA" => Array(1)}
  "Brazil" => Map(1) {"Soccer" => Array(1)}
  "Switzerland" => Map(1) {"Tennis" => Array(1)}
  <prototype>: Map {Symbol(Symbol.toStringTag): "Map", Symbol(Symbol.iterator): ƒ()}
}
```

#### d3.rollup用于计算分组的汇总值
* 计算每个分组的元素数量
```
d3.rollup(athletes, v => v.length, d => d.sport)
```
* 计算每个分组元素的某个属性和
```
d3.rollup(athletes, v => d3.sum(v, d => d.earnings), d => d.sport)
```
#### 备忘点
* 若要使用嵌套的array替代map,使用use d3.groups

### d3.least, d3.greatest [参考文档](https://observablehq.com/@d3/d3-least)
有数据
```
friends = [
  {name: "BORIS", age: 15},
  {name: "bastien", age: 2},
  {name: "carmen D.", age: 18},
  {name: "DIVINE", age: 35}
]
```
* 使用比较器comparator
```
d3.least(friends, (a, b) => d3.ascending(a.age, b.age))
```
* 使用访问器accessor
```
d3.least(friends, d => d.age)
```
* Map作为迭代参数时,访问器的参数为[key,val]形式的数组，这里用到解构
```
d3.least(d3.rollup(athletes, v => d3.sum(v, d => d.earnings), d => d.sport), ([, sum]) => -sum) // 取返以获得最大值
```
### 参考
* [Inputs大全](https://observablehq.com/@jashkenas/inputs)
* [Scrubber大全](https://observablehq.com/@mbostock/scrubber)
* [brushing](https://github.com/d3/d3-brush), [zooming](https://github.com/d3/d3-zoom), and [dragging](https://github.com/d3/d3-drag). (For self-directed study, find examples in the [D3 gallery](https://observablehq.com/@d3/gallery) and [collections](https://observablehq.com/@d3?tab=collections).)
* 数据转换See [d3-array](https://observablehq.com/collection/@d3/d3-array)’s methods for transforming and aggregating data, including [basic summary statistics](https://observablehq.com/@d3/d3-mean-d3-median-and-friends) and the powerful [d3.group and d3.rollup](https://observablehq.com/@d3/d3-group).
* [后面的主题Further Topics](https://observablehq.com/@d3/learn-d3-further-topics?collection=@d3/learn-d3) 