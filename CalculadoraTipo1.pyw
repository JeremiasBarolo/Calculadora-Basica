#Invocaciones
from tkinter import *
from tkinter import messagebox as MesseageBox

#Root
root= Tk()
root.title("Calculadora")
root.config(bd=25)
root.geometry("350x350")

#Funciones
def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except: 
        MesseageBox.showerror("*error*", "Colocar Bien los Datos")
        numero1.set("")
        numero2.set("")

def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except: 
        MesseageBox.showerror("*error*", "Colocar Bien los Datos")
        numero1.set("")
        numero2.set("")


def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except: 
        MesseageBox.showerror("*error*", "Colocar Bien los Datos")
        numero1.set("")
        numero2.set("")

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except: 
        MesseageBox.showerror("*error*", "Colocar Bien los Datos")
        numero1.set("")
        numero2.set("")
    
def mostrarResultado():
    MesseageBox.showinfo("Resultado", f"El Resultado de la operacion es: {resultado.get()}")
    numero1.set("")
    numero2.set("") 

#Variables, Frames, Strings
numero1= StringVar()
numero2= StringVar()
resultado = StringVar()

marco = Frame(root, width=250, height=250)
marco.config(
            padx=15,
            pady=15,
            bd=1,
            relief=SOLID
)
marco.pack(side=TOP , anchor=CENTER)
marco.pack_propagate(False)


primer_numero_Label = Label(marco, text= "Primer Numero: ").pack() 
primer_numero_Entry = Entry(marco, textvariable=numero1,justify="center").pack()
 
segundo_numero_Label = Label(marco, text= "Segundo Numero: ").pack() 

segundo_numero_Entry = Entry(marco, textvariable=numero2,justify="center").pack()

label = Label(marco, text="").pack()

#Botones
Button(marco, text="Sumar", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar",command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar",command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir",command=dividir).pack(side=LEFT, fill=X, expand=YES)


root.mainloop()