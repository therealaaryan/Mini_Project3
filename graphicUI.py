from tkinter import *
import Code_5thSem as csem

root = Tk()

myLabel1 = Label(root, text = "Listening...")
myLabel2 = Label(root, text="You said: {}".format(csem.text))

myLabel1.pack()
myLabel2.pack()

root.mainloop()