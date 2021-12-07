"""Содержит функции для обработки пользовательского ввода и команд"""
import re
from random import randint
from .sort_func import quick_sort


examples = (
        {"w", "o", "r", "l", "d"},
        ["1", "5", "0", "7", "3"],
        [1, 0.2, 3 / 5, 12.8, -10, -2],
        [randint(-100, 100) for _ in range(100)],
        [4, -10, 0, '1', 6, 1.8, 2, 9, -3, -1, 0, 4],
        (1, 2, 0)
        )


def sequence_validation() -> list:
    """
    Функция sequence_validation запрашивает ввод последовательности и,
    если она корректна, формирует из её элементов список
    """
    print("Введите значения для сортировки в формате: 1, '4a', -3, 'qwerty'")
    pattern = r"""((-?\d*|'\w*'|"\w*")(,\s)?)*"""
    while not re.fullmatch(pattern, s := input()) or s == '':
        print('Некорректный формат ввода, пожалуйста, введите снова.')
    values = list(s.split(', '))
    for idx, c in enumerate(values):
        if c.find("'") != -1 or c.find('''"''') != -1:
            values[idx] = c[1:-1]
        else:
            values[idx] = int(c)
    return values


def border_validation():
    """
    Функция border_validation запрашивает ввод границ
    сортировки и проверяет его на корректность
    """
    print('Введите индекс начала и конца сортировки в формате: 1, 7'
          ' или нажмите enter')
    pattern = r"-?\d*, -?\d*|"
    while not re.fullmatch(pattern, s := input()):
        print('Некорректный формат ввода, пожалуйста, попробуйте снова.')
    if not s:
        beg, end = 0, -1
    else:
        beg, end = tuple(map(int, s.split(', ')))
    return beg, end


def order_validation():
    """
    Функция order_validation запрашивает порядок сортировки и проверяет
    введённое значение на корректность
    """
    print('Для сортировки в обратном порядке введите -1')
    while True:
        s = input()
        if s == '-1' or not s:
            return bool(s)
        else:
            print('Некорректное значение, пожалуйста, попробуйте снова')


def print_menu():
    """
    Функция print_menu выводит в консоль меню и обрабатывает
    команды пользователя
    """
    print('Для выхода введите exit')
    print('Для использования готовых примеров введите example')
    print('Для ввода собственной последовательность введите new')
    while (command := input()) != 'exit':
        if command == 'example':
            for ex in examples:
                quick_sort(ex, reverse=True)
                quick_sort(ex, reverse=False)
        elif command == 'new':
            inp_lst = sequence_validation()
            beg, end = border_validation()
            rev = order_validation()
            quick_sort(inp_lst, begin=beg, end=end, reverse=rev)
        else:
            print('Введена несуществующая команда')
