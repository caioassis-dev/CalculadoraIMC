from tkinter import *

import os

c = os.path.dirname(__file__)
nomeArquivo = c+"\\dadosIMC.txt"


def gravarDados():
    P = float(vpeso.get())
    A = float(valtura.get())
    IMC = P / A**2
    arquivo = open(nomeArquivo, "a")
    arquivo.write("Nome......:%s" % vnome.get())
    arquivo.write("\nPeso....:%s" % vpeso.get())
    arquivo.write("\nAltura..:%s" % valtura.get())
    arquivo.write("\nIMC.....:%s" % IMC)
    arquivo.write("\n\n")
    arquivo.close()


app = Tk()
app.title("Calculadora IMC")
app.geometry("700x500")
app.configure(background="#dda")

Label(app, text="Nome", background="#dda", foreground="#031",
      anchor=W).place(x=295, y=10, width=100, height=20)
vnome = Entry(app)
vnome.place(x=220, y=30, width=200, height=20)

Label(app, text="Peso", background="#dda", foreground="#031",
      anchor=W).place(x=300, y=60, width=100, height=20)
vpeso = Entry(app)
vpeso.place(x=270, y=80, width=100, height=20)

Label(app, text="Altura", background="#dda", foreground="#031",
      anchor=W).place(x=300, y=110, width=100, height=20)
valtura = Entry(app)
valtura.place(x=270, y=130, width=100, height=20)

Button(app, text="Gravar", foreground="#031", command=gravarDados).place(
    x=270, y=170, width=100, height=20)


app.mainloop()
