import tkinter as tk
from math import sin, cos, tan, log, sqrt
import json

memory = 0
dark_mode = False
history = []
current_language = "en"

# Dil yükleme fonksiyonu
def load_language(lang="en"):
    global current_language
    current_language = lang
    with open("languages.json", "r") as file:
        languages = json.load(file)
    return languages.get(lang, languages["en"])

language_texts = load_language()

def button_click(value):
    global memory
    if value == language_texts["clear"]:
        entry_field.delete(0, tk.END)
    elif value == language_texts["backspace"]:
        current_text = entry_field.get()
        entry_field.delete(len(current_text) - 1, tk.END)
    elif value == language_texts["equal"]:
        try:
            result = eval(entry_field.get())
            formatted_result = f"{result:,}"
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, formatted_result)
            history.append(f"{entry_field.get()} = {formatted_result}")
            update_history()
            save_history()
        except ZeroDivisionError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, language_texts["error_divide_by_zero"])
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, language_texts["error_invalid_input"])
    elif value in ["sin", "cos", "tan", "log", "√"]:
        try:
            num = float(entry_field.get())
            if value == "sin":
                result = sin(num)
            elif value == "cos":
                result = cos(num)
            elif value == "tan":
                result = tan(num)
            elif value == "log":
                result = log(num)
            elif value == "√":
                result = sqrt(num)
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, result)
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, language_texts["error_invalid_input"])
    else:
        entry_field.insert(tk.END, value)

def change_language(lang):
    global language_texts
    language_texts = load_language(lang)
    update_ui_texts()

def update_ui_texts():
    standard_button.config(text=language_texts["standard"])
    scientific_button.config(text=language_texts["scientific"])
    theme_button.config(text=language_texts["dark_mode"])
    for btn, text in zip(all_buttons, button_labels):
        btn.config(text=text)

def change_theme():
    global dark_mode
    if not dark_mode:
        window.config(bg='black')
        entry_field.config(bg="black", fg="white")
        for button in all_buttons:
            button.config(bg="gray", fg="white")
        theme_button.config(text="Varsayılan Mod")
        dark_mode = True
    else:
        window.config(bg="white")
        entry_field.config(bg="white", fg="black")
        for button in all_buttons:
            button.config(bg="light gray", fg="black")
        theme_button.config(text="Karanlık Mod")
        dark_mode = False

def update_history():
    history_listbox.delete(0, tk.END)
    for item in history[-5:]:
        history_listbox.insert(tk.END, item)

def save_history():
    with open("history.txt", "w") as file:
        file.write("\n".join(history))

def load_history():
    try:
        with open("history.txt", "r") as file:
            for line in file:
                history.append(line.strip())
            update_history()
    except FileNotFoundError:
        pass
def update_buttons(button_set):
    """Dinamik olarak butonları günceller."""
    for my_btn in all_buttons:
        my_btn.grid_forget()  # Mevcut düğmeleri gizle
    all_buttons.clear()  # Tüm düğme listesini temizle
    for row_index, row in enumerate(button_set):
        for col_index, button in enumerate(row):
            my_btn = tk.Button(button_frame, text=button, font=("Verdana", 18), bg="lightgray", fg="black",
                               command=lambda value=button: button_click(value))
            my_btn.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5)
            all_buttons.append(my_btn)

# Tkinter penceresi ve diğer kodlar aşağıda devam ediyor
window = tk.Tk()
window.title("Modern Hesap Makinesi")
window.geometry("600x800")
window.resizable(True, True)
window.config(bg="#f2f2f2")

def switch_to_standard():
    """Standart mod tuşlarını yükler."""
    button_set = [
        [language_texts["clear"], language_texts["backspace"], "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["+/-", "0", ".", language_texts["equal"]],
        ["MC", "M+", "M-", "MR"]
    ]
    update_buttons(button_set)
    # Geçmiş kutusunu standart modda göster
    history_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

def switch_to_scientific():
    """Bilimsel mod tuşlarını yükler."""
    button_set = [
        [language_texts["clear"], language_texts["backspace"], "sin", "cos"],
        ["tan", "log", "√", "^"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["+/-", "0", ".", language_texts["equal"]]
    ]
    update_buttons(button_set)
    # Geçmiş kutusunu bilimsel modda gizle
    history_listbox.grid_forget()


entry_field = tk.Entry(window, font=("Verdana", 24), bg="#ffffff", fg="#000000", justify="right")
entry_field.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

history_listbox = tk.Listbox(window, height=5, font=("Arial", 12), bg="#ffffff", fg="#000000")
history_listbox.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

button_frame = tk.Frame(window, bg="#f2f2f2")
button_frame.grid(row=2, column=0, columnspan=4, sticky="nsew")

for i in range(6):
    button_frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    button_frame.grid_columnconfigure(j, weight=1)

button_labels = [
    language_texts["clear"], language_texts["backspace"], "%", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "+/-", "0", ".", language_texts["equal"]
]

all_buttons = []
for i, label in enumerate(button_labels):
    btn = tk.Button(button_frame, text=label, font=("Verdana", 18), bg="light gray", fg="black",
                    command=lambda value=label: button_click(value))
    btn.grid(row=i // 4, column=i % 4, sticky="nsew", padx=5, pady=5)
    all_buttons.append(btn)

standard_button = tk.Button(button_frame, text=language_texts["standard"], font=("Verdana", 14), command=lambda: switch_to_standard())
standard_button.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

scientific_button = tk.Button(button_frame, text=language_texts["scientific"], font=("Verdana", 14), command=lambda: switch_to_scientific())
scientific_button.grid(row=6, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

theme_button = tk.Button(button_frame, text=language_texts["dark_mode"], font=("Verdana", 14), command=change_theme)
theme_button.grid(row=7, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

language_selector = tk.OptionMenu(button_frame, tk.StringVar(value="English"), "en", "tr", command=change_language)
language_selector.grid(row=8, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

load_history()
window.mainloop()
