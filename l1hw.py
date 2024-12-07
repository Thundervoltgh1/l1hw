from tkinter import*
root=Tk()
root.geometry('100x100')
root.title("WELCOME TO TKINTER")
btn=Button(root,text="CLICK ME!!!",bd="7",background="Orange",command=root.destroy)
btn.pack(side="top")
root.mainloop()
