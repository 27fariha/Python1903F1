import tkinter

def ShowValuesM():
    print("Male : %s"%(vargender.get()))
    
def ShowValuesF():
    print("Female : %s"%(vargender.get()))

root=tkinter.Tk()

vargender=tkinter.StringVar()
vargender.set(0)

tkinter.Label(root,text="Select your gender").pack()

tkinter.Radiobutton(root,text="Male",padx=20,variable=vargender,value=1,command=ShowValuesM).pack(anchor=tkinter.W)
tkinter.Radiobutton(root,text="Female",padx=20,variable=vargender,value=2,command=ShowValuesF).pack(anchor=tkinter.W)


root.mainloop()