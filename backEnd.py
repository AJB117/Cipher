# CAESAR
def caesar(caesar_out, shift, e_or_d):
    temp = ""
    if e_or_d == "encrypt":
        for c in caesar_out:
            if not c.isalpha():
                temp += chr(ord(c))
            else:
                if c.islower():
                    temp += chr((((ord(c) - 97) + shift) % 26) + 97)
                else:
                    temp += chr((((ord(c) - 65) + shift) % 26) + 65)
        return temp
    elif e_or_d == "decrypt":
        for c in caesar_out:
            if not c.isalpha():
                temp += chr(ord(c))
            else:
                if c.islower():
                    temp += chr((((ord(c) - 97) - shift) % 26) + 97)
                else:
                    temp += chr((((ord(c) - 65) - shift) % 26) + 65)
        return temp


# TODO
# Vigenere functionality
