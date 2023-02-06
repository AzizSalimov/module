from tkinter import *
import json
import requests

KEY = 'gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR'
url = f"https://api.freecurrencyapi.com/v1/latest?apikey=gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR"

resp = requests.get(url)

window = Tk()
window.title('Valyuta')
window.config(bg='#111111')
window.geometry('600x500')

nam_ = StringVar()
nam = StringVar()

with open('latest (1).json') as f:
    chose = json.load(f)



def valuta():
    get = nam.get()
    get_ = chose.get(get)
    get__ = var1.get()
    get__ = int(get__)
    all = get__ * get_
    all = str(all)
    var2.set(all)

def exitt():
    window.destroy()


menu = OptionMenu(window, nam_, *chose).place(x=70, y=60, width=140)
nam_.set('USD')
menu2 = OptionMenu(window, nam_, *chose).place(x=300, y=60, width=140)
var1 = StringVar()
name = Entry(window, textvariable=var1, width=22)
name.place(x=70, y=100)

var2 = StringVar()
name2 = Entry(window, textvariable=var2, width=22).place(x=300, y=100)

ad_btn = Button(window, text='↞↠', width=10, command=valuta).place(x=220, y=70)
exiT_bt = Button(window, text='Exit', command=exitt).place(x=250, y=100)

window.mainloop()
