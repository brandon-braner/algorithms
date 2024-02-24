from binary_search.binary_search import binary_search

def test_number_in_array():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([0,1, 2, 3, 4, 5], 0) == 0
def test_number_not_in_array():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 0) == -1