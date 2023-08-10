#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(x, y):
    return x + y


def mul(x, y):
    """take X and Y, return X * Y"""
    return x * y


def square_sum(x, y):
    return mul(x, x) + mul(y, y)


def operate(x, y, f):
    return f(x, y)


def operate_n(x, y, f, n):
    res = f(x, y)
    i = 1
    while i <= n:
        res = f(res, f(x, y))
    return res


if __name__ == "__main__":
    res = operate(3, 5, square_sum)
    res1 = operate_n(3, 6, mul, 8)
    print(res)
    print(res1)
