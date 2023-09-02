# def sort_both(arr1, arr2):
#     a1 = sorted(arr1)
#     a2 = sorted(arr2)
#     for i in range(len(a2)-1):
#         if a1[i] != a2[i]:
#             return (a1[i] + " is the missing element")
#
#     print(str(a1[-1]) + " is missing element")
#
# test1 = [1, 3, 5, 6, 8]
# test2 = [6, 5, 3, 1]
# print(sort_both(test1, test2))
#
#
# def largest_sum(arr: list):
#     cur_sum = max_sum = arr[0]
#
#     for num in arr[1:]:
#         cur_sum = max(cur_sum + num, num)
#         max_sum = max(max_sum, cur_sum)
#     return max_sum
#
# test_list = [-4, 2, -1, 3, 4, 10, 10, -10, -1]
# print(largest_sum(test_list))


