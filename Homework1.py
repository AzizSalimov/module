import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.geometry('500x450')
window.title('TUDU')
window.config(bg='#111111')


def aufgabe_dazu():
    aufgabe = aufgaben_eingabe.get()

    if aufgabe != '':
        if aufgabe == 'Topshiriq':
            messagebox.showwarning('Error', 'Please enter settings for the window to work')
        else:
            aufgaben_liste.insert(tk.END, aufgabe)
            aufgaben_eingabe.delete(0, 'end')
    else:
        messagebox.showwarning('Error', 'Pleace enter settings for the window to work')



def aufgabe_weg():
    aufgaben_liste.delete(tk.ANCHOR)

def eingabe_entrfernem(event, eingage):
    eingage.delete(0, tk.END)


frame = tk.Frame(window)
frame.pack(pady=10)


aufgaben_liste = tk.Listbox(frame, width=25, height=8, font=('Times, 10'),
                            fg='#464646', selectbackground='#333333', activestyle='none')
aufgaben_liste.pack(side=tk.LEFT, fill=tk.BOTH)

scroo_bar = tk.Scrollbar(frame)
scroo_bar.pack(side=tk.RIGHT, fill=tk.BOTH)


aufgaben_liste.config(yscrollcommand=scroo_bar.set)
scroo_bar.config(command=aufgaben_liste.yview)

aufgaben_eingabe = tk.Entry(window, font=('Times', 24))
aufgaben_eingabe.insert(0, '')
aufgaben_eingabe.bind('<Button-1>',lambda event: eingabe_entrfernem(event, aufgaben_liste))
aufgaben_eingabe.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

aufgaben_dazu_btn = tk.Button(button_frame, text='Vazifa bering', font=('Times', 14),
                              bg='green', fg='white', padx=20, pady=10, command=aufgabe_dazu)
aufgaben_dazu_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)



aufgaben_weg_btn = tk.Button(button_frame, text='Vazifani ochiring', font=('Times', 14),
                              bg='red', fg='white', padx=20, pady=10, command=aufgabe_weg)
aufgaben_weg_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
if __name__ == '__main__':
    window.mainloop()
