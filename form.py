import tkinter as tk
from PIL import ImageTk, Image
import os

window = tk.Tk()
window.title("Formularzyk")

label1 = tk.Label(window, text="Imie: ")
label1.grid(row = 0, column = 0, padx = 2, pady=2)

label2 = tk.Label(window, text="Nazwisko: ")
label2.grid(row = 1, column = 0, padx = 2, pady=2)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=2, pady=2)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=2, pady=2)

label3=  tk.Label(window, text="Płeć: ")
label3.grid(row = 2, column = 0, padx = 2, pady=2)

label4=  tk.Label(window, text="Wiek: ")
label4.grid(row = 3, column = 0, padx = 2, pady=2)

label5=  tk.Label(window, text="Województwo: ")
label5.grid(row = 4, column = 0, padx = 2, pady=2)

woj = ["dolnośląskie", "kujawsko-pomorskie","lubelskie", "lubuskie", "łódzkie","małopolskie","mazowieckie","opolskie","podkarpackie","podlaskie","pomorskie","śląskie","świętokrzyskie","warmińsko-mazurskie","wielkopolskie","zachodniopomorskie"]
woj_d = tk.StringVar(value=woj[0])
woj_menu = tk.OptionMenu(window, woj_d, *woj)
woj_menu.grid(row=4, column=1)

b1= tk.Button(window, text="Wyślij")
b1.grid(row=5, column=0)

def clearFunc():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    spin.delete(0, tk.END)
    woj_d.set(woj[0])
    radioValue.set(0)

b2= tk.Button(window, text="Reset", command=clearFunc)
b2.grid(row=5, column=1)

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
img_path = "img.jpg"
image = Image.open(img_path)
photo = ImageTk.PhotoImage(image)

label6 = tk.Label(window, compound=tk.RIGHT, image=photo)
label6.grid(row = 0, column = 2, padx = 2, pady=2)


def radioClicked():
    print(radioValue.get())

radioValue = tk.IntVar()
radio1 = tk.Radiobutton(window, text='M', variable=radioValue, value=1, command=radioClicked)
radio1.grid(row=2, column=1)

radio2 = tk.Radiobutton(window, text='K', variable=radioValue, value=2, command=radioClicked)
radio2.grid(row=2, column=2)

def spinValue():
    print(spin.get())


spin = tk.Spinbox(window, from_ = 13, to = 99, command=spinValue)
spin.grid(row=3, column=1)

window.geometry("800x650")


window.mainloop()