#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_subsets(n, current_set=None, index=1):
    """
    Рекурсивная функция для печати всех подмножеств множества {1,2,...n}.
    """
    if current_set is None:
        current_set = set()

    if index > n:
        print(current_set)
        return

    # Не включаем текущий элемент
    print_subsets(n, current_set, index + 1)

    # Включаем текущий элемент
    current_set.add(index)
    print_subsets(n, current_set, index + 1)
    current_set.remove(index)

if __name__ == "__main__":
    n = 3  # Замените значение n на необходимое
    print_subsets(n)