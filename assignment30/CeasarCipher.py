plainText = input("Enter messege (must be lowercase): ")
distance = int(input("Enter distance value: "))
code = ""
for letter in plainText:
    ordValue = ord(letter)
    cipherValue = ordValue + distance
    if cipherValue > (ord("z") + 1):
        cipherValue = ord("a") + distance - \
                        (ord("z") - ordValue + 1)
    code += chr(cipherValue)
print(code)