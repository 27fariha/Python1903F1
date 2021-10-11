import tkinter

def ShowValues():
    print("Yes : %d \n No: %d"%(varYes.get(),varNo.get()))


root=tkinter.Tk()
varYes=tkinter.IntVar()
tkinter.Checkbutton(root,text="Yes",variable=varYes).grid(row=0,sticky=tkinter.W)

varNo=tkinter.IntVar()
tkinter.Checkbutton(root,text="No",variable=varNo).grid(row=1, sticky=tkinter.W)

tkinter.Button(root,text="Show",command=ShowValues).grid(row=2)
tkinter.Button(root,text="Quit",command=root.quit).grid(row=3)
root.mainloop()