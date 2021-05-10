# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성

import pytest
import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)
from functions import add, minus, multiply, divide

def test_add():
    assert add(1, 2) == str(1 + 2)


def test_minus():
    assert minus(5, 3) == str(5 - 3)


def test_multiply():
    assert multiply(4, 6) == str(4 * 6)


def test_divide():
    assert divide(8, 2) == str(8 / 2)
