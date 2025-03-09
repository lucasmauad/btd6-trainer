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

text1 = ttk.Label(frm, text="Choose the tower to upgrade:")
text1.grid(column=0, row=0, pady='5')
text2 = ttk.Label(frm, text="Press 'F12' to Start Trainer.\nPress 'F8' to Stop Trainer.\nPress 'F9' to End Trainer.")
text2.grid(column=0, row=1, pady='5')

combo_box = ttk.Combobox(frm, values = list(tower_dict.keys()), state = 'readonly')
combo_box.set('None')
combo_box.grid(column=2, row=0, pady='5')

def start_but():
    global text1
    
    value = tower_dict[combo_box.get()]
    
    if value == 0:
        text1.config(text='Starting without upgrading.')
    else:
        text1.config(text=f'Upgrading {combo_box.get()}.')
    
    print(f'Starting with {value}')
    start_bot(value)

ttk.Button(frm, text="Run", command=start_but).grid(column=2, row=1)

root.mainloop()