#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache
import timeit


def factorial_rec(n):
    """
    Функция, вычисляющая факториал рекурсивно
    """
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


def fib_rec(n):
    """
    Функция, вычисляющая число фибонначи рекурсивно
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 2) + fib_rec(n - 1)


@lru_cache
def factorial_rec_lru(n):
    """
    Функция, вычисляющая факториал рекурсивно

    Оптимитизирована с использованием lru_cache
    """
    if n == 0:
        return 1
    else:
        return n * factorial_rec_lru(n - 1)


@lru_cache
def fib_rec_lru(n):
    """
    Функция, вычисляющая число фибонначи рекурсивно

    Оптимитизирована с использованием lru_cache
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec_lru(n - 2) + fib_rec_lru(n - 1)


def factorial_iter(n):
    """
    Функция, вычисляющая факториал итеративно
    """
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib_iter(n):
    """
    Функция, вычисляющая число фибонначи итеративно
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    dpi = 100
    width_inches = (1680 / dpi) / 4
    height_inches = (850 / dpi) / 2
    size = (width_inches, height_inches)
    functions = {
        factorial_rec: "Факториал рекурсивный",
        factorial_rec_lru: "Факториал рекурсивный с @lru_cache",
        factorial_iter: "Факториал итеративный",
        fib_rec: "Fibonacci рекурсивный",
        fib_rec_lru: "Fibonacci рекурсивный c @lru_cache",
        fib_iter: "Fibonacci итеративный"
    }

    n = int(input("Введите число для вычислений: "))

    for func, desc in functions.items():
        start_time = timeit.default_timer()
        result = func(n)
        elapsed_time = timeit.default_timer() - start_time
        print(f"{desc}: {result}, Время выполнения: {elapsed_time:.6f} секунд")
    