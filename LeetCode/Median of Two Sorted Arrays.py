from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    total_len = len_nums1 + len_nums2
    start = 0
    end = len_nums1
    while start <= len_nums2:
        prtn_nums1 = (start + end) // 2
        prtn_nums2 = ((total_len + 1) // 2) - prtn_nums1
        max_left_nums1 = nums1[prtn_nums1 - 1] if prtn_nums1 - 1 >= 0 else float("-infinity")
        max_left_nums2 = nums2[prtn_nums2 - 1] if prtn_nums2 - 1 >= 0 else float("-infinity")
        min_right_nums1 = nums1[prtn_nums1] if prtn_nums1 < len_nums1 else float("infinity")
        min_right_nums2 = nums2[prtn_nums2] if prtn_nums2 < len_nums2 else float("infinity")
        if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
            if total_len % 2:
                return max(max_left_nums1, max_left_nums2)
            else:
                return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
        elif max_left_nums1 > min_right_nums2:
            end = prtn_nums1 - 1
        else:
            start = prtn_nums1 + 1


print(find_median_sorted_arrays([1, 3], [2]))
