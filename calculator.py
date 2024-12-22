import tkinter as tk

memory = 0  # Bellek değişkeni
dark_mode = False  # Tema durumu
history = []  # Geçmiş listesi

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
            formatted_result = f"{result:,}"  # Binlik ayırıcı ekle
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, formatted_result)
            # Geçmişi güncelle
            history.append(f"{entry_field.get()} = {formatted_result}")
            update_history()
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

def update_history():
    history_listbox.delete(0, tk.END)
    for item in history[-5:]:  # Son 5 işlemi göster
        history_listbox.insert(tk.END, item)

# Klavye desteği
def keypress(event):
    if event.char.isdigit() or event.char in "+-*/.=":
        button_click(event.char)
    elif event.keysym == "Return":  # Enter tuşu "=" işlemini çağırır
        button_click("=")
    elif event.keysym == "Escape":  # Escape tuşu "C" işlemini çağırır
        button_click("C")

# Tkinter penceresi
window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("400x750")
window.resizable(True, True)

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

# Geçmiş için Listbox
history_listbox = tk.Listbox(window, height=5, font=("Arial", 12))
history_listbox.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

# Satır ve sütun genişlemesini ayarla
for i in range(9):  # 0-8 satır
    window.grid_rowconfigure(i, weight=1)
for j in range(4):  # 0-3 sütun
    window.grid_columnconfigure(j, weight=1)

# Klavye olaylarını pencereye bağla
window.bind("<Key>", keypress)

# Tkinter döngüsü
window.mainloop()