import Tkinter as Tk
import backEnd

window = Tk.Tk()
window.title("Cipher Encrypt/Decrypt")
window.geometry("900x600")

lbl = Tk.Label(window, text="")
lbl.pack()

i = 0


def increment():
    global i
    i += 1
    lbl.configure(text="%d" % i)

btn = Tk.Button(window, text="Count", command=increment)
btn.pack()

encrypt = Tk.Text(window, height=20, width=40)
encrypt.pack()


def backend_caesar():
    x = encrypt.get("1.0", 'end-1c')
    print backEnd.caesar_1(x)

submit = Tk.Button(window, text="Submit", command=backend_caesar)
submit.pack()

decrypt = Tk.Text(window, height=20, width=40)
decrypt.pack()

window.mainloop()
