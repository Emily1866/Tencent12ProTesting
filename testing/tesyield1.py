#!/usr/bin/env python
# -*- coding: utf-8 -*-
def provider():
    for i in range(5):
        yield i # 生成器 : return i

p = provider()
print(next(p))
print(next(p))
print(next(p))