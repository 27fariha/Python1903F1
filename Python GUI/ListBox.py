import tkinter

root=tkinter.Tk()

listBox=tkinter.Listbox(root)
for op in ["A","B","C","D","E","F"]:
    listBox.insert(tkinter.END,op)

listBox.pack()
root.mainloop()