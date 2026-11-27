counter = int(input("enter sum:"))
def increment():
    global counter 
    counter = counter +1
    print("Inside function, counter =",counter)
print("Before:", counter)
increment()
print("After:", counter)