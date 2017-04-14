import Tkinter as Tk
import backEnd

# Main window
window = Tk.Tk()
window.title("Cipher Encrypt/Decrypt")
window.geometry("900x600")

# Where users put their text to encrypt (Caesar)
Caesar_encrypt = Tk.Text(window, height=20, width=40)
Caesar_encrypt.pack()


# Passing plaintext to caesar function in backend
def backend_caesar():
    x = Caesar_encrypt.get("1.0", 'end-1c')
    print backEnd.caesar_1(x)

# Submit plaintext to function to backend
submit = Tk.Button(window, text="Submit", command=backend_caesar)
submit.pack()

# Where users put their text to decrypt (Caesar)
Caesar_decrypt = Tk.Text(window, height=20, width=40)
Caesar_decrypt.pack()

window.mainloop()
