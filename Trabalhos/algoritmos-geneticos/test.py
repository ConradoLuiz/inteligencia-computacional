'''
pip install pytest
Rodar com "$pytest unit.py"
Windows: py -m pytest unit.py
'''
import main

def test_binToDecimal():
    assert main.binToDecimal([1,0,0]) == 4
    assert main.binToDecimal([1,0,1]) == 5
    assert main.binToDecimal([1,0,0,1]) == 9
    assert main.binToDecimal([1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1]) == 2_713_497
    assert main.binToDecimal([1 for _ in range(23)]) == 8_388_607

def test_f6():
    assert main.f6(0,0) == 1

def test_decode():
    assert main.decode(165377) == -92.11420824866491
    assert main.decode(2270139) == 8.248688757106962