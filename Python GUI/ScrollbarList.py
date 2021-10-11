import tkinter

root=tkinter.Tk()
sbar=tkinter.Scrollbar(root)
sbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

lbox=tkinter.Listbox(root,yscrollcommand=sbar.set)
for op in range(100):
    lbox.insert(tkinter.END,str(op))
lbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH)


sbar.config(command=lbox.yview)
root.mainloop()