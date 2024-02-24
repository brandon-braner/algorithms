from linear_search import linear_search


class TestLinearSearch:

    def test_number_in_list(self):
        assert linear_search([1, 2, 3, 4, 5], 3) == 2


    def test_number_not_in_list(self):
        assert linear_search([1, 2, 3, 4, 5], 6) == -1