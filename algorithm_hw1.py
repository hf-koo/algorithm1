## Level 1
# 1 prints all numbers from 1 to 100

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


# 2 Compute the sum of digits in all numbers

def sum_nums(n: int):
    final_sum = 0
    for i in range(n + 1):
        final_sum += i
    return final_sum


print(sum_nums(5))


## Level 2
# 1 Find Max Number

def find_max(a: int, b: int, c: int):
    result = 0
    if a > b and a > c:
        result = a
    elif b > c and b > a:
        result = b
    else:
        result = c
    return result


print(find_max(124, 21, 32))


# 2 Leap Year


def leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap year.')
            else:
                print('Not Leap year.')
        else:
            print('Leap year.')
    else:
        print('Not Leap year.')


print(leap_year(2016))



## Level 3