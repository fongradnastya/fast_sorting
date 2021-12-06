"""Тестирует функцию quick_sort со значением reverse=False"""
import pytest
from ..sort_func import quick_sort


def test_empty(say_hello):
    srt_lst = []
    quick_sort(srt_lst)
    print(say_hello)
    assert srt_lst == [], "Ошибка с пустым списком"


def test_one_element():
    srt_lst = [1]
    quick_sort(srt_lst)
    assert srt_lst == [1], "Ошибка с 1 элементом"


def test_correct_order():
    srt_lst = [1, 2, 3]
    quick_sort(srt_lst)
    assert srt_lst == [1, 2, 3], "Ошибка с правильным начальным порядком"


def test_list_of_str():
    srt_lst = ['red', 'blue', 'white']
    quick_sort(srt_lst)
    assert srt_lst == ['blue', 'red', 'white'], "Ошибка со строками"


def test_on_reversed_order():
    srt_lst = [9, 8, 7, 6, 5]
    quick_sort(srt_lst)
    assert srt_lst == [5, 6, 7, 8, 9], "Ошибка с обратным начальным порядком"


if __name__ == '__main__':
    pytest.main()
