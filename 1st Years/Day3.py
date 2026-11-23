# # # # # METHOD 1 # #
# # # # arr = ["Spiderman", "Batman", "Superman"]
# # # # print(arr)

# # # # # METHOD 2(i) # #
# # # # mov1 = input("Enter mov1 = ")
# # # # mov2 = input("Enter mov2 = ")
# # # # mov3 = input("Enter mov3 = ")

# # # # arr = [mov1, mov2, mov3]
# # # # print(arr)

# # # # # METHOD 2 (ii) # #
# # # # arr = []
# # # # arr.append(mov1)
# # # # arr.append(mov2)
# # # # arr.append(mov3)
# # # # print(arr)

# # # # # METHOD 2 (iii) # #

# # # # arr = [input("Enter mov1 = "), input("Enter mov2 = "), input("Enter mov3 = ")]
# # # # print(arr)



# # # # # METHOD 3 # #
# # # # arr = []
# # # # for i in range(3):
# # # #     movie = input(f"Enter fav movie {i+1} = ")
# # # #     arr.append(movie)

# # # # print(arr)



# # # # arr = [1, 2, 2, 1]
# # # # arr = ['m', 'a', 'd', 'a', 'm']
# # # # duplicate = arr.copy()
# # # # duplicate.reverse()
# # # # print(arr == duplicate)




# # # # # arr = ['m', 'a', 'd', 'a', 'm']
# # # # arr = [1, "abc", "abc", 1]
# # # # flag = False
# # # # for i in range((len(arr) // 2) + 1):
# # # #     if(arr[i] != arr[len(arr) - i - 1]):
# # # #         flag = False
# # # #         break

# # # #     else:
# # # #         flag = True

# # # # if(flag == True):
# # # #     print(f"{arr} is Palindrome")
# # # # else:
# # # #     print(f"{arr} is not a Palindrome")





# # # # arr = []
# # # # for i in range(1, 11):
# # # #     arr.append(i * i)

# # # # # print(arr)

# # # # target = int(input("Enter the value you want to search: "))

# # # # flag = False
# # # # targetIndex = None
# # # # for i in range(len(arr)):
# # # #     if(target == arr[i]):
# # # #         # print("Target Found !!!")
# # # #         flag = True
# # # #         targetIndex = i
# # # #         break

# # # #     else:
# # # #         flag = False
# # # #         # print("Target NOT Found !!!")

# # # # if(flag == True):
# # # #     print(f"{target} is Found is at position {targetIndex}")
# # # # else:
# # # #     print(f"{target} not Found")



# # # # arr = []
# # # # for i in range(1, 11):
# # # #     arr.append(i * i)

# # # # arr = [1, 2, 3, 4,5, 6, 7,8 ,9 ,10]
# # # # target = 100
# # # # a = arr.index(target)
# # # # print(a)

# # # # print(f'Original Array: {arr}')
# # # # arr.reverse()
# # # # arr2 = arr.copy()
# # # # print(arr.count(36))
# # # # arr.index(target)
# # # # print(f'Reversed Array: {arr2}')


# # # # tup = (42,)
# # # # print(tup)
# # # # print(type(tup))


# # # # arr = [42]
# # # # tup = tuple(arr)

# # # # print(tup)
# # # # print(type(tup))



# # # # setA = {1, 2, 3, 4, 1, 2, 3, 4}
# # # # setA = set()
# # # # print(setA)
# # # # print(type(setA))

# # # setA = {1, 2, 3, 1}
# # # setB = {3, 4, 5, 6}
# # # # print(setA)
# # # # setA.pop()
# # # # print(setA)

# # # # print(setA.union(setB))
# # # # print(setA.intersection(setB))
# # # # print(setA | setB)
# # # # print(setA & setB)

# # # print(f"setA = {setA}")
# # # print(f"setB = {setB}")
# # # # print(setB.difference(setA))
# # # # print(setB.symmetric_difference(setA))
# # # # print(setB - setA)

# # # # setB.remove(4)
# # # setB.discard(40000)
# # # print(setB)






# # # text1 = "Python is a great programming language"
# # # text2 = "Many developers love the python language"


# # # arr = list(text1.split("great"))
# # # print(arr)

# # # arr = []

# # # for i in range(5):
# # #     a = input()
# # #     arr.append(a)

# # # print(arr)

