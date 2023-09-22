## HW 5


# Task 1
# Selection Sort

def selection_sort(arr:list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([20, 12, 10, 15, 2]))


# Task 2
#Bubble Sort

def bubble_sort_descending(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort_descending([2,45,0,11,1]))



# Task 3
#Insertion Sort

def insertion_sort_descending(arr:list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Example usage
arr = [12, 11, 13, 5, 6]

insertion_sort_descending(arr)

print(arr)