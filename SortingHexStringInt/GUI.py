from tkinter import *


window = Tk()

window.title("Hello")
window.geometry('500x300')
text = Text(window)
text.insert(END, "Hello")
text.grid(column=2, row=0)
ent = Entry(window,width=10)
ent.grid(column=0, row=0)
def clicked():
    res = '\n' + ent.get()
    text.insert(END, res)

    # btn.destroy()

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()