# Se debe importar base64
# La password es 1234
from tkinter import *
from tkinter import messagebox
import base64

#Funciones
def reset():
    '''Limpia el cuadro de texto de la app'''
    code.set("")
    cuad_txt1.delete(1.0, END)

def encrypt():
    '''Muestra y crea el mensaje encriptado'''
    pwd = code.get()

    if pwd == "1234":
        window = Toplevel(wn)
        window.title("Encryption")
        window.geometry("400x200")
        window.configure(bg="#a1c1be")

        msg = cuad_txt1.get(1.0, END)
        enconde_msg = msg.encode("ascii")
        base64_bytes = base64.b64encode(enconde_msg)
        encriptado = base64_bytes.decode("ascii")

        Label(window, text="ENCRIPTADO", font="arial", fg="#59554e",
              bg="#a1c1be").place(x=10, y=0)
        txt2 = Text(window, font="Rebote 10", bg="#ffffff",
                    relief=GROOVE, wrap=WORD, bd=0)
        txt2.place(x=10, y=40, width=380, height=150)

        txt2.insert(END, encriptado)
    elif pwd == "":
        messagebox.showerror("Encriptación", "Ingrese PWD")
    elif pwd != "1234":
        messagebox.showerror("Encriptación", "PWD invalida")

def decrypt():
    '''Muestra y crea el mensaje desencriptado'''
    pwd = code.get()

    if pwd == "1234":
        window2 = Toplevel(wn)
        window2.title("Decryption")
        window2.geometry("400x200")
        window2.configure(bg="#e2e3d9")

        msg = cuad_txt1.get(1.0, END)
        decode_msg = msg.encode("ascii")
        base64_bytes = base64.b64decode(decode_msg)
        desencriptado = base64_bytes.decode("ascii")

        Label(window2, text="DESENCRIPTADO", font="arial", fg="#59554e",
              bg="#e2e3d9").place(x=10, y=0)
        txt2 = Text(window2, font="Rebote 10", bg="#ffffff",
                    relief=GROOVE, wrap=WORD, bd=0)
        txt2.place(x=10, y=40, width=380, height=150)

        txt2.insert(END, desencriptado)
    elif pwd == "":
        messagebox.showerror("Desencriptación", "Ingrese PWD")
    elif pwd != "1234":
        messagebox.showerror("Desencriptación", "PWD invalida")

#Ventana Principal
wn = Tk()
wn.geometry("375x398")
wn.title("KryApp")

# Cuadro de texto para mensaje
Label(text="Pon texto para encriptar o desencriptar",
      fg="#59554e", font=("calibri", 12)).place(x=10, y=10)

cuad_txt1 = Text(font="Robote 20", bg="#ffffff", relief="groove",
                 wrap="word",bd=0)
cuad_txt1.place(x=10, y=50, width=355, height=100)

# Cuadro de texto para clave
Label(text="Pon secret key para encriptar o desencriptar",
      fg="#59554e", font=("calibri", 12)).place(x=10, y=170)
code = StringVar()
Entry(textvariable=code, width=22,
      bd=0, font=("arial", 25), show="*").place(x=10, y=200)

# Boton encriptar
Button(text="ENCRIPTAR", height="2", width=20, bg="#a1c1be",
       fg="#59554e", bd=0, command=encrypt).place(x=10, y=250)
# Boton Desencriptar
Button(text="DESENCRIPTAR", height="2", width=20, bg="#e2e3d9",
       fg="#59554e", bd=0, command=decrypt).place(x=200, y=250)
# Boton de Reset
Button(text="RESET", height="2", width=47, bg="#59554e",
       fg="#ffffff", bd=0, command=reset).place(x=10, y=300)

wn.mainloop()


