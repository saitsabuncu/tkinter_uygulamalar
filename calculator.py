import tkinter as tk
from math import *

# Global history ve memory
history = []
memory = 0

# Tuşların işlevi
def button_click(value):
    global memory
    if value == "C":
        entry_field.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry_field.get())
            if "/0" in entry_field.get():
                raise ZeroDivisionError
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
            # Sonuçları history'e ekle
            history.append(f"{entry_field.get()} = {result}")
            update_history()
        except ZeroDivisionError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Hata: Sıfıra bölünemez!")
    elif value == "√":
        try:
            result = sqrt(float(entry_field.get()))
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Hata")
    elif value == "+/-":
        current_value = entry_field.get()
        if current_value.startswith("-"):
            entry_field.delete(0, tk.END)
            entry_field.insert(0, current_value[1:])
        else:
            entry_field.insert(0, "-")
    elif value == "M+":
        memory += float(entry_field.get())
    elif value == "MR":
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(memory))
    else:
        entry_field.insert(tk.END, value)

def update_history():
    history_listbox.delete(0, tk.END)
    for item in history[-5:]:  # Son 5 işlemi göster
        history_listbox.insert(tk.END, item)

# Pencere oluştur
pence = tk.Tk()
pence.title("Hesap Makinesi")
pence.geometry("400x600")

# Ekran
entry_field = tk.Entry(pence, font=("Arial", 24), borderwidth=2, relief="solid",
                       justify="right")
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=10)

# Tuşlar
buttons = [
    ["C", "CE", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="],
    ["√"]
]

# Tuşları oluştur ve yerleştir
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        tk.Button(pence, text=button, font=("Arial", 18),
                  command=lambda value=button: button_click(value),
                  width=5, height=2, relief="raised", borderwidth=2).grid(row=i+1, column=j,
                                                                          padx=5, pady=5)

# History listesi
history_listbox = tk.Listbox(pence, height=5)
history_listbox.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Tkinter döngüsü
pence.mainloop()