# # text1 = "Python is a greAt programming language".lower()
# # text2 = "MaNy develOpers love tHe python language".lower()

# # setA = set(text1.split())
# # setB = set(text2.split())
# # # print(setA)
# # # print(setB)

# # # print(setA.intersection(setB))             # 1
# # # print(setA.difference(setB))               # 2
# # uniqueElements = setA.symmetric_difference(setB)              # 3
# # print(len(uniqueElements))



# # # print(text1.intersection(text2))
# # # arr = set(map(str, text1.split()))

# # a = 5
# # print(a)

# # a = 10
# # print(a)


# # myDictionary = {
# #     'name': "Shivam",
# #     'role': "Python Trainer",
# #     # 'name': "Mohini"
# #     # 'marks': {
# #     #     'webDev': 98,
# #     #     'java': 76
# #     # }
# # }
# # print(myDictionary['name'])
# # print(myDictionary['role'])

# # myDictionary['names'] = "Mohini"
# # print(myDictionary)
# # print(myDictionary['marks']['webDev'])

# # print(myDictionary.keys())
# # print(myDictionary.values())
# # print(myDictionary.items())
# # print("Dictionary")
# # print(myDictionary['names'])
# # print(myDictionary.get('names'))
# # myDictionary.update({'isTrainer': True})
# # myDictionary['isTrainer'] = True
# # print(myDictionary.setdefault('name', 8900))


# # myDict = {
# #     'table': ["a piece of furniture", "list of facts & figures"],
# #     'cat': "a small animal"
# # }

# # myDict = {
# #     'table': {"a piece of furniture", "list of facts & figures"},
# #     'cat': "a small animal"
# # }

# # print(myDict)


# # myDict = {}

# # sub1 = input("Enter sub1 name = ")
# # marks1 = input("Enter marks of subject 1 = ")

# # sub2 = input("Enter sub2 name = ")
# # marks2 = input("Enter marks of subject 2 = ")

# # sub3 = input("Enter sub3 name = ")
# # marks3 = input("Enter marks of subject 3 = ")

# # myDict.update({sub1:marks1})
# # myDict.update({sub2:marks2})
# # myDict.update({sub3:marks3})

# # print(myDict)




# # myDict = {}

# # for i in range(3):
# #     sub1 = input(f"Enter sub{i+1} name = ")
# #     marks1 = int(input(f"Enter marks of {sub1} = "))

# #     myDict.update({sub1:marks1})

# # print(myDict)


# # # # Remove Duplicates # # #
# # arr = [1, 2, 3, 3, 4, 5, 1]
# # print(set(arr))



# # # # # Print Duplicates ONLY (after Sorting) # # #
# # arr = [1, 2, 3, 3, 4, 5, 1]
# # # arr = [1, 1, 2, 3, 3, 4, 5]

# # arr.sort()

# # for i in range(len(arr) -1):
# #     if(arr[i] == arr[i + 1]):
# #         print(arr[i])



# # # # # Print Duplicates ONLY (after Sorting) # # #
# # arr = [1, 2, 3, 3, 4, 5, 1]
# # # arr = [1, 1, 2, 3, 3, 4, 5]

# # arr.sort()

# # for i in range(1, len(arr)):
# #     if(arr[i] == arr[i - 1]):
# #         print(arr[i])



# # # # Print Duplicates ONLY (after Sorting) # # #
# # arr = [1, 2, 1, 3]
# #arr = [1, 2, 3, 3, 4, 5, 1]
# # arr = [1, 2, 34, 5, 6]

# # dupArr = []
# # for i in range(len(arr)):
# #     for j in range(i+1, len(arr)):
# #         if(arr[i] == arr[j]):
# #             dupArr.append(arr[i])

# # if(len(dupArr) == 0):
# #     print("No Duplicates Found !!!")
# # else:
# #     print(dupArr)

# # # ## # # Frequency Count # # # ## 
# arr = [1, 2, 3, 3, 4, 5, 1]
# uniqueValues = set()
# freqCount = {}
# for i in range(len(arr)):
#     if(arr[i] in uniqueValues):
#         freqCount.update({arr[i] : (freqCount.get(arr[i])) + 1})

#     else:
#         uniqueValues.add(arr[i])
#         freqCount.update({arr[i]: 1})

# # freqCount = {
# #     1: 1,
# #     2: 1,
# #     3: 2,
# # }

# print(freqCount)




print('My name is "Shivam Bansal"')