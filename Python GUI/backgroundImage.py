import tkinter 

#png - photoImage 
#jpeg,jpg - pip install pillow

root=tkinter.Tk()

root.geometry("500x500")

img = tkinter.PhotoImage(file="C:/Users/farihaahmed/Desktop/python/Python 1903F1/bg.png") #set background image
label=tkinter.Label(root,image=img)
label.place(x=0,y=0)

text=tkinter.Text(root,height=10,width=60)
text.place(x=30,y=50)

root.mainloop()