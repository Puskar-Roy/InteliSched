import customtkinter as ctk
from time import strftime
import subprocess
import pyrebase
from tkinter import *
from tkinter import messagebox
from a_admin_panel import handel_admin_details
from b_faculty_panel import handel_faculty_details
from c_student_panel import handel_student_details
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase_clouddb.json")
app = firebase_admin.initialize_app(cred,name="login")
db = firestore.client(app=app) #for cloud firestore




# firebaseConfig = {
#     'apiKey': "AIzaSyBC8LtuaA-hYafFeK-22bKm0K2kmT0yNXo",
#     'authDomain': "intellisched-1de1e.firebaseapp.com",
#     'projectId': "intellisched-1de1e",
#     'databaseURL':"https://intellisched-1de1e-default-rtdb.firebaseio.com/",
#     'storageBucket': "intellisched-1de1e.appspot.com",
#     'messagingSenderId': "656618374988",
#     'appId': "1:656618374988:web:3321d6f80fff66a79871e9",
#     'measurementId': "G-DMWX90RRYJ"
# }

firebaseConfig = {
  'apiKey': "AIzaSyDlwmXi6-Y8fPhURBAdJybXlJuSbvew-PE",
  'authDomain': "formintellisched.firebaseapp.com",
  'databaseURL': "https://formintellisched-default-rtdb.firebaseio.com",
  'projectId': "formintellisched",
  'storageBucket': "formintellisched.appspot.com",
  'messagingSenderId': "725143468756",
  'appId': "1:725143468756:web:920f84d70991093482d941",
  'measurementId': "G-SNSBZJ54Q2"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
# db = firebase.database() # this is for real time data base



def forgot_pass(event):
        def get_otp():
            emailvar = usernameFor.get()
            if len(emailvar) == 0:
                messagebox.showwarning(title="Invalid Email", message="Plese Enter a Email")
                print("Plese Enter a Email")
            elif len(emailvar) != 0:
                try:
                    auth.send_password_reset_email(emailvar)
                    messagebox.showinfo(title="Forgot Password",message=f"In {emailvar} We'll Sent A Reset Password Link")
                    root.destroy()
                except:
                    messagebox.showerror(title="Invalid User",message=f"Did'nt Found Any Account {emailvar},At First Register Yourself")
                    root.destroy()

    
        root = ctk.CTk()
        root.title("Forgot Password")
        root.minsize(640,495)
        root.maxsize(640,495)

        root1 = ctk.CTkFrame(root,height=350,width=500,corner_radius=20)
        root1.pack(pady=(60,0))

        lable1 = ctk.CTkLabel(root1,text="Forgot Password",
                                    font=ctk.CTkFont(size=35,weight="bold",family="Verdana"))
        lable1.place(x=82,y=50) 


        lable2 = ctk.CTkLabel(root1,text="Email",
                                    font=ctk.CTkFont(size=20,weight="bold"))
        lable2.place(x=80,y=135)
        usernameFor = ctk.CTkEntry(root1,placeholder_text="Enter Email",
                                    width=360,
                                    height=45,
                                    font=ctk.CTkFont(size=19,weight="bold"),
                                    border_color="#3468c9",
                                    corner_radius=20)
        usernameFor.place(x=70,y=169)
        btn1 = ctk.CTkButton(root1,text="Get Email",
                                height=38,
                                font=ctk.CTkFont(weight="bold",size=18),
                                command=get_otp,
                                corner_radius=20)
        btn1.place(x=275,y=235)
        root.mainloop()
    





def login():
    email = username.get()
    passwd = password.get()
    if len(email) == 0 and len(passwd) == 0:
        messagebox.showerror(title="Sign Up",message="Plese Enter Email And Password")
    elif len(email) != 0 and len(passwd) != 0:
        if (optionmenu_1.get() == "Student"):
            try:
                docs = db.collection("Student").where("Email","==",email).get()
                user_data = {}
                for doc in docs:
                    user_data = doc.to_dict()    

                if(user_data["Role"]!="Student"):
                    messagebox.showerror(title="Log In",message="Your Role Is Not Correct, Try Again")
                    root.destroy()
                    subprocess.run(["python3","d_login_page.py"])
                else:
                    auth.sign_in_with_email_and_password(email,passwd)  
                    db.collection("Student").document(user_data["Roll Number"]).update({"Password":passwd})
                    messagebox.showinfo(title="Log In",message="Login Successful")
                    root.destroy()
                    handel_student_details(user_data["Roll Number"])


            except:
                messagebox.showerror(title="Log In",message="Invalid Email Or Password, Try Again")
                print("Didnt Get Any Data") 
                root.destroy()
                subprocess.run(["python3","d_login_page.py"])
        elif (optionmenu_1.get() == "Faculty"):    #done 
            try:
                docs = db.collection("Faculties").where("Email","==",email).get()
                user_data = 0
                for doc in docs:
                    user_data = doc.to_dict() 

                if(user_data["Role"]!="Faculty"):
                    messagebox.showerror(title="Log In",message="Your Role Is Not Correct, Try Again")
                    root.destroy()
                    subprocess.run(["python3","d_login_page.py"])
                else:
                    auth.sign_in_with_email_and_password(email,passwd) 
                    db.collection("Faculties").document(user_data["Faculty Id"]).update({"Password":passwd})
                    messagebox.showinfo(title="Log In",message="Login Successful")
                    root.destroy()
                    handel_faculty_details(user_data["Faculty Id"])

            except:
                messagebox.showerror(title="Log In",message="Invalid Email Or Password, Try Again")
                print("Didnt Get Any Data") 
                root.destroy()
                # subprocess.run(["python3","d_login_page.py"])
        elif (optionmenu_1.get() == "Admin"):    #done 
            try:
                # result = db.collection("Admin").document(email).get()
                # user_data = 0
                # if result.exists:
                #     user_data = result.to_dict()
                # print(user_data)   
                docs = db.collection("Admin").where("Email","==",email).get()
                user_data = 0
                for doc in docs:
                    user_data = doc.to_dict()  

                if(user_data["Role"]!="Admin"):
                    messagebox.showerror(title="Log In",message="Your Role Is Not Correct, Try Again")
                    root.destroy()
                    subprocess.run(["python3","d_login_page.py"])
                else:
                    auth.sign_in_with_email_and_password(email,passwd)   
                    db.collection("Admin").document(user_data["Admin Id"]).update({"Password":passwd})
                    messagebox.showinfo(title="Log In",message="Login Successful")
                    root.destroy()
                    handel_admin_details(user_data["Admin Id"])

            except:
                messagebox.showerror(title="Log In",message="Invalid Email Or Password, Try Again")
                print("Didnt Get Any Data") 
                root.destroy()
                subprocess.run(["python3","d_login_page.py"])
                
        



if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    root.geometry("830x630")
    root.title("InteleSched")

    root1 = ctk.CTkFrame(root,height=500,
                                width=600,
                                corner_radius=20)
    root1.pack(pady=(55,0))

    img1 = PhotoImage(file="logo1 (1).png")
    label = ctk.CTkLabel(root1, image=img1,text="",height=10,width=10)
    label.place(x=27,y=25)




    def time():
        string = strftime('%H:%M:%S %p')
        mark.configure(text = string)
        mark.after(1000, time)


    mark = ctk.CTkLabel(root1, 
                font = ('calibri', 20, 'bold'))
    mark.place(x=470,y=46)
    time()




    label1 = ctk.CTkLabel(root1,text ="IntelliSched",
                        font=ctk.CTkFont(size=40,weight="bold",family="Verdana"))
    label1.place(x=85,y=25)



    label21 = ctk.CTkLabel(root1,text ="Select Role",
                        font=ctk.CTkFont(size=20,weight="bold",family="Helvetica"))
    label21.place(x=110,y=105)







    optionmenu_1 = ctk.CTkOptionMenu(root1,dynamic_resizing=False,
                                                values=["Admin","Faculty", "Student"],
                                                width=360,
                                                height=40,
                                                font=ctk.CTkFont(size=20,weight="bold",family="Helvetica"),
                                                dropdown_font=ctk.CTkFont(size=20,weight="bold"),
                                                corner_radius=20)
    optionmenu_1.place(x=110,y=140)








    lable2 = ctk.CTkLabel(root1,text="Email",
                                    font=ctk.CTkFont(size=20,weight="bold"))
    lable2.place(x=110,y=200) 


    username = ctk.CTkEntry(root1,placeholder_text="Enter Email",
                                    width=360,
                                    height=40,
                                    font=ctk.CTkFont(size=20,weight="bold"),
                                    border_color="#3468c9",
                                    corner_radius=20)
    username.place(x=110,y=235)


    lable3 = ctk.CTkLabel(root1,text="Password",
                                    font=ctk.CTkFont(size=20,weight="bold"),
                                    )
    lable3.place(x=110,y=302)


    password = ctk.CTkEntry(root1,placeholder_text="Enter Password",
                                    width=360,
                                    height=40,
                                    font=ctk.CTkFont(size=20,weight="bold"),
                                    border_color="#3468c9",
                                    corner_radius=20)
    password.place(x=110,y=335)


    btn = ctk.CTkButton(root1,text="Launch",
                                height=33,
                                font=ctk.CTkFont(weight="bold",size=18,family="Verdana"),
                                command=login,
                                corner_radius=18)
    btn.place(x=320,y=420)


    lable4 = ctk.CTkLabel(root1,text="Forgot Password?",
                                    font=ctk.CTkFont(size=12,weight="bold"),
                                    )
    lable4.place(x=350,y=390)
    lable4.bind("<Button-1>",forgot_pass)
    # home_btn3.bind("<Button-1>",xD)

    



    root.mainloop()
    



    