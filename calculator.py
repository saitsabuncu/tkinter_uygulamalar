import tkinter as tk
from math import *

# Tuslarin islevi
def button_click(value):
    if value == "C":
        entry_field.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry_field.get())
            if '/0' in entry_field.get():
                raise ZeroDivisionError
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
        except ZeroDivisionError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Hata: Sıfıra bölünemez!")
    else:
        entry_field.insert(tk.END, value)



# Tkinter screen
pence=tk.Tk()
pence.title('Hesap Makinesi')
pence.geometry("400x600")

def keypress(event):
    if event.char.isdigit() or event.char in "+-*/.=":
        button_click(event.char)
    elif event.keysym == "BackSpace":
        entry_field.delete(len(entry_field.get())-1, tk.END)

pence.bind("<Key>", keypress)

# Screen
entry_field=tk.Entry(pence,
                     font=("Arial", 24),
                     borderwidth=2,
                     relief="solid",
                     justify="right")
entry_field.grid(row=0,
                 column=0,
                 columnspan=4,
                 ipadx=8,
                 ipady=25,
                 padx=10,
                 pady=10)

# Tuslar
buttons = [
    ["C", "CE", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

# Tuslari olustur ve yerlestir
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        tk.Button(pence, text=button,
                  font=('Arial',18),
                  command=lambda  value=button: button_click(value),
                  width=5,
                  height=2,
                  relief="raised",
                  borderwidth=2).grid(row=i+1, column=j, padx=5, pady=5)


# Tkinter döngüsü
tk.mainloop()