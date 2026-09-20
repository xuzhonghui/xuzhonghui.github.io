---
layout: post
title: "python-版本特性-3.9-字典合并运算符"
date: 2026-09-17
categories: [技术, python, 版本特性]
tags: [GitHub Pages, Jekyll, Markdown, 博客]
---

> Python 3.9 引入 `dict | dict`，用于创建合并后的新字典

# 1、基本用法 `|`

```python
default_config = {"host": "localhost", "port": 8080, "debug": False}
user_config = {"port": 9000, "debug": True, "PhoneNumber": 10010}

config = default_config | user_config

print(default_config)   # 结果: {"host": "localhost", "port": 8080, "debug": False}
print(user_config)  # 结果: {"port": 9000, "debug": True, "PhoneNumber": 10010}
print(config)   # 结果: {'host': 'localhost', 'port': 9000, 'debug': True}
```

规则：

- 结果是一个新字典。
- 左右字典的所有键都会出现在结果中。
- 键重复时，右侧字典的值覆盖左侧。
- 两个原字典都不会被修改。

# 2、原地更新 `|=`

`|=` 会直接修改左侧字典, 等同于基本用法, 只是省了一个变量

```python
config = {"host": "localhost", "port": 8080}
config |= {"port": 9000, "debug": True}

print(config)   # 结果: {'host': 'localhost', 'port': 9000, 'debug': True}
```

# 3、多层合并 

运算顺序从左到右，越靠右优先级越高：

```python
defaults = {"name": "default"}
user_input1 = {"name": '小明', "email": "xiaoming@xxx.com"}
user_input2 = {"name": "小王", "age": 18}

result = defaults | user_input1 | user_input2
print(result)   # 结果: {'name': '小王', 'email': 'xiaoming@xxx.com', 'age': 18}
```

# 4、嵌套合并

只合并第一层键；嵌套字典不会递归合并

```python
base = {
    "database": {"host": "localhost", "port": 5432},
    "debug": False,
}
override = {
    "database": {"port": 5433},
}

merged = base | override
print(merged)   # {'database': {'port': 5433}, 'debug': False}

```
