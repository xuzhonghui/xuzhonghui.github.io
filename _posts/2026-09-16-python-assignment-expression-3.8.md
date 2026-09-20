---
layout: post
title: "python-版本特性-3.8-海象运算符"
date: 22026-09-16 14:00:00 +0800
categories: [技术, python, 版本特性]
tags: [GitHub Pages, Jekyll, Markdown, 博客]
---

> 海象运算符由 Python 3.8 引入。它允许在“需要表达式的位置”完成赋值，因此常用于避免重复计算、重复读取或重复匹配。它的目标是提高局部代码的清晰度，而不是把代码压缩得越短越好

## 1、基本概念

普通赋值语句使用`=`, 不能作为表达式的一部分, 比如:

```python
name = "小明"
```

海象运算符 `:=` 会“赋值，同时产生该值”：

```python
if name := input("请输入名字："):
    print(f"你好，{name}")
```

其形状像海象的眼睛和长牙，因此得名“海象运算符” , 其基本形式：

```
变量 := 表达式
```

但是需要注意: 它只允许给简单名称赋值，不能给属性、下标或解包目标赋值, 例如：

```python
# 合法
if total := calculate_total():
    print(total)

# 不合法
# obj.value := 10
# items[0] := 10
# a, b := get_pair()
```

## 2、为什么需要它

> 海象运算符最常见的价值是：一个值既用于判断，又要在判断成功后继续使用。

传统写法:
```python
text = input("请输入内容：")
if text:
    print(f"长度：{len(text)}")
```

使用海象运算符:
```python
if text := input("请输入内容："):
    print(f"长度：{len(text)}")
```

两种写法功能相同。后者把“读取”和“判断”放在一起，适合变量只在当前分支中使用的情况

## 3、使用场景

### 3.1 `if` 中缓存计算结果

```python
text = 'abc'

if result := 'abc' in text:
    print(result)
```

### 3.2 `while` 中持续读取，直到没有数据

```python
while line := file.readline():
    print(line.rstrip())
```

### 3.3 列表推导式中避免重复计算

```python
texts = ["  Python  ", "", "  asyncio", "   "]

cleaned = [value for text in texts if (value := text.strip())]
print(cleaned)  # ['Python', 'asyncio']
```

### 3.4 条件判断中保存易变结果

```python
if (count := get_unread_message_count()) > 0:
    print(f"你有 {count} 条未读消息")
```

