block1 = "Hello"
block2 = "World"
fullblock = "Hello Wonderful World"
boolean = True #byte 1
        #   [H,E,L,L,o]
        #   [0,1,2,3,4,5]
# Concatenation string, character, number + string, character, number
# print(block1 + " " + block2)
# print(f"{block1} {block2}")
# print from 6 to length of fullblock
# print(fullblock[6:])
# print(block2)
# MATH % / ** AAssignment operator
    # =
    # block2 = 1
    # print(block2)
    # += -= *= /= %=
    # number = 1
    # print(number)
    # number += 1
    # print(number)


# BOOLEAN 
    # 100 byte
    # [1,1,1,1,1,1,1,1,0,0,0,...]
    # print(boolean == True)

    # [ "1" == 1 ] - Equal = False
    # [ 1 != "1" ] - Not Equal = True
    # [ 2 >= 2 ] - True

    # or -> "1" == 1 (False) or 1 == 1 (True) -> True
    # and   5 >= 10 (False) and 12 >= 12 (True)-> False
    # not   10 < 100 not 32 > 2 -> Mariella False : Marvin False

# LOOPS

# [while , for , foreach, dowhile]
# count = 0
# while(count <= 5): # CONDITION <--------------------------
#     print("hello") # PRINT
#     count += 1 # ADD

    # 0 <= 5 
    # hello 1
    # 1 <= 5 
    # hello 2
    # 2 <= 5
    # hello 3
    # 3 <= 5 
    # hello 4
    # 4 <= 5 
    # hello 5
    # 5 <= 5 

# for i in range(1, 5 + 1):
#     print(f"{i} hello")

# letters = "ABCDEFG"
# count = 0
# for i in letters:
#     if(count < 3):
#         print(i)
#     else:
#         print("end")
# while(True) working, not working while(False)

input("number one : ")
input("number two : ")
print("sum  : one and two")
# Retrun the sum of two numbers