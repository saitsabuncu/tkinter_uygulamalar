from tkinter import *

# Pencere oluştur
my_window=Tk()
my_window.title("Toplama Uygulaması")
my_window.geometry("300x200")  # Pencere boyutu

# Toplama fonksiyonu
def total():
    try:
        toplam=int(number1.get())+int(number2.get())
        lbl_Sonuc.config(text=f"Sonuç: {toplam}")
        # Girişlerin arka planını temizle
        number1.config(bg="white")
        number2.config(bg="white")
    except ValueError:
        lbl_Sonuc.config(text='Hata: Geçerli bir tam sayı girin!')
        # Hatalı girişlerde arka planı renklendir
        number1.config(bg='lightcoral')
        number2.config(bg="lightcoral")

# Girişleri temizleme fonksiyonu
def temizle():
    number1.delete(0, END)
    number2.delete(0, END)
    lbl_Sonuc.config(text="")
    number1.config(bg="white")
    number2.config(bg="white")

# Etiketler
Label(my_window,text='Sayı 1').grid(row=0,column=0,padx=20,pady=10)
Label(my_window,text='Sayı 2').grid(row=1,column=0)

# Giriş kutuları
number1=Entry(my_window)
number2=Entry(my_window)
number1.grid(row=0,column=1,padx=20)
number2.grid(row=1,column=1)

#Topla butonu
Button(my_window,text='Topla',command=total).grid(row=2,column=1,sticky='w',padx=20)

# Temizle butonu
Button(my_window, text='Temizle', command=temizle).grid(row=2, column=1)

# Sonuç etiketi
lbl_Sonuc=Label(my_window)
lbl_Sonuc.grid(row=3,column=1,sticky='w',padx=20)

# Tkinter döngüsü
my_window.mainloop()