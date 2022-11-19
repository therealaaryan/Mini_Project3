from tkinter import *
import Code_5thSem as csem

root = Tk()
root.geometry("700x350")
root.title("Speech to Text")

try:
    myLabel2 = Label(root, text="{}".format(csem.text), font=('Times', 24)).grid(row=1, column=0)
except:
    myLabel3 = Label(root, text="Couldn't recognize your speech!", font=('Times', 24)).grid(row=1, column=0)

root.mainloop()