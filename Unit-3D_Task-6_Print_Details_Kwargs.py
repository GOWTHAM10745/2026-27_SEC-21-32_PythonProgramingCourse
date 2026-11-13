def print_details(**kwargs):  
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="sukumar", age=122, city="red city")