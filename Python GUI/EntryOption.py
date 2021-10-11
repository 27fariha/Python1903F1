import tkinter
def showName():
    text1=tkinter.Label(root,text="FirstName =%s LastName =%s"%(input1.get(),input2.get()))
    text1.pack()
    print("FirstName =%s LastName =%s"%(input1.get(),input2.get()))
    




root=tkinter.Tk()
fname=tkinter.Label(root,text="Enter First Name")
fname.pack()
lname=tkinter.Label(root,text="Enter Last Name")
lname.pack()
input1=tkinter.Entry(root)
input1.pack()
input2=tkinter.Entry(root)
input2.pack()
btn1=tkinter.Button(root,text="Quit", command=root.quit)
btn1.pack()
btn2=tkinter.Button(root,text="Show",command=showName)
btn2.pack()
root.mainloop()