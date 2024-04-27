# This demonstration should result in a simple Tkinter window with a button specifically for opening new Tkinter windows.
import tkinter

root = tkinter.Tk()

def newWindow():
  rootN = tkinter.Tk()
  rootN.mainloop()

button = tkinter.Button(root, text="New Window", command=newWindow)
button.pack()
root.mainloop()
