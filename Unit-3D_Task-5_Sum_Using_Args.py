def sum_values(*args): 
    total = int(input("enter total ="))
    for value in args:
        total = total + value
    return total
print(sum_values(1, 2, 3))
print(sum_values(10, 20, 30, 40))