+++
date = '2025-11-19T11:24:12+08:00'
draft = false
title = '【排查实录】Curl 通但 Node 不通？一次 macOS、旁路由与 EHOSTUNREACH 的填坑记'
+++

## 背景
最近在使用 `claude code` (Anthropic 官方命令行工具) 连接局域网内的自建 API 网关时，遇到了一个极其诡异的网络问题。

**环境坐标：**
*   **OS**: macOS Sequoia (Mac Mini)
*   **Shell**: Tmux + Zsh
*   **网络拓扑**: 典型的**旁路由**架构
    *   主路由: `192.168.1.1`
    *   旁路由 (网关): `192.168.1.9` (负责科学上网等)
    *   本机 IP: `192.168.1.8`
    *   目标 API 服务器: `192.168.1.31`

## 诡异的现象
在 Tmux 中运行 `claude`，报错连接失败。为了排查，我写了一个最简单的 Node.js 测试脚本 (`http.get`)，结果报出 `EHOSTUNREACH`。

最“闹鬼”的地方在于，**终端下的基础工具全是通的**：
1.  `ping 192.168.1.31` -> **通** (0.x ms)
2.  `curl http://192.168.1.31:9200` -> **通** (能收到响应)
3.  `node test_net.js` -> **报错**：
    ```
    Error: connect EHOSTUNREACH 192.168.1.31:9200 - Local (192.168.1.8:xxxx)
    ```

**核心疑问**：为什么 `curl` 和 `ping` 都能找到路，唯独基于 Node.js 的程序像是瞎了一样，找不到同一个网段的目标主机？

## 排查弯路 (Winding Roads)

在定位到真凶之前，我尝试了以下常规手段，均告失败：

1.  **怀疑代理 (Proxy)**：
    *   以为是 `http_proxy` 环境变量导致流量走了梯子。
    *   **操作**：设置 `NO_PROXY`，甚至 `unset` 所有代理变量。
    *   **结果**：无效。

2.  **怀疑 V2Ray/Clash 残留**：
    *   macOS 上即便关掉代理软件，`utun` 虚拟网卡和防火墙规则 (`pf`) 可能残留。
    *   **操作**：杀进程、`sudo route flush`、`sudo pfctl -F all`。
    *   **结果**：无效。

3.  **怀疑 IPv6**：
    *   Node.js 倾向于优先走 IPv6，导致被错误的路由引导。
    *   **操作**：`export NODE_OPTIONS="--dns-result-order=ipv4first"`。
    *   **结果**：无效。

## 真相大白：路由“黑洞”与 Node 的倔强

通过 `netstat -nr` 仔细观察路由表，发现了问题的端倪。

### 1. 错误的本地路由
当你试图用 `route add -host ... -interface en0` 强制指定接口时，如果此时 ARP 表没有正确绑定，macOS 可能会建立一条错误的路由：
```bash
192.168.1.31    d0:11:e5:xx:xx:xx    UHLS    en0
```
这里的 MAC 地址竟然是 **Mac Mini 自己的 MAC**！
这就导致 Node.js 发出的包，转了一圈发给了自己。网卡收到包一看目标 IP 不是自己，直接丢弃。

### 2. Curl 为什么能通？
`curl` 使用的是 macOS 系统级网络框架（CFNetwork/libcurl），它非常智能（或者说“鸡贼”）。当它发现路由表有点不对劲但目标在同网段时，它会**主动发起 ARP 广播**去寻找真实地址，绕过了内核路由表的“坑”。

而 **Node.js (libuv)** 非常老实，严格遵守路由表。路由表指向了错误的 MAC 或指向了旁路由（而旁路由可能因为配置问题拒绝了内网回环流量），Node 就直接抛出 `EHOSTUNREACH`。

### 3. 旁路由的锅
我的默认网关是 `192.168.1.9` (旁路由)。在处理 Lan-to-Lan 流量时，旁路由规则复杂，导致 Node 认为去往 `.31` 的路不通。

## 终极解决方案：借道主路由 (Hairpin Routing)

既然直连路由容易受本地 ARP 缓存和旁路由干扰，最稳妥的办法是：**强制把流量扔给主路由器，让主路由去转发。**

主路由 (`192.168.1.1`) 拥有最权威的 ARP 表，且不会像旁路由那样拦截流量。

### 操作步骤

**Step 1: 清理旧的错误路由**
```bash
sudo route delete 192.168.1.31
# 多执行几次，直到提示 "not in table"
```

**Step 2: 添加下一跳为主路由的静态路由**
```bash
# 语法: route add -host [目标IP] [主路由IP]
sudo route add -host 192.168.1.31 192.168.1.1
```
这条命令的含义是：“Mac 你别自己瞎找了，所有去往 `.31` 的包，直接丢给 `.1` (主路由)，让它看着办。”

**Step 3: 验证**
再次运行 Node 脚本，瞬间跑通，返回 `401 Unauthorized`（这是成功的标志，说明连上了）。

## 备忘总结 (TL;DR)

如果在 macOS + Tmux + Node.js 环境下遇到 **Curl 通但 Node 不通**，且目标在局域网内：

1.  **现象**：错误代码 `EHOSTUNREACH` 或 `EAFNOSUPPORT`。
2.  **检查**：`netstat -nr | grep 目标IP`，看 Gateway 是否异常（指向了自己或 link#7）。
3.  **秒杀公式**：不要折腾代理和 ARP，直接**指定下一跳为主路由**。
    ```bash
    sudo route delete <目标IP>
    sudo route add -host <目标IP> <主路由网关IP>
    ```

这也再次印证了网络工程里的一句老话：**静态路由是解决“脑裂”最不讲道理但最有效的手段。**