"""
pip install pytest pytest-mock
"""

import pytest
from aplication import *


def test_alfabet():
    A = alfabet(10)
    assert A == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    A = alfabet(1)
    assert A == [1]


def test_pobierz_wartosci(mocker):
    mocker.patch('builtins.input', side_effect=['2', '5'])
    assert pobierz_wartosci() == (2, 5)

    mocker.patch('builtins.input', side_effect=['0', '5'])
    with pytest.raises(StopIteration):
        pobierz_wartosci()

    mocker.patch('builtins.input', side_effect=['2', '-2'])
    with pytest.raises(StopIteration):
        pobierz_wartosci()

def test_strategia1_przegrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '1'])
    strategia_1([1, 2, 3], 4)
    captured = capsys.readouterr()
    assert "Przegrałeś" in captured.out

def test_strategia2a_przegrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '1'])
    strategia_2a([1, 2, 3], 4)
    captured = capsys.readouterr()
    assert "Przegrałeś" in captured.out

def test_strategia2b_przegrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '1'])
    strategia_2b([1, 2, 3], 4)
    captured = capsys.readouterr()
    assert "Przegrałeś" in captured.out
