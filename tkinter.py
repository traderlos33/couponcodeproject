import tkinter as tk
import random
win = tk.Tk()
name_var=tk.StringVar()
name = name_var.get()


def test_button_click():

    print('The Code for this item is  STUDENT' + name + str(int(random.randrange(250,300))))

    name_var.set("")

name_entry = tk.Entry(win,textvariable = name_var, font=('calibre',10,'normal'))
my_button = tk.Button(win, text='Test Button',
                      command=test_button_click)
my_button.grid(column=0, row=0)
label_val = tk.IntVar()
my_Label = tk.Label(win, textvariable=label_val)
my_Label.grid(column=1, row=0)
win.mainloop()
