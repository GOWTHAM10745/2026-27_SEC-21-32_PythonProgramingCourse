def total_and_average(mark1, mark2, mark3):  
    total = mark1+mark2+mark3
    average = total/3
    return total, average
m1= int(input("m1:"))
m2= int(input("m2:"))
m3= int(input("m3:"))
total, average = total_and_average(m1, m2, m3)
print("Total:", total)
print("Average:",average)