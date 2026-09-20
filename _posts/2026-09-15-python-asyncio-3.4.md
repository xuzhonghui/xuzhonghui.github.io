---
layout: post
title: "python-版本特性-3.4-异步asyncio"
date: 2026-09-15
categories: [技术, python, 版本特性]
tags: [GitHub Pages, Jekyll, Markdown, 博客]
---

> asyncio 是 python 3.4 版本引入的标准库，主要为了支持异步编程

asyncio 能力全景

| 能力     | 关键API                                    | 用途                  |
|--------|------------------------------------------|---------------------|
| 运行异步程序 | asyncio.run()                            | 创建并运行事件循环，普通脚本的异步入口 |
| 定义协程   | async def、await                          | 编写可暂停、可恢复的异步函数      |
| 并发执行   | create_task()、gather()、TaskGroup         | 同时调度多个协程            |


## 运行一个最简单的异步程序: asyncio.run()
```python
import asyncio

async def debug_async():
    print('开始')
    await asyncio.sleep(1)
    print('结束')

asyncio.run(debug_async())
```

上述代码输出结果:

```
开始
结束
```

## 任务并发：gather() && create_task() && TaskGroup

### gather()

示例代码：

```python
import asyncio

async def debug_async():
    print('开始')
    await asyncio.sleep(1)
    print('结束')

async def main():
    await asyncio.gather(
        debug_async(),
        debug_async(),
        debug_async(),
    )

asyncio.run(main())
```

上述示例代码的输出结果：

```
开始
开始
开始
结束
结束
结束
```

### create_task()

示例代码:

```python
import asyncio

async def debug_async():
    print('开始')
    await asyncio.sleep(1)
    print('结束')

async def main():
    task1 = asyncio.create_task(debug_async())
    task2 = asyncio.create_task(debug_async())
    task3 = asyncio.create_task(debug_async())
    await task1
    await task2
    await task3

asyncio.run(main())
```

输出结果:

```commandline
开始
开始
开始
结束
结束
结束
```

### TaskGroup

示例代码：

```python
import asyncio

async def debug_async():
    print('开始')
    await asyncio.sleep(1)
    print('结束')

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(debug_async())
        task2 = tg.create_task(debug_async())
        task3 = tg.create_task(debug_async())

asyncio.run(main())
```

输出结果：

```commandline
开始
开始
开始
结束
结束
结束
```

### 三者之间的主要区别

create_task 其实就是一个单独的任务，所以，这里主要比较 gather 和 TaskGroup

|                   | gather                     | create_task        | TaskGroup                         |
|-------------------|----------------------------|--------------------|-----------------------------------|
| 最低版本              | 3.4                        | 3.7                | 3.11                              |
| 结果顺序              | 结果list（按传入顺序）              | Task               | 无序（用 task.result()自行管理）           |
| 异常处理              | 出错函数停止，其他函数正常运行            |                    | 出错时全部停止                           |
| 动态任务追加            | 不支持，一开始就需要定好               |                    | 运行中可以随时加 使用tg.create_task()       |
| 取消任务              | 支持，但是只能取消所有子任务，不能只取消其中的某一个 | 支持   task.cancel() | 支持，通过task引用来一个个取消/或者tg.cancel整体取消 |


