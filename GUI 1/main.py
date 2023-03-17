import tkinter
import customtkinter as ctk
import pyrebase
import subprocess
from tkinter import messagebox


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

firebaseConfig = {
    'apiKey': "AIzaSyBC8LtuaA-hYafFeK-22bKm0K2kmT0yNXo",
    'authDomain': "intellisched-1de1e.firebaseapp.com",
    'projectId': "intellisched-1de1e",
    'databaseURL':"https://intellisched-1de1e-default-rtdb.firebaseio.com/",
    'storageBucket': "intellisched-1de1e.appspot.com",
    'messagingSenderId': "656618374988",
    'appId': "1:656618374988:web:3321d6f80fff66a79871e9",
    'measurementId': "G-DMWX90RRYJ"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()



def main_screen():
    root = ctk.CTk()
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    root.geometry("1250x700")
    root.minsize(1250,700)
    root.maxsize(1250,700)
    root.title("InteleSched | Home")

    root1 = ctk.CTkFrame(root,height=700,width=300)
    root1.grid(row=0, sticky=ctk.NSEW)
    

    root.mainloop()



def handle_user_details(email):
    user_data1 = db.child("User").order_by_child("Email").equal_to(email).get()
    name = []
    roll = []
    dept = []
    for people in user_data1.each():
        name.append(people.val()["Name"])
        roll.append(people.val()["Roll Number"])
        dept.append(people.val()["Depertment"])

    root = ctk.CTk()
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    root.geometry("1250x700")
    root.minsize(1250,700)
    root.maxsize(1250,700)
    root.title("InteleSched | Home")

    root1 = ctk.CTkFrame(root,height=700,width=300)
    root1.grid(row=0, sticky=ctk.NSEW)

    label = ctk.CTkLabel(root,
                         text= "Name - " + name[0],
                         font=ctk.CTkFont(size=30,
                         weight="bold"))
    label.place(x=400,y=20)

    labe2 = ctk.CTkLabel(root,
                         text= "Branch - "+ dept[0],
                         font=ctk.CTkFont(size=30,
                        weight="bold"))
    labe2.place(x=400,y=60)

    labe3 = ctk.CTkLabel(root,
                         text= "Roll Number  - " + roll[0],
                         font=ctk.CTkFont(size=30,
                        weight="bold"))
    labe3.place(x=400,y=100)

    root.mainloop()
    

       
     



def login():
    email = username.get()
    passwd = password.get()
    if len(email) == 0 and len(passwd) == 0:
        messagebox.showerror(title="Sign Up",message="Plese Enter Email And Password")
    elif len(email) != 0 and len(passwd) != 0:
        try:
            Login = auth.sign_in_with_email_and_password(email, passwd)
            messagebox.showinfo(title="Log In",message="Log In Succesful")
            root.destroy()
            print("Log In")
            handle_user_details(email)
        except:
            messagebox.showerror(title="Log In",message="Invalid Email Or Password")
            print("Didnt Get Any Data")    
    return  


def go_to_signup(event):
    subprocess.run(["python3","register.py"])

def forgot_pass(event):
    subprocess.run(["python3","forgot.py"])

if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    root.geometry("950x950")
    root.title("InteleSched")
    root1 = ctk.CTkFrame(root,height=750,
                            width=800,
                            corner_radius=20)
    root1.pack(pady=(45,0))



    lable1 = ctk.CTkLabel(root1,text="Log In",
                                font=ctk.CTkFont(size=60,weight="bold"))
    lable1.place(x=310,y=70)    


    lable1 = ctk.CTkLabel(root1,text="Select User Type ",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable1.place(x=110,y=215) 


    optionmenu_1 = ctk.CTkOptionMenu(root1,dynamic_resizing=False,
                                            values=["Admin","Teacher", "Student"],
                                            width=560,
                                            height=40,
                                            dropdown_hover_color="#2f4978",
                                            font=ctk.CTkFont(size=20,weight="bold"),
                                            dropdown_font=ctk.CTkFont(size=20,weight="bold"))
    optionmenu_1.place(x=110,y=250)


    lable2 = ctk.CTkLabel(root1,text="Username",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable2.place(x=110,y=325) 


    username = ctk.CTkEntry(root1,placeholder_text="Enter Email",
                                width=560,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    username.place(x=110,y=362)


    lable3 = ctk.CTkLabel(root1,text="Password",
                                font=ctk.CTkFont(size=20,weight="bold"),
                                )
    lable3.place(x=110,y=442)


    password = ctk.CTkEntry(root1,placeholder_text="Enter Password",
                                width=560,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    password.place(x=110,y=480)


    lable4 = ctk.CTkLabel(root1,text="Forgot Password?",
                                font=ctk.CTkFont(size=20,weight="bold"),
                                )
    lable4.place(x=490,y=540)
    lable4.bind("<Button-1>",forgot_pass)


    btn1 = ctk.CTkButton(root1,text="Log In",
                            height=38,
                            font=ctk.CTkFont(weight="bold",size=18),
                            command=login)
    btn1.place(x=320,y=600)

    lable5 = ctk.CTkLabel(root1,text="Don't Have a Accout? Register Now",
                                font=ctk.CTkFont(size=20,weight="bold"),
                                )
    lable5.place(x=210,y=690)
    lable5.bind("<Button-1>",go_to_signup)


    root.mainloop()