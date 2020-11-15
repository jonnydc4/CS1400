def decimalToRep(i, b):
    lookup = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = ""
    while i >= b:
        remainder = i % b
        answer = lookup[remainder] + answer
        i = int(i / b)
    return lookup[i] + answer

    # if i < b:
    #     return lookup[i]
    # else:
    #     quotient = int(i / b)
    #     remainder = i % b
    #     return lookup[quotient] + lookup[remainder]


print(10, 10, decimalToRep(10, 10))
print(10, 8, decimalToRep(10, 8))
print(10, 2, decimalToRep(10, 2))
print(10, 16, decimalToRep(10, 16))
