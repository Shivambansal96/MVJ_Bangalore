# # # # # # # =========================================================================
# # # # # # # =========================================================================
# # # # # # # ========= Staring Python class with print Statements ====================
# # # # # # # =========================================================================
# # # # # # # =========================================================================

# # # # # # print("HellO world!!!", end=" ")
# # # # # # print("Shivam Bansal")


# # # # # # # print("My name is Shivam", "Today we are learning Python !", sep="; ")

# # # # # # # Explaining DataTypes
# # # # # # # n = None   
# # # # # # # int n;




# # # # # # a = 5

# # # # # # a = a+ 5
# # # # # # a += 5

# # # # # # print(a)



# # # # # # print(2 == 2 and not(4 == 5))


# # # # # a = 5
# # # # # b = "3"

# # # # # b = int(b)

# # # # # add = a + b

# # # # # print(add)
# # # # # print(type(b))


# # # # name = int(input("Enter your age = "))

# # # # print("Age = ", name)


# # # name = "Shivam"
# # # age = 24
# # # city = "Hyderabad"

# # # # print("Hello Shivam, I am 24 years old and I live in Hyderabad.")
# # # # print("Hello", name, "I am", age, "years old and I live in", city, ".")

# # # print(f"Hello {name}, I am {age} years old and I live in {city}.")





# # # # firstName = input("Enter first name: ")
# # # # lastName = input("Enter second name: ")
# # # # print(f"First Name: {firstName}")
# # # # print(f"Last Name: {lastName}")



# # # # a = int(input("Enter a num: "))
# # # # b = int(input("Enter another num: "))

# # # # print(a + b)


# # # # print(4 >= 2)





# # # firstName = input("Enter first name: ") # Shivam
# # # lastName = input("Enter last name: ") # Bansal

# # # new = firstName + " " + lastName

# # # print(len(new))


# # # firstName = input("Enter your name: ")
# # # print("FirstName: ", firstName)
# # # print("length of name = ", len(firstName))



# # # s = "madam"

# # # print(s[0] == s[len(s) - 1])


# # s = "i Am a CodEr."

# # print(s.endswith("er"))
# # print(s.endswith("er."))
# # print(s.capitalize())
# # # print(s.replace("a", "i", 1))
# # # print(s.replace("q", "Shivam Bansal"))
# # print(s.replace("CodEr", "Trainer"))
# # # print(s.find("C"))
# # print(s.find("CodEr"))
# # print(s.swapcase())
# # print(s.count("a"))




# s = "Shivam"

# # output = s[1:5]
# # output = s[1:5:2]
# # output = s[-3:-1:-1]
# # output = s[-1 : -(len(s) + 1) : -1]

# # rev = s[::-1]
# # print(s == rev)



# # trafficColor = input("Enter the color of light: ").lower()

# # if(trafficColor == "red"):
# #     print("STOP!")
# # elif(trafficColor == "yellow"):
# #     print("Ready to Go!")
# # elif(trafficColor == "green"):
# #     print("Go!")
# # else:
# #     print("Wrong Input!!!")
    
# # marks = 90
# # if(marks > 90 and marks <= 100):
# #     grade = "A"
# # elif(marks > 80 and marks <= 90):
# #     grade = "B"
# # elif(marks > 70 and marks <= 80):
# #     grade = "C"
# # elif(marks > 60 and marks <= 70):
# #     grade = "D"
# # else:
# #     grade = "F"

# # print(grade)



# # marks = 90
# # if(marks > 90 and marks <= 100):
# #     grade = "A"
# # elif(marks > 80):
# #     grade = "B"
# # elif(marks > 70):
# #     grade = "C"
# # elif(marks > 60):
# #     grade = "D"
# # else:
# #     grade = "F"

# # print(grade)

# # age = 65

# # if(age >= 18 and age < 60):
# #     print("ADULT")

# # elif(age >= 60):
# #     print("SENIOR CITIZEN")

# # else:
# #     print("MINOR")





# # age = 25

# # if(age >= 18):
# #     if(age >= 60):
# #         if(age >= 80):
# #             print("SUPER SENIOR CITIZEN")
# #         else:
# #             print("SENIOR CITIZEN")
# #     else:
# #         print("ADULT")
# # else:
# #     print("MINOR")

# # num = 452

# # if(num % 2 == 1):
# #     print("ODD")
# # else:
# #     print("EVEN")


# # m1 = 98
# # m2 = 530
# # m3 = 103

# # if(m1 > m2 and m1 > m3):
# #     print(f"{m1} is the largest.")
# # elif(m2 > m3):
# #     print(f"{m2} is the largest.")
# # # elif(m3 > m1 and m3 > m1):
# # else:
# #     print(f"{m3} is the largest.")


# num = 491

# if(num % 7 == 0):
#     print("Divisible by 7")
# else:
#     print("NOT Divisible by 7")


# print("Hello World!")

# for i in range(100000):
#     print("My name is Shivam")


# for i in range(10):

#     if(i == 5):
#         print("ENTERED 5")
#         continue

# else:
#     print("CODE ENDS")


for i in range(1, 101):
    if(i < 100):
        print(i, end = ", ")
    else:
        print(i, end = ". ")


# for i in range(100, 0, -1):
    # print(i)