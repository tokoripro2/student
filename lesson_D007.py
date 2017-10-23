input_lines = input()
exponentiation = 0
result = ""
for i in range(9):
    exponentiation = exponentiation + int(input_lines)
    #print(exponentiation)
    if i != 8:
        list_Create = str(exponentiation) + str(" ")
        result = result + list_Create
    else:
        #list_Create = str(exponentiation)
        result = result + str(exponentiation)

print(result)

# input_lines = input()
# exponentiation = 0
# result = ""
# for i in range(9):
#     exponentiation = exponentiation + int(input_lines)
#     print(exponentiation)
#     if i != 9:
#         list_Create = str(exponentiation) + str(" ")
#         result = result.append(list_Create)
#     else:
#         list_Create = str(exponentiation)
#         result = result.append(list_Create)

# print(result)