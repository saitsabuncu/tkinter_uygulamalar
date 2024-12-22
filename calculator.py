import tkinter as tk

memory = 0  # Bellek değişkeni
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
        except ZeroDivisionError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Hata: Sıfıra bölünemez")
        except SyntaxError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Hata: Geçerli bir ifade girin!")
    elif value == 'MC': # Belleği sıfırla
        memory = 0
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END,"Bellek sıfırlandı")
    elif value == "M+":  # Belleğe ekle
        try:
            memory += float(entry_field.get())
            entry_field.delete(0, tk.END)
        except ValueError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Hata: Geçerli bir sayı girin!")
    elif value == "M-":  # Bellekten çıkar
        try:
            memory -= float(entry_field.get())
            entry_field.delete(0, tk.END)
        except ValueError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Hata: Geçerli bir sayı girin!")
    elif value == 'MR': # Belleği getir
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(memory))

    else:
        entry_field.insert(tk.END, value)

# Tkinter penceresi
window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("400x600")
window.resizable(0, 0)

# Ekran
entry_field = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=10)

# Tuşlar
buttons = [
    ["C", "CE", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="],
["MC", "M+", "M-", "MR"]
]

# Tuşları oluştur ve yerleştir
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        tk.Button(window, text=button, font=("Arial", 18), command=lambda value=button: button_click(value),
                  width=5, height=2, relief="raised", borderwidth=2).grid(row=i+1, column=j, padx=5, pady=5)

# Tkinter döngüsü
window.mainloop()
