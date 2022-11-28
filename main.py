import tkinter as tk
from tkinter import ttk
from random import choice

lets = 'ABCDEF'
nums = '123456'

w = tk.Tk()
w.minsize(width=200, height=200)
w.title('map')
w.attributes("-fullscreen", 1)
w['bg'] = '#ffffff'

def random():
    let = choice(lets)
    num = choice(nums)
    rand_let['text']=let
    rand_num['text'] = num
    w.update_idletasks()

w.columnconfigure(0, weight=1)

rand_lab_st = ttk.Style()
rand_lab_st.configure('b.TLabel', font='Calibri 280', background='#ffffff', relief=tk.SOLID, width=3, anchor=tk.CENTER,
                      borderwidth=6)

rand_frame = tk.Frame(w, background='#ffffff')
rand_frame.grid(row=0, column=0, padx=30, pady=30)

rand_let = ttk.Label(rand_frame, text='A', style='b.TLabel')
rand_let.grid(row=0, column=0, pady=20, padx=20)

rand_num = ttk.Label(rand_frame, text='1', style='b.TLabel')
rand_num.grid(row=0, column=1, pady=20, padx=20)

rand_but_st = ttk.Style()
rand_but_st.configure('b.TButton', font='Calibri 80')

rand_but = ttk.Button(w, text='Random', style='b.TButton', command=random)
rand_but.grid(row=1, column=0, pady=40, padx=20)

w.mainloop()
