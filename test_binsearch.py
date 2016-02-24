
from pytest import raises
from binsearch import binary_search
import numpy as np

def test_exists():
    assert binary_search([1,2,3,4.5,5], 4.5) == 3

def test_missing():
    assert binary_search([1,2,3,4.5,5], 4) == -1

def test_multiple():
    assert binary_search([1,1,1,1,1], 1) == 2
    
def test_inf():
    assert binary_search([np.inf], np.inf) == 0
        
def test_range():
    assert binary_search([0,1,2,3,4,5], 2 , 1, 3) == 2
    
def test_missing_range():
    assert binary_search([0,1,2,3,4,5], 2 , 0, 1) == -1