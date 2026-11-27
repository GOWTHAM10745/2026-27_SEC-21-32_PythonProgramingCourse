def student_details(**kwargs):  
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_details(name="gowtham", maths= 85, science= 90)  