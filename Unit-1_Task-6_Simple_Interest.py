#python program to calculate simple interest.
principal=float(input("principal amount:"))
rate=float(input("rate of interest for annual (in %):"))
time=int(input("time duration (in years):"))
simpleinterest=(principal * rate * time) / 100
print("simpleinterest in Rs.",simpleinterest)
