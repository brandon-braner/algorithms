from binary_search.binary_search import binary_search


class TestBinarySearch:
    def test_number_in_array(self):
        assert binary_search([1, 2, 3, 4, 5], 3) is True
        assert binary_search([1, 2, 3, 4, 5], 5) is True
        assert binary_search([0, 1, 2, 3, 4, 5], 0) is True
        assert binary_search([0, 1, 2, 3, 4, 5], 1) is True
        assert binary_search([0, 4, 7, 8, 10, 12], 8) is True

    def test_number_not_in_array(self):
        assert binary_search([1, 2, 3, 4, 5], 6) is False
        assert binary_search([1, 2, 3, 4, 5], 0) is False
        assert binary_search([1, 2, 3, 4, 5], 9) is False

    def test_empty_array(self):
        assert binary_search([], 1) is False
        assert binary_search([], 0) is False
        assert binary_search([], 9) is False
        assert binary_search([], 100) is False
