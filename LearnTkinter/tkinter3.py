import tkinter as tk

window = tk.Tk()
window.title('My windows')
window.geometry('400x400')

e = tk.Entry(window, show='*')
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=40, height=10, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=40, height=10, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
