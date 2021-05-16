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
    
    
 def test_wybierz_strategie(mocker):
    mocker.patch('builtins.input', side_effect=['0'])
    with pytest.raises(StopIteration):
    wybierz_strategie()

    mocker.patch('builtins.input', side_effect=['a'])
    with pytest.raises(StopIteration):
    wybierz_strategie()

    mocker.patch('builtins.input', side_effect=['2'])
    with pytest.raises(StopIteration):
    wybierz_strategie()

def test_najlepsze_miejsce():
    A=najlepsze_miejsce([2,2,4,3,4,1])
    assert A==[3,5]
    A = najlepsze_miejsce([2, 5, 4, 3, 4, 1])
    assert A == [2]

def test_list_repetycje():
    A=list_repetycje([1,2,1],4)
    assert A==[2,2,2,2]
    A=list_repetycje([2,1,2,3,1,2],4)
    assert A==[3,3,3,3,2,3,2]
