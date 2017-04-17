import Tkinter as Tk
import backEnd

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
var.set('')

# Drop down menu for encryption key
Caesar_key = Tk.OptionMenu(window, var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
Caesar_key.pack(side='left')

# Passing plaintext to caesar function in backend; create new window to show selectable
# encrypted string
def backend_caesar():
    x = Caesar_encrypt.get("1.0", 'end-1c')
    win = Tk.Toplevel(window)
    output_box = Tk.Text(win, height=300, width=300)
    output_box.pack()
    shift = var.get()
    output_box.insert(Tk.END, backEnd.caesar_e(x, shift))
    output_box.configure(state=Tk.DISABLED)
    
# Submit plaintext to function to backend
Caesar_submit = Tk.Button(window, text="Caesar Submit", command=get_caesar)
Caesar_submit.pack(side='left')

# CAESAR DECRYPTION

# Where users put their text to decrypt (Caesar)
Caesar_decrypt = Tk.Text(window, height=20, width=40)
Caesar_decrypt.pack()

# Variable for drop down menu for decryption key
decrypt_var = Tk.IntVar(window)
decrypt_var.set('')

# Drop down menu for decryption key
Caesar_dkey = Tk.OptionMenu(window, decrypt_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
Caesar_dkey.pack(side='left')

# Passing encrypted text to caesar decryption function in backend; create new window
# to show selectable encrypted string
def dget_caesar():
    y = Caesar_decrypt.get("1.0", 'end-1c')
    win = Tk.Toplevel(window)
    output_box = Tk.Text(win, height=300, width=300)
    output_box.pack()
    shift = decrypt_var.get()
    output_box.insert(Tk.END, backEnd.caesar_d(y, shift))

# Submit encrypted text to function to backend
Caesar_dsubmit = Tk.Button(window, text="Caesar Decrypt Submit")
Caesar_dsubmit.pack(side='left')
 
# TODO
# Vigenere UI in the same style as Caesar boxes
# Beautification

window.mainloop()
