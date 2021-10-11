import tkinter

root=tkinter.Tk()
Firstframe=tkinter.Frame(root)
Firstframe.pack()

Secondframe=tkinter.Frame(root)
Secondframe.pack()

btn1=tkinter.Button(Firstframe,text="Button 1")
btn1.pack(side=tkinter.LEFT)

btn2=tkinter.Button(Firstframe,text="Button 2")
btn2.pack(side=tkinter.LEFT)

btn3=tkinter.Button(Secondframe,text="Button 3")
btn3.pack(side=tkinter.BOTTOM)

root.mainloop()