import tkinter
import customtkinter as ctk
import pyrebase
import subprocess
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

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")



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
    def delete_page():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def home_page(event):
        delete_page()
        frame1 = ctk.CTkFrame(main_frame,width=1100,height=750)
        lable= ctk.CTkLabel(frame1,text="Student Details",
                            font=ctk.CTkFont(weight="bold",size=40))
        lable.place(x=440,y=20)

        lable1 = ctk.CTkLabel(frame1,text="Name : "+name[0],
                            font=ctk.CTkFont(weight="bold",size=25))
        lable1.place(x=100,y=150)
        lable2 = ctk.CTkLabel(frame1,text="Roll Number : "+roll[0],
                            font=ctk.CTkFont(weight="bold",size=25))
        lable2.place(x=100,y=200)

        lable3 = ctk.CTkLabel(frame1,text="Section : ",
                            font=ctk.CTkFont(weight="bold",size=25))
        lable3.place(x=100,y=250)

        lable4 = ctk.CTkLabel(frame1,text="Depertment : "+dept[0],
                            font=ctk.CTkFont(weight="bold",size=25))
        lable4.place(x=100,y=300)

        lable5 = ctk.CTkLabel(frame1,text="Caste : ",
                            font=ctk.CTkFont(weight="bold",size=25))
        lable5.place(x=100,y=350)

        lable6 = ctk.CTkLabel(frame1,text="Adress : ",
                            font=ctk.CTkFont(weight="bold",size=25))
        lable6.place(x=100,y=400)

        frame1.pack(pady=20)

    def stu_page(event):
        delete_page()
        frame1 = ctk.CTkFrame(main_frame,width=1100,height=750)

        l1 =ctk.CTkLabel(frame1,text="konichiba")
        l1.place(x=30)
        frame1.pack(pady=20)

    root = ctk.CTk()
    root.geometry("1400x750")
    root.minsize(width=1400,height = 750)
    root.maxsize(width=1400,height = 750)
    root.title("InteliSched")

    option_frame = ctk.CTkFrame(root,border_color="#101B46")


    home_btn = ctk.CTkLabel(option_frame,text="Student Details",
                            font=ctk.CTkFont(weight="bold",size=25),
                            corner_radius=25,width=250)
    home_btn.place(y=40)
    home_btn.bind("<Button-1>",home_page)


    home_btn1 = ctk.CTkLabel(option_frame,text="Edite Info",
                            font=ctk.CTkFont(weight="bold",size=25),
                            corner_radius=25,width=250)
    home_btn1.place(y=100)
    home_btn1.bind("<Button-1>",stu_page)


    home_btn2  = ctk.CTkLabel(option_frame,text="View Schedule",
                            font=ctk.CTkFont(weight="bold",size=25),
                            corner_radius=25,width=250)
    home_btn2.place(y=160)

    home_btn3 = ctk.CTkLabel(option_frame,text="View Notice",
                            font=ctk.CTkFont(weight="bold",size=25),
                            corner_radius=25,width=250)
    home_btn3.place(y=220)

    home_btn4 = ctk.CTkButton(option_frame,text="Log Out",
                            font=ctk.CTkFont(weight="bold",size=20),
                            corner_radius=5,width=250)
    home_btn4.place(y=280)


    option_frame.pack(side=ctk.LEFT)
    option_frame.configure(width=250,height = 750)


    main_frame = ctk.CTkFrame(root,bg_color="#333740")
    main_frame.pack(side=ctk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(width=1150,height=750)





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