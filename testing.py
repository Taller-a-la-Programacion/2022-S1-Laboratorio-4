
import Laboratorio7;
import pytest;

m = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

k = [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]

def test_diferenciaMatrices _1():
    assert Laboratorio7.diferenciaMatrices(m, n) == [[0,0,0,'d','f'], [0,0,0,'j','k'], [0,0,0,'o','p'], ['q','r','s','t','u']]

def test_diferenciaMatrices _2():
    assert Laboratorio7.diferenciaMatrices(m, m) == [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0, [0,0,0,0,0]]
                                                     
def test_diferenciaMatrices _3():
    assert Laboratorio7.diferenciaMatrices(k, n) == [[0,0], [0,0], [0, 0] ['g', 'h']]     
                                                     
m = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

def test_ubicarObjeto_1():
    assert Laboratorio7.ubicarObjeto(m, 2, 3, 3, 4) == [[0,0,0,0], [0,0,0,0] , [0,'x','x','x'] , [0,0,0,0]]
