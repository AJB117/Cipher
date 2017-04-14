def caesar_1(caesar_out):
    temp = ""
    for c in caesar_out:
        if c.isalpha() == False:
            temp += chr(ord(c))
        else:
            temp += chr(ord(c) + 1)
    return temp
