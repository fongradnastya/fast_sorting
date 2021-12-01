import pytest
from ..sort_func import quick_sort


def test_with_pos():
    srt_lst = [9, 8, 7, 6, 5]
    quick_sort(srt_lst, begin=1, end=3)
    assert srt_lst == [9, 6, 7, 8, 5], "Ошибка с двумя позициями"


def test_left_pos():
    srt_lst = [9, 2, 7, 8, 0]
    quick_sort(srt_lst, begin=2)
    assert srt_lst == [9, 2, 0, 7, 8], "Ошибка с начальной позицией"


def test_right_pos():
    srt_lst = [9, 2, 7, 8, 0]
    quick_sort(srt_lst, end=2)
    assert srt_lst == [2, 7, 9, 8, 0], "Ошибка с конечной позицией"


if __name__ == '__main__':
    pytest.main()
