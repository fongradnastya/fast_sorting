"""Тестирует функцию quick_sort со значением reverse=True"""
import pytest
from ..sort_func import quick_sort


def test_rev_empty():
    srt_lst = []
    quick_sort(srt_lst, reverse=True), "Ошибка с обратным пустым списком"
    assert srt_lst == []


def test_rev_one_elem():
    srt_lst = [1]
    quick_sort(srt_lst, reverse=True), "Ошибка с обратным 1 элементом"
    assert srt_lst == [1]


def test__rev_corr_order():
    srt_lst = [3, 2, 1]
    quick_sort(srt_lst, reverse=True), "Ошибка с обратным правильным списком"
    assert srt_lst == [3, 2, 1]


def test_rev_list_of_str():
    srt_lst = ['red', 'blue', 'white']
    quick_sort(srt_lst, reverse=True)
    assert srt_lst == ['white', 'red', 'blue'], "Ошибка с обратными строками"


def test_rev_on_incorr_order():
    srt_lst = [4, 0, 1, 2, -1, 10]
    quick_sort(srt_lst, reverse=True)
    assert srt_lst == [10, 4, 2, 1, 0, -1], "Ошибка с обратным неправильным" \
                                            "списком"


if __name__ == '__main__':
    pytest.main()
