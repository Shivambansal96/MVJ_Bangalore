# # # n = int(input("Enter a number: "))

# # # for i in range(n, 0, -1):
# # #     if(i > 1):
# # #         print(i, end=", ")
# # #     else:
# # #         print(i, end=".")

# # # print()
# # # print("==================================")
# # # print("============== CODE 1 ENDS =============")
# # # print("==================================")


# # # n = int(input("Enter a num: "))

# # # for i in range(1, 11):
# # #     # print(n, " x ", i, " = ", n*i)
# # #     print(f"{n} x {i} = {n * i}")

# # # print()
# # # print("==================================")
# # # print("============== CODE 2 ENDS =============")
# # # print("==================================")



# # # i = 1

# # # while(i <= 5):
# # #     if(i == 4):
# # #         continue

# # #     print(i)

# # #     i += 1




# # # i = 1

# # # while(i <= 5):
# # #     if(i == 4):
# # #         break

# # #     print(i)

# # #     i += 1



# # # i = 1

# # # while(i <= 5):
# # #     i += 1
# # #     print(i)


# # #  1 2 3 4 5 
# # n = 5

# # total = 0

# # for i in range(1, n+1):
# #     total = total + i
    
# # print(f"Sum of first {n} Natural Numbers: {total}")



# n = int(input("Enter a number: "))
# fact = 1

# for i in range(1,n+1):
#     fact = fact * i

# print(f"Factorial of {n} = {fact} ")


# print(5/0)  # ERO DIVISION ERROR


arr = [10, 23, 14, 50]

arr.append(100)

arr.sort(reverse=True)
print(arr)

arr.reverse()
print(arr)

