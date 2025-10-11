---
title: "Lua简单命令行框架"
date: 2020-04-02T13:30:04+08:00
tags: [
    "lua", "cli", "test"
]
categories: [
    "技术",
]
author: "prehisle"
toc: true
autoCollapseToc: true
---

### 源码`test_nmod.lua`

```lua
local module = {}

function module.main()
    print("module.main called")
end

function module.noparam()
    print("module.noparam called")
end

function module.oneparam(a)
    print("module.oneparams called " .. a)
end

function module.multiparams(a, b)
    print("module.multiparams called " .. a .." " ..b)
end



if pcall(getfenv, 4) then

else
    if #arg == 0 then
        print(module.main())
    elseif #arg == 1 then
        print(module[arg[1]]())
    else
        print(module[arg[1]](unpack(arg, 2)))
    end
end

return module
```

### 测试程序`test_nmod.lua`

```lua
local nmod = require("test.nmod")
nmod.oneparam("hello")
```

### 调用执行结果

```bash
root@OLYM-SW:/usr/lib/lua/test# lua test_nmod.lua 
module.oneparams called hello

root@OLYM-SW:/usr/lib/lua/test# lua nmod.lua 
module.main called

root@OLYM-SW:/usr/lib/lua/test# lua nmod.lua noparam
module.noparam called

root@OLYM-SW:/usr/lib/lua/test# lua nmod.lua oneparam a
module.oneparams called a

root@OLYM-SW:/usr/lib/lua/test# lua nmod.lua multiparams 1 2
module.multiparams called 1 2

```

