from tkinter import *

my__window=Tk()
my__window.geometry('500x500')

topFrame=Frame(my__window)
bottomFrame=Frame(my__window)

topFrame.pack()
#bottomFrame.pack(side=BOTTOM)
bottomFrame.pack()

Button(topFrame,text='Button 1').grid(row=0, column=0)
Button(topFrame,text='Button 2').grid(row=0, column=1)
Button(topFrame,text='Button 3').grid(row=0, column=2)

Button(bottomFrame,text='Button 4').pack()
Button(bottomFrame,text='Button 5').pack()
Button(bottomFrame,text='Button 6').pack()

my__window.mainloop()