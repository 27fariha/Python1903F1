import tkinter

root=tkinter.Tk(className="My Program")

tkinter.Label(root,text="some text here").pack()
root.geometry("600x400") #set screen width,lenght

#root.configure(background="Yellow") #set background color

#root['bg']="#ffb3b3"  #set color with hexa code
root['bg']="blue"

root.mainloop()