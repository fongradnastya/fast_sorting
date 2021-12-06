"""Точка входа при запуске пакета"""
import click
import pytest
from input_proc import print_menu


@click.command()
@click.option("--run_test", "-t", default=0)
def start(run_test):
    if run_test:
        pytest.main(['sorting_package/tests'])
    else:
        print_menu()


if __name__ == "__main__":
    start()
