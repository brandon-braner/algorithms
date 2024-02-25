from bubble_sort.bubble_sort import bubble_sort


class TestBubbleSort:

    def test_list_with_values(self):
        assert bubble_sort([3, 2, 1]) == [1, 2, 3]

        assert bubble_sort([3, 2, 1, 7, 10, 100, 1007]) == [1, 2, 3, 7, 10, 100, 1007]
