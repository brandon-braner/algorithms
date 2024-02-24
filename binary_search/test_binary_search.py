from binary_search.binary_search import binary_search

def test_number_in_array():
    assert binary_search([1, 2, 3, 4, 5], 3) is True
    assert binary_search([1, 2, 3, 4, 5], 5) is True
    assert binary_search([0, 1, 2, 3, 4, 5], 0) is True
    assert binary_search([0, 1, 2, 3, 4, 5], 1) is True
def test_number_not_in_array():
    assert binary_search([1, 2, 3, 4, 5], 6) is False
    assert binary_search([1, 2, 3, 4, 5], 0) is False
    assert binary_search([1, 2, 3, 4, 5], 9) is False