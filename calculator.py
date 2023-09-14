import tkinter
import customtkinter
import tkinter.messagebox

customtkinter.set_appearance_mode("windowtem")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.geometry("310x470")
window.title("Calculator")

screen = customtkinter.CTkEntry(window, width=290, height=50,)
screen.pack(padx=10, pady=10)
screen.place(x=10, y=25)

def insert(no):
    screen.insert(customtkinter.END, no)

def clear():
    screen.delete(0, customtkinter.END)

def result():
    try:
        x = str(eval(screen.get()))
        screen.delete(0, customtkinter.END)
        screen.insert(0, x)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

btn = customtkinter.CTkButton(window, width=90, height=50, text=1, command=lambda: insert(1))
btn.place(x=10, y=100)
btn2 = customtkinter.CTkButton(window, width=90, height=50, text=2, command=lambda: insert(2))
btn2.place(x=110, y=100)
btn3 = customtkinter.CTkButton(window, width=90, height=50, text=3, command=lambda: insert(3))
btn3.place(x=210, y=100)
btn4 = customtkinter.CTkButton(window, width=90, height=50, text=4, command=lambda: insert(4))
btn4.place(x=10, y=160)
btn5 = customtkinter.CTkButton(window, width=90, height=50, text=5, command=lambda: insert(5))
btn5.place(x=110, y=160)
btn6 = customtkinter.CTkButton(window, width=90, height=50, text=6, command=lambda: insert(6))
btn6.place(x=210, y=160)
btn7 = customtkinter.CTkButton(window, width=90, height=50, text=7, command=lambda: insert(7))
btn7.place(x=10, y=220)
btn8 = customtkinter.CTkButton(window, width=90, height=50, text=8, command=lambda: insert(8))
btn8.place(x=110, y=220)
btn9 = customtkinter.CTkButton(window, width=90, height=50, text=9, command=lambda: insert(9))
btn9.place(x=210, y=220)
btn0 = customtkinter.CTkButton(window, width=90, height=50, text=0, command=lambda: insert(0))
btn0.place(x=110, y=280)

sum = customtkinter.CTkButton(window, width=90, height=50, text='+', command=lambda: insert('+'))
sum.place(x=10, y=340)
sub = customtkinter.CTkButton(window, width=90, height=50, text='-', command=lambda: insert('-'))
sub.place(x=110, y=340)
clr = customtkinter.CTkButton(window, width=90, height=50, text='X', command=lambda: clear())
clr.place(x=210, y=340)
mul = customtkinter.CTkButton(window, width=90, height=50, text='*', command=lambda: insert('*'))
mul.place(x=10, y=400)
div = customtkinter.CTkButton(window, width=90, height=50, text='/', command=lambda: insert('/'))
div.place(x=110, y=400)
res = customtkinter.CTkButton(window, width=90, height=50, text='=', command=lambda: result())
res.place(x=210, y=400)

window.mainloop()