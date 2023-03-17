import tkinter
import customtkinter as ctk
import pyrebase
from tkinter import messagebox

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



def signup():
    name1 = name.get()
    depertment = dept.get()
    rollno= roll.get()
    email = username.get()
    passwd = password.get()
    if len(email) == 0 or len(passwd) == 0 or len(name1) == 0 or len(depertment) == 0 or len(rollno) == 0:
        messagebox.showerror(title="Sign Up",message="Plese Fill All Details")
    elif len(email) != 0 and len(passwd) != 0:   
        try:
            user = auth.create_user_with_email_and_password(email=email,password=passwd)
            messagebox.showinfo(title="Sign Up",message="Registration Succesful")
            data = {"Name":name1,"Depertment":depertment,"Roll Number":rollno,"Email":email,"Password":passwd}
            # db.child("User").child(user_id).push(data)
            db.child("User").push(data)
            print("Register Done")
            root.destroy()
        except:
            messagebox.showerror(title="Sign Up",message="Already Have A Account, Or Invalid Email")
            print("Already Have A Account")

if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    root.geometry("1050x1000")
    root.title("InteleSched")
    root1 = ctk.CTkFrame(root,height=800,
                            width=800,
                            corner_radius=20)
    root1.pack(pady=(20,0))  



    lable1 = ctk.CTkLabel(root1,text="Register",
                                font=ctk.CTkFont(size=60,weight="bold"))
    lable1.place(x=270,y=50)  


    lable2 = ctk.CTkLabel(root1,text="Name",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable2.place(x=110,y=155) 


    name = ctk.CTkEntry(root1,placeholder_text="Enter Name",
                                width=560,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    name.place(x=110,y=192)


    lable2 = ctk.CTkLabel(root1,text="Deperment",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable2.place(x=110,y=265) 


    dept = ctk.CTkEntry(root1,placeholder_text="Enter Deperment",
                                width=560,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    dept.place(x=110,y=302)

    lable3 = ctk.CTkLabel(root1,text="Roll Number",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable3.place(x=110,y=375) 
    roll = ctk.CTkEntry(root1,placeholder_text="Enter RollNumber",
                                width=560,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    roll.place(x=110,y=412)


    lable4 = ctk.CTkLabel(root1,text="Email",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable4.place(x=110,y=475) 
    username = ctk.CTkEntry(root1,placeholder_text="Enter Email",
                                width=560,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    username.place(x=110,y=512)


    lable5 = ctk.CTkLabel(root1,text="Password",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable5.place(x=110,y=580) 
    password = ctk.CTkEntry(root1,placeholder_text="Enter Password",
                                width=560,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    password.place(x=110,y=618)

    btn1 = ctk.CTkButton(root1,text="Register",
                            height=38,
                            font=ctk.CTkFont(weight="bold",size=18),
                            command=signup)
    btn1.place(x=320,y=710)







    root.mainloop()
