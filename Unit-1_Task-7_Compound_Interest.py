principle=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest for annual (in %):"))
time=int(input("Enter the time duration (in years):"))
compoundinterest=principle*(1+rate/100)**time-principle
print("Compound interest in Rs.",compoundinterest)
