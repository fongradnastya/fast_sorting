"""Точка входа при запуске пакета"""
import fire
from sorting_package.input_proc import print_menu

if __name__ == "__main__":
    fire.Fire(print_menu())
