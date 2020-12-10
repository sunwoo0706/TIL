from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_idx = bisect_left(a, left_value)
    right_idx = bisect_right(a, right_value)

    return right_idx - left_idx
    