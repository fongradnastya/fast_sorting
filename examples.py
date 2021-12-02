"""Применяет функцию сортировки к объектам из exmpl"""
from sorting_package import sort_func
from random import randint


exmpl = (
        {"w", "o", "r", "l", "d"},
        ["1", "5", "0", "7", "3"],
        [1, 0.2, 3 / 5, 12.8, -10, -2],
        [randint(-100, 100) for _ in range(100)],
        [4, -10, 0, '1', 6, 1.8, 2, 9, -3, -1, 0, 4],
        (1, 2, 0)
        )


def check_on_examples():
    for ex in exmpl:
        sort_func.quick_sort(ex, reverse=True)
        sort_func.quick_sort(ex, reverse=False)


if __name__ == '__main__':
    check_on_examples()
