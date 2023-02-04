import csv
import os
from tkinter import messagebox, END, Tk, Label, Entry, Button, StringVar, OptionMenu

from datetime import datetime
from translate import Translator

window = Tk()
window.title("Google translator")
window.geometry("700x350")
window.configure(bg="black")


def translate():
    trans_ = entry3.get()
    trans = options[trans_]
    translator = Translator(to_lang=trans)
    text = entry1.get()
    translation = translator.translate(text)
    res_label = Label(window, width=25, text=translation)
    res_label.place(x=400, y=100)
    sentence = {
        "From language": "English",
        "Text": text,
        "TO language": trans_,
        "Result": translation,
        "Date": datetime.now()

    }

    with open("translate.csv", "a", encoding="utf_8_sig") as file:
        header = ["From language", "Text", "TO language", "Result", "Date"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("sentence.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerow(sentence)
        messagebox.showinfo("Information", "Saved successfully")


def clear():
    entry1.delete(0, END)
    entry2.set("English")
    entry3.set("Uzbek")
    res_label = Label(window, width=20, text="")
    res_label.place(x=200, y=200)


langueage_label = Label(window, text="Translator", font=25, bg="blue", fg="cyan")
langueage_label.place(x=270, y=10)

# Dropdown menu options
options = {
    "English": "en",
    "Russian": "ru",
    "Arabic": "ar",
    "Korean": "ko",
    "Turkish": "tr",
    "Uzbek": "uz",

}
opt = list(options.keys())

# datatype of menu text
entry2 = StringVar()

# Initial menu text
entry2.set("English")

# Create Dropdown menu
drop1 = OptionMenu(window, entry2, *opt)
drop1.config(borderwidth=8, width=20)
drop1.place(x=50, y=50)
entry1 = Entry(window, width=20)
entry1.config(borderwidth=8)
entry1.place(x=70, y=100)

tr_label = Label(window, text="----", font=14, width=10, bg="blue")
tr_label.place(x=270, y=100)

result_btn = Button(window, text="Translate", width=10, height=2, bg="gray", fg="green", command=translate)
result_btn.place(x=280, y=150)

clear_btn = Button(window, text="clear", width=10, height=2, bg="gray", fg="green", command=clear)
clear_btn.place(x=280, y=200)

entry3 = StringVar()
entry3.set("Uzbek")

drop2 = OptionMenu(window, entry3, *opt)
drop2.config(borderwidth=8, width=20)
drop2.place(x=400, y=50)

if __name__ == "__main__":
    window.mainloop()
