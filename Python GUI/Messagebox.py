import tkinter
root=tkinter.Tk()
msg="Install Pillow Package or PIL in the local machine.Open the Image using Open(image_location) method.Resize the given image using resize((w,h), Image"
w1=tkinter.Message(root,text=msg)
w1.config(bg="red",font=('times',14,'italic'))
w1.pack()
root.mainloop()