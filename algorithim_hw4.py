# HW 4
# Task 1

def sum_even_an_product_odd(arr: list):
    sum_even = 00
    product_odd = 1

    for e in arr:
        if e % 2 == 0:
            sum_even += e
        else:
            product_odd *= e
    return [sum_even, product_odd]

print(sum_even_an_product_odd([1, 2, 3, 4]))



# Task 2

# def sum_between_range(arr: list, min_val: int, max_val: int):


# Task 3

def buy_and_sell_stock(prices: list):
    maximum = 0


# Task 4

def plus_one(arr: list):
