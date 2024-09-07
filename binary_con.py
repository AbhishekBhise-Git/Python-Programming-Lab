def convertBinary(num):
    binary = 0
    i, rem = 1, 0
    while num != 0:
        rem = num % 2
        num = num // 2
        binary += rem * i
        i *= 10
    return binary


decimal_num = 21
print("Binary of", decimal_num, "is : ", end="")
print(convertBinary(decimal_num))
