"""
pip install pytest pytest-mock
"""

import pytest
from aplication import *

def test_sprawdz_abelowo():
    slowo=[1, 2, 1, 3, 1, 2]
    alfabet=[1, 2, 3]
    assert sprawdz_abelowo(slowo, alfabet) == 0
    slowo=[1, 2, 3, 2, 1, 3]
    alfabet=[1, 2, 3, 4]
    assert sprawdz_abelowo(slowo, alfabet) == 1

def test_sprawdz_abel():
    slowo=[1, 2, 1, 3, 1, 4, 2, 3]
    alfabet=[1, 2, 3, 4]
    assert sprawdz_abel(slowo, alfabet) == [0, 0]
    slowo=[1, 2, 1, 3, 1, 2, 3, 4]
    alfabet=[1, 2, 3, 4]
    assert sprawdz_abel(slowo, alfabet) == [1, '1<213-123>4']


def test_sprawdz_abelowo():
    assert sprawdz_abelowo([1, 2, 1, 3, 1, 2], [1, 2, 3]) == 0
    assert sprawdz_abelowo([1, 2, 3, 2, 1, 3], [1, 2, 3, 4]) == 1


def test_sprawdz_abel():
    assert sprawdz_abel([1, 2, 1, 3, 1, 4, 2, 3], [1, 2, 3, 4]) == [0, 0]
    assert sprawdz_abel([1, 2, 1, 3, 1, 2, 3, 4], [1, 2, 3, 4]) == [1, '1<213-123>4']


def test_alfabet():
    a = alfabet(10)
    assert a == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = alfabet(1)
    assert a == [1]


def test_pobierz_wartosci(mocker):
    mocker.patch('builtins.input', side_effect=['2', '5'])
    assert pobierz_wartosci() == (2, 5)

    mocker.patch('builtins.input', side_effect=['0', '5'])
    with pytest.raises(StopIteration):
        pobierz_wartosci()

    mocker.patch('builtins.input', side_effect=['2', '-2'])
    with pytest.raises(StopIteration):
        pobierz_wartosci()

# testy potwierdzajace, że nie da się wygrać z trzyliterowym alfabetem i słowem długości 8
# dla każdej strategii wybrano losowo 100 takich słów

def test_strategia1_8_3(mocker, capsys):
    j = 0
    while j < 100:
        lista = [0 * i for i in range(0, 8)]
        i = 0
        while i < 8:
            lista[i] = str(random.randint(1, 3))
            i = i + 1
        mocker.patch('builtins.input', side_effect=lista)
        strategia_1([1, 2, 3], 8)
        captured = capsys.readouterr()
        assert "Przegrałeś" in captured.out
        j = j + 1


def test_strategia2a_8_3(mocker, capsys):
    j = 0
    while j < 100:
        lista = [0 * i for i in range(0, 8)]
        i = 0
        while i < 8:
            lista[i] = str(random.randint(1, 3))
            i = i + 1
        mocker.patch('builtins.input', side_effect=lista)
        strategia_2a([1, 2, 3], 8)
        captured = capsys.readouterr()
        assert "Przegrałeś" in captured.out
        j = j + 1


def test_strategia2b_8_3(mocker, capsys):
    j = 0
    while j < 100:
        lista = [0 * i for i in range(0, 8)]
        i = 0
        while i < 8:
            lista[i] = str(random.randint(1, 3))
            i = i + 1
        mocker.patch('builtins.input', side_effect=lista)
        strategia_2b([1, 2, 3], 8)
        captured = capsys.readouterr()
        assert "Przegrałeś" in captured.out
        j = j + 1


def test_strategia1_przegrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '1'])
    strategia_1([1, 2, 3], 4)
    captured = capsys.readouterr()
    assert "Przegrałeś" in captured.out


def test_strategia1_wygrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '2', '3'])
    strategia_1([1, 2, 3], 3)
    captured = capsys.readouterr()
    assert "Wygrałeś" in captured.out


def test_strategia2a_przegrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '1'])
    strategia_2a([1, 2, 3], 4)
    captured = capsys.readouterr()
    assert "Przegrałeś" in captured.out


def test_strategia2a_wygrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '2', '3'])
    strategia_1([1, 2, 3], 3)
    captured = capsys.readouterr()
    assert "Wygrałeś" in captured.out


def test_strategia2b_przegrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '1'])
    strategia_2b([1, 2, 3], 4)
    captured = capsys.readouterr()
    assert "Przegrałeś" in captured.out


def test_strategia2b_wygrana(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['1', '2', '3'])
    strategia_1([1, 2, 3], 3)
    captured = capsys.readouterr()
    assert "Wygrałeś" in captured.out


def test_wybierz_strategie(mocker):
    mocker.patch('builtins.input', side_effect=['0'])
    with pytest.raises(StopIteration):
        wybierz_strategie()

    mocker.patch('builtins.input', side_effect=['-1'])
    with pytest.raises(StopIteration):
        wybierz_strategie()


def test_najlepsze_miejsce():
    a = najlepsze_miejsce([2, 2, 4, 3, 4, 1])
    assert a == [4, 2]
    a = najlepsze_miejsce([2, 5, 4, 3, 4, 1])
    assert a == [1]


def test_list_repetycje():
    a = list_repetycje([1, 2, 1], 4)
    assert a == [2, 2, 2, 2]
    a = list_repetycje([2, 1, 2, 3, 1, 2], 4)
    assert a == [3, 3, 3, 3, 2, 3, 2]

def test_wygrana(capsys):
    wygrana()
    captured = capsys.readouterr()
    assert "Wygrałeś" in captured.out

def test_przegrana( capsys):
    przegrana([1, 1, 2], [1, 2, 3])
    captured = capsys.readouterr()
    assert "Przegrałeś" in captured.out
