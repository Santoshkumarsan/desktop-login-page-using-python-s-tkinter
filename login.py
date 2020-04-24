from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1150x650+0+0")
        
    
        self.bg_icon=ImageTk.PhotoImage(file="images/1.jpg")
        self.user_icon=PhotoImage(file="images/user.png")
        self.pass_icon=PhotoImage(file="images/pass.png")
        self.logo_icon=ImageTk.PhotoImage(file="images/man-user.jpg")
        #=======variables========
        self.uname=StringVar()
        self.pass_=StringVar()

        Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="blue",fg="red",bd=15,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        login_Frame=Frame(self.root,bg="white")
        login_Frame.place(x=440,y=150)


        Label(login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        Label(login_Frame,text="username",image=self.user_icon,compound=LEFT,font=("title new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=0,pady=0)
        Entry(login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        Label(login_Frame,text="password",image=self.pass_icon,compound=LEFT,font=("title new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=0,pady=0)
        Entry(login_Frame,bd=5,relief=GROOVE,textvariable=self.pass_,font=("",15)).grid(row=2,column=1,pady=20)


        Button(login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.uname.get()=="santosh" and self.pass_.get()=="12345":
            messagebox.showinfo("successfull",f"welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error","invalid username or password")
            
            
root=Tk()
obj=Login_system(root)
root.mainloop()