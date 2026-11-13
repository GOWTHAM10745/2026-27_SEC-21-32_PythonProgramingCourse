def simple_interest(principal, time, rate= int(input("enter number"))):
    return (principal * time * rate) / 100
print("SI (default rate):", simple_interest(1000, 2))
print("SI (rate=8):", simple_interest(1000, 2, 8))