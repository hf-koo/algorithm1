## Algorithim 3

# Task 1


def find_two_lowest(arr: list):
    new_list = sorted(list1)
    return new_list[0], new_list[1]

list1 = [198, 3, 4, 9, 10, 9, 2]

print(find_two_lowest(list1))



# Task 2


def invert_list(arr: list):
        list2 = []
        for num in list1:
            new_num = num * -1
            list2.append(new_num)
        return list2


list1 = [1, 5, -2, 4]

print(invert_list(list1))



# Task 3


def max_diff(arr: list):
    # if len(list1) == 0:
    #     return 0
        list2 = sorted(list1)
        num1 = list2[-1] - list2[0]
        return num1

list1 = [3, 5, 7, 2]


print(max_diff(list1))



# Task 4

def count_larger_neighbors(arr: list):
    count = 0
    if len(list1) < 3:
        return count
    for i in range(1, len(list1) - 2):
        if list1[i] > list1[i - 1] and list1[i] > list1[i + 1]:
            count += 1
    return count

list1 = [2, 56, 7, 21, 22, 19, 26]
result = count_larger_neighbors(list1)

print(result)




# Task 5

def subtract_min(arr: list):
    list2 = []
    num = min(list1)
    # print(num)

    for n in list1:
        n -= 1
        list2.append(n)
    return list2



list1 = [9, 2, 5, 4, 7, 6, 1]

print(subtract_min(list1))