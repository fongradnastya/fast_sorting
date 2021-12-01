"""Содержит функцию сортировки и 2 декоратора, применяемых к ней"""
import functools
import doctest
from random import randint


def trace(func):
    """
    Декоратор trace выводит в консоль информацию о поведении
    декорируемой функции
    """
    @functools.wraps(func)
    def inner(*args, dec=True, **kwargs):
        if not dec:
            func(*args, dec=dec, **kwargs)
            return None
        old_v = args[0].copy()
        func(args[0], **kwargs)
        keys = ""
        for key, value in kwargs.items():
            keys += f"{key}={value}\n"
        print(f"Функция {func.__name__} с параметрами:\n{old_v}\n{keys}"
              f"изменила исходный список на {args[0]}")
    return inner


def check_sort_ability(sort_func):
    """
     Декоратор check_sort_ability проверяет, соответствуют ли переданные в
     функцию параметры необходимым для корректной сортировки условиям
    """
    @functools.wraps(sort_func)
    def inner(*args, dec=True, **kwargs):
        if not dec:
            sort_func(*args, dec=dec, **kwargs)
            return None
        try:
            if type(args[0]) is not list:
                raise TypeError("Неподходящий для сортировки тип объекта",
                                args[0], type(args[0]))
        except TypeError as ex:
            print(*ex.args)
            return None
        else:
            try:
                sort_func(*args, **kwargs)
            except IndexError as ex:
                print("Параметры begin и end должны быть значениями индексов "
                      "в пределах списка", ex)
            except TypeError as ex:
                print(f"Сортировка невозможна, список {args[0]} содержит "
                      f"элементы разных типов.", ex)
    return inner


@check_sort_ability
@trace
def quick_sort(sort_lst: list, *, dec=True, begin=0, end=-1, reverse=False):
    """
    Функция quick_sort реализует сортировку Хоара
    :param sort_lst: список для сортировки
    :param dec: значение True включает обработку исключений и вывод
    результата, False выключает
    :param begin: позиция первого сортируемого элемента
    :param end: позиция последнего сортируемого элемента
    :param reverse: False - сортировка по неубываню, True - по невозрастанию
    :return: ничего не возвращается, так как изменяется переданный объёкт
    >>> new_lst = [3, 0, 7]
    >>> quick_sort(new_lst)
    Функция quick_sort с параметрами:
    [3, 0, 7]
    изменила исходный список на [0, 3, 7]
    >>> new_lst = [3, 0, 7, 4]
    >>> quick_sort(new_lst, reverse=True)
    Функция quick_sort с параметрами:
    [3, 0, 7, 4]
    reverse=True
    изменила исходный список на [7, 4, 3, 0]
    """
    if len(sort_lst) < 2:
        return None
    if begin < end or end == -1:
        left = begin
        if end == -1:
            end = len(sort_lst) - 1
        right = end
        start = sort_lst[randint(left, right)]
        while left <= right:
            while (sort_lst[left] > start) == reverse \
                    and sort_lst[left] != start:
                left += 1
            while (sort_lst[right] < start) == reverse \
                    and sort_lst[right] != start:
                right -= 1
            if left <= right:
                sort_lst[left], sort_lst[right] = \
                    sort_lst[right], sort_lst[left]
                left += 1
                right -= 1

        quick_sort(sort_lst, dec=False, begin=begin, end=right,
                   reverse=reverse)
        quick_sort(sort_lst, dec=False, begin=left, end=end, reverse=reverse)
    else:
        return None


if __name__ == "__main__":
    doctest.testmod()
