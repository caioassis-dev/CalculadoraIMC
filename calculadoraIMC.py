from tkinter import *

app = Tk()
app.title("Calculadora IMC")
app.geometry("700x500")
app.configure(background="#dda")

Label(app, text="Nome", background="#dda", foreground="#031",
      anchor=W).place(x=295, y=10, width=100, height=20)
vnome = Entry(app)
vnome.place(x=220, y=30, width=200, height=20)

app.mainloop()
