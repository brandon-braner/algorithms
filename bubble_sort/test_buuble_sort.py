from bubble_sort.bubble_sort import bubble_sort


class TestBubbleSort:

    def test_list_with_values_asc(self):
        assert bubble_sort([3, 2, 1]) == [1, 2, 3]

        assert bubble_sort([3, 2, 1, 7, 10, 100, 1007]) == [1, 2, 3, 7, 10, 100, 1007]

    def test_list_with_values_desc(self):
        assert bubble_sort([1, 7, 3, 2, 1], direction='desc') == [7, 3, 2, 1, 1]

        assert bubble_sort([3, 2, 1, 7, 10, 100, 1007], direction='desc') == [1007, 100, 10, 7, 3, 2, 1]
