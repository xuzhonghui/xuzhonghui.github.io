---
layout: post
title: "python-版本特性-3.6-f-string"
date: 2026-09-16
categories: [技术, python, 版本特性]
tags: [GitHub Pages, Jekyll, Markdown, 博客]
---

> 格式化字符串, 适用版本：Python 3.6+。f"{value=}" 需要 Python 3.8+；Python 3.12 放宽了花括号内复杂表达式的限制

# 1、概念与基本语法：

在字符串前加 f 或 F，即可在花括号中嵌入变量或表达式， 例如：
```python
name = "user"
age = 20
print(f'姓名: {name}, 年龄: {age}')     # 结果: 姓名: user, 年龄: 20
```

支持单引号、双引号和三引号：
```python
name = "user"

# 下述结果输出都是: 姓名: user
print(f'姓名: {name}')     
print(f"姓名: {name}") 
print(f"""姓名: {name}""") 
```

# 2、格式化表达式

花括号中不仅可以放变量，也可以放表达式, 例如：
```python
price = 19.9
quantity = 3
items = ["苹果", "香蕉"]

print(f"总价：{price * quantity}")     # 总价：59.699999999999996
print(f"商品数：{len(items)}")      # 商品数：2
print(f"首项：{items[0]}")     # 首项：苹果
print(f"大写：{'python'.upper()}")     # 大写：PYTHON
print(f"状态：{'有货' if items else '缺货'}")      # 状态：有货
```

# 3、常用格式说明符:

| 目标 | 示例 | 结果 |
| --- | --- | --- |
| 两位小数 | `f"{3.14159:.2f}"` | `3.14` |
| 百分比 | `f"{0.256:.1%}"` | `25.6%` |
| 千分位 | `f"{1234567:,}"` | `1,234,567` |
| 科学计数法 | `f"{1234567:.2e}"` | `1.23e+06` |
| 二进制 | `f"{10:b}"` | `1010` |
| 八进制 | `f"{10:o}"` | `12` |
| 十六进制 | `f"{255:x}"` | `ff` |
| 大写十六进制 | `f"{255:X}"` | `FF` |
| 强制正负号 | `f"{42:+d}"` | `+42` |
| 补零编号 | `f"{42:06d}"` | `000042` |

```python
amount = 1_234_567.8
ratio = 0.1234
number = 42

print(f"金额：¥{amount:,.2f}")  # 金额：¥1,234,567.80
print(f"完成率：{ratio:.1%}")   # 完成率：12.3%
print(f"编号：{number:06d}")    # 编号：000042
```

# 4、宽度、对齐和动态


| 写法 | 含义 |
| --- | --- |
| `:<10` | 左对齐，宽度 10 |
| `:>10` | 右对齐，宽度 10 |
| `:^10` | 居中，宽度 10 |
| `:0>5` | 左侧以 `0` 填充到宽度 5 |

```python
products = [("键盘", 199.0, 3), ("显示器", 1299.0, 2)]

print(f"{'商品':<10}{'单价':>12}{'数量':>8}{'小计':>14}")
print("-" * 44)
for name, price, quantity in products:
    subtotal = price * quantity
    print(f"{name:<10}{price:>12.2f}{quantity:>8}{subtotal:>14.2f}")

# 输出结果:
# 商品                  单价      数量            小计
# --------------------------------------------
# 键盘              199.00       3        597.00
# 显示器            1299.00       2       2598.00
```

宽度和精度也可以由变量决定, 例如:

```python
number = 3.1415926
width = 10
precision = 3
print(f"[{number:{width}.{precision}f}]")  # 输出: [     3.142]
```

# 5、日期、转换与花括号嵌套

日期:
```python
from datetime import datetime

now = datetime.now()
print(f"当前时间：{now:%Y-%m-%d %H:%M:%S}")  # 当前时间：2026-09-16 16:02:15
```

转换方式:
- `!s` 调用 `str()`，通常是默认行为。
- `!r` 调用 `repr()`，适合排查换行、空格和转义字符。
- `!a` 调用 `ascii()`，会转义非 ASCII 字符。

```python
value = "hello\nworld"
name = "小明"
print(f"{value!r}")  # 'hello\nworld'
print(f"{name!a}")   # '\u5c0f\u660e'
```

花括号嵌套:
```python
name = "小明"
print(f"{{name}}")      # {name}
print(f"{{'name': '{name}'}}")  # {'name': '小明'}
```

# 6、表达式-3.8版本引入

```python
price = 19.9
quantity = 3
rate = 0.12345

print(f"{price=}, {quantity=}, {price * quantity=}")    # price=19.9, quantity=3, price * quantity=59.699999999999996
print(f"{rate=:.2%}")  # rate=12.35%
```