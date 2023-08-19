## Level 1
#1
def access_numbers(n: int):
    for i in range(1, 101):
        if i % 3 == 0 and i % 7 == 0:
            print("BinGo")
        elif i % 3 == 0:
            print("Bin")
        elif i % 7 == 0:
            print("Go")
        else:
            print(i)
access_numbers(101)

#2
def sum_nums(n: int):
    final_sum = 0
    for i in range(n + 1):
        final_sum += i
    return final_sum

print(sum_nums(5))