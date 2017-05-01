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
# PS limit the key to 5 letters
# finish the message encryption i have no clue how to make array loops
# Vigenere functionality
def vigenere(vigenere_out, key, e_or_d):
    key = [1,2,3,4,5]
    if key == "encrypt":
        for [i] in key:
            if not key[i].isalpha():
                temp += chr(ord(key[i])):
            else:
                if key[i].islower():
                    temp += chr((((ord(key[i]) - 97) + shift) % 26) + 97)
            else:
                temp += chr((((ord(key[i]) -65) + shift) % 26) + 65)
        return temp
    elif e_or_d == "decrypt":
        for [i] in key:
            if not key[i].isalpha():
                temp += chr(ord(key[i])):
            else:
                if key[i].islower():
                    temp += chr((((ord(key[i]) - 97) + shift) % 26) + 97)
            else:
                temp += chr((((ord(key[i]) -65) + shift) % 26) + 65)
        return temp
