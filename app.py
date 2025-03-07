from tkinter import *
from tkinter import ttk
from main import *


tower_dict = {'None':0,
        'Dart Monkey':1,
        'Dartling Gunner':2,
        'Ice Monkey':3,
        'Mortar Monkey':4,
        'Beast Handler':5,
        'Monkey Ace':6}

root = Tk()
root.title("Bloons TD6 Trainer")

frm = ttk.Frame(root)
frm.grid(padx=30, pady=30)

ttk.Label(frm, text="Choose the tower to upgrade:").grid(column=0, row=0, pady='5')

combo_box = ttk.Combobox(frm, values = list(tower_dict.keys()), state = 'readonly')
combo_box.set('None')
combo_box.grid(column=2, row=0, pady='5')

def start_but():
    value = tower_dict[combo_box.get()]
    print(f'Starting with {value}')
    start_bot(value)

ttk.Button(frm, text="Run", command=start_but).grid(column=2, row=1)

root.mainloop()