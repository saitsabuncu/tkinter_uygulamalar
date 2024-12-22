import tkinter as tk

memory = 0  # Bellek değişkeni
dark_mode = False  # Tema durumu: Varsayılan olarak açık tema

# Tuşların işlevi
def button_click(value):
    global memory
    if value == "C":
        entry_field.delete(0, tk.END) # Tüm girdiyi temizler
    elif value == 'CE':
        current_text = entry_field.get()
        entry_field.delete(len(current_text) - 1, tk.END)  # Son karakteri siler
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

def change_theme():
    global dark_mode
    if not dark_mode: # Karanlık moda geçiş
        window.config(bg='black')
        entry_field.config(bg="black", fg="white")

        for button in all_buttons:
            button.config(bg="gray", fg="white")
        theme_button.config(text="Varsayılan Mod")
        dark_mode = True
    else:  # Varsayılan moda dönüş
        window.config(bg="white")
        entry_field.config(bg="white", fg="black")
        for button in all_buttons:
            button.config(bg="lightgray", fg="black")
        theme_button.config(text="Karanlık Mod")
        dark_mode = False
# Tkinter penceresi
window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("400x600")
window.resizable(0, 0)

# Ekran
entry_field = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="solid",
                       justify="right")
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
all_buttons = []
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        btn=tk.Button(window, text=button, font=("Arial", 18),
                      command=lambda value=button: button_click(value),
                        width=5, height=2, relief="raised", borderwidth=2,
                      bg="lightgray", fg="black")
        btn.grid(row=i + 1, column=j, padx=5, pady=5)
        all_buttons.append(btn)

# Tema değiştirme butonu
theme_button = tk.Button(window, text="Karanlık Mod", font=("Arial", 14),
                         command=change_theme, width=20)
theme_button.grid(row=7, column=0, columnspan=4, pady=10)



# Tkinter döngüsü
window.mainloop()
