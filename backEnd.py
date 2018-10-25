# Caesar functionality
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

# Vigenere functionality
def vigenere(vigenere_out, key, e_or_d):
    i = 0
    k = 0
    if e_or_d == "encrypt":
        for c in key:
            if not c.isalpha():
                return "Use only single characters and words for the Vigenere key."
        temp = ""
        while len(vigenere_out) > len(key):
            key += key
        while i < len(vigenere_out):
            if not vigenere_out[i].isalpha():
                temp += vigenere_out[i]
                i += 1
            else:
                if vigenere_out[i].islower():
                    shift = ord(key[k].lower()) - 97
                    output = chr(((ord(vigenere_out[i]) - 97 + shift) % 26) + 97)
                    temp += output
                    i += 1
                    k += 1
                elif vigenere_out[i].isupper():
                    shift = ord(key[k].upper()) - 65
                    output = chr(((ord(vigenere_out[i]) - 65 + shift) % 26) + 65)
                    temp += output
                    i += 1
                    k += 1
        return temp
    else:
        for c in key:
            if not c.isalpha():
                return "Use only single characters and words for the Vigenere key."
        temp = ""
        while len(vigenere_out) > len(key):
            key += key
        while i < len(vigenere_out):
            if not vigenere_out[i].isalpha():
                temp += vigenere_out[i]
                i += 1
            else:
                if vigenere_out[i].islower():
                    shift = ord(key[k].lower()) - 97
                    output = chr(((ord(vigenere_out[i]) - 97 - shift) % 26) + 97)
                    temp += output
                    i += 1
                    k += 1
                elif vigenere_out[i].isupper():
                    shift = ord(key[k].upper()) - 65
                    output = chr(((ord(vigenere_out[i]) - 65 - shift) % 26) + 65)
                    temp += output
                    i += 1
                    k += 1
        return temp

if "__name__" != "__main__":
    out = "test word yay"
    shift = 3
    key = "testkey"
    e_or_d = "encrypt"
    encryptCaesar = caesar(out, shift, e_or_d)
    encryptVigenere = vigenere(out, key, e_or_d)
    print(encryptCaesar)
    print(encryptVigenere)
    e_or_d = "decyrpt"
    decryptedCaesar = caesar(encryptCaesar,shift , e_or_d)
    decryptedVigenere = vigenere(encryptVigenere, key, e_or_d)
    print(decryptedCaesar)
    print(decryptedVigenere)
