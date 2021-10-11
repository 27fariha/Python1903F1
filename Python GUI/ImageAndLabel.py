import tkinter 
root =tkinter.Tk()
image1 = tkinter.PhotoImage(file="C:/Users/farihaahmed/Desktop/BS/logo.png")
text1 = "This is sample text for testing"
w1=tkinter.Label(root,image=image1,bd=50,relief=tkinter.RIDGE)
w2=tkinter.Label(root,padx=10,justify=tkinter.LEFT,text=text1,font= ("Helvetica 10"),fg="red",bd=4,bg="blue")
w1.pack(side="right")
w2.pack(side="left")
root.mainloop()
