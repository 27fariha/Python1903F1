import tkinter
def showName():
    text1=tkinter.Label(root,text="FirstName =%s LastName =%s"%(input1.get(),input2.get()))
    text1.grid(row=4)
    print("FirstName =%s LastName =%s"%(input1.get(),input2.get()))
    

root=tkinter.Tk()
tkinter.Label(root,text="Enter First Name").grid(row=0)

tkinter.Label(root,text="Enter Last Name").grid(row=1,pady=15)

input1=tkinter.Entry(root)
input1.grid(row=0,column=1)

input2=tkinter.Entry(root)
input2.grid(row=1,column=1,pady=15)

tkinter.Button(root,text="Quit", command=root.quit).grid(row=3,column=0,sticky=tkinter.W,pady=30,padx=30)

tkinter.Button(root,text="Show",command=showName).grid(row=3,column=1,sticky=tkinter.W,pady=30,padx=30)

root.mainloop()