from binary_search.binary_search import binary_search


class TestBinarySearch:
    def test_number_in_array(self):
        assert binary_search([1, 2, 3, 4, 5], 3) == 2
        assert binary_search([1, 2, 3, 4, 5], 5) == 4
        assert binary_search([0, 1, 2, 3, 4, 5], 0) == 0
        assert binary_search([0, 1, 2, 3, 4, 5], 1) == 1
        assert binary_search([0, 4, 7, 8, 10, 12], 8) == 3

    def test_number_not_in_array(self):
        assert binary_search([1, 2, 3, 4, 5], 6) == -1
        assert binary_search([1, 2, 3, 4, 5], 0) == -1
        assert binary_search([1, 2, 3, 4, 5], 9) == -1

    def test_empty_array(self):
        assert binary_search([], 1) == -1
        assert binary_search([], 0) == -1

