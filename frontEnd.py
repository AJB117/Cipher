import Tkinter as Tk
import backEnd

# Functions

# Passing plaintext to caesar function for encryption
def get_caesar():
    win = Tk.Toplevel(window)
    output_box = Tk.Text(win, height=300, width=300)
    output_box.pack()
    shift = var.get()
    output_box.insert(Tk.END, backEnd.caesar(Caesar_encrypt.get("1.0", 'end-1c'), shift), "encrypt")
    output_box.configure(state=Tk.DISABLED)

# Passing encrypted text to caesar function for decryption
def dget_caesar():
    win = Tk.Toplevel(window)
    output_box = Tk.Text(win, height=300, width=300)
    output_box.pack()
    shift = decrypt_var.get()
    output_box.insert(Tk.END, backEnd.caesar(Caesar_decrypt.get("1.0", 'end-1c'), shift), "decrypt")
    output_box.configure(state=Tk.DISABLED)

# Passing plaintext to vigenere function for encryption given a key
def get_vigenere():
    win = Tk.Toplevel(window)
    output_box = Tk.Text(win, height=300, width=300)
    output_box.grid(row=0, column=0)
    output_box.insert(Tk.END, vigenere(vigenere_encrypt.get("1.0", 'end-1c'), keyfield.get("1.0", 'end-1c'), "encrypt"))
    output_box.configure(state=Tk.DISABLED)

# Passing encrypted text to vigenere function for decryption given a key
def dget_vigenere():
    win = Tk.Toplevel(window)
    output_box = Tk.Text(win, height=300, width=300)
    output_box.grid(row=0, column=0)
    output_box.insert(Tk.END, vigenere(vigenere_decrypt.get("1.0", 'end-1c'), dsubmit_keyfield.get("1.0", 'end-1c'), "decrypt"))
    output_box.configure(state=Tk.DISABLED)


# Main window
window = Tk.Tk()
window.title("Cipher Encrypt/Decrypt")
window.geometry("900x600")

# CAESAR ENCRYPTION

# Where users put their text to encrypt
Caesar_encrypt = Tk.Text(window, height=20, width=40)
Caesar_encrypt.pack()

# Variable for drop down menu for key
var = Tk.IntVar(window)
var.set(1)

# Drop down menu for encryption key
Caesar_key = Tk.OptionMenu(window, var, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
Caesar_key.pack(side='left')
    
# Submit plaintext to function to backend
Caesar_submit = Tk.Button(window, text="Caesar Submit", command=get_caesar)
Caesar_submit.pack(side='left')

# CAESAR DECRYPTION

# Where users put their text to decrypt (Caesar)
Caesar_decrypt = Tk.Text(window, height=20, width=40)
Caesar_decrypt.pack()

# Variable for drop down menu for decryption key
decrypt_var = Tk.IntVar(window)
decrypt_var.set(1)

# Drop down menu for decryption key
Caesar_dkey = Tk.OptionMenu(window, decrypt_var, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
Caesar_dkey.pack(side='left')

# Submit encrypted text to function to backend
Caesar_dsubmit = Tk.Button(window, text="Caesar Decrypt Submit", command=dget_caesar)
Caesar_dsubmit.pack(side='left')
 
# Vigenere layout

vigenere_encrypt = Tk.Text(window, height=20, width=40)
vigenere_encrypt.grid(row=2, column=0)

keyfield = Tk.Text(window, height=5, width=10)
keyfield.grid(padx=10, row=2, column=1)

vigenere_decrypt = Tk.Text(window, height=20, width=40)
vigenere_decrypt.grid(row=2, column=3)

# Button needs a command
vigenere_submit = Tk.Button(window, text="Vigenere Submit", command=get_vigenere)
vigenere_submit.grid(row=2, column=2)

dsubmit_keyfield = Tk.Text(window, height=5, width=10)
dsubmit_keyfield.grid(padx=10, row=2, column=4)

# Button needs a command
vigenere_dsubmit = Tk.Button(window, text="Vigenere Decrypt Submit", command=dget_vigenere)
vigenere_dsubmit.grid(row=2, column=5)



window.mainloop()
