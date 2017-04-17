# Encryption function: takes plaintext and offsets by key
# Ignores non-alphabetical chars
def caesar_e(caesar_out, shift):
    temp = ""
    for c in caesar_out:
       if c.isalpha == False:
           temp += chr(ord(c))
       else:
            if c.islower():
                temp += chr((((ord(c) - 97) + shift) % 26) + 97)
            else:
                temp += chr((((ord(c) - 65) + shift) % 26) + 65)
    return temp

# Decryption function: takes encrypted text and offsets by key
# Ignores non-alphabetical chars
def caesar_d(caesar_out, shift):
    temp = ""
    for c in caesar_out:
        if c.isalpha == False:
            temp += chr(ord(c))
        else:
            if c.islower():
                temp += chr((((ord(c) - 97) - shift) % 26) + 97)
            else:
                temp += chr((((ord(c) - 65) - shift) % 26) + 65)
    return temp

# TODO
# Vigenere functionality
