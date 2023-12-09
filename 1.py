#!/usr/bin/env python3
# -*- coding: utf-8 -*-

@tail_call_optimized
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)
    if __name__ == '__main__':
     print(fib(10000))
