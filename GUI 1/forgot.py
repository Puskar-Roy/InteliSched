import customtkinter as ctk
import pyrebase
import tkinter
from tkinter import messagebox
import subprocess

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
            subprocess.run(["python3","register.py"])


 
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Forgot Password")
    root.geometry("700x650")
    root.minsize(700,650)
    root.maxsize(700,650)

    root1 = ctk.CTkFrame(root,height=400,width=600,corner_radius=20)
    root1.pack(pady=(60,0))

    lable1 = ctk.CTkLabel(root1,text="Forgot Password",
                                font=ctk.CTkFont(size=50,weight="bold"))
    lable1.place(x=92,y=70) 


    lable2 = ctk.CTkLabel(root1,text="Email",
                                font=ctk.CTkFont(size=20,weight="bold"))
    lable2.place(x=105,y=170)



    usernameFor = ctk.CTkEntry(root1,placeholder_text="Enter Email",
                                width=400,
                                height=50,
                                font=ctk.CTkFont(size=20,weight="bold"),
                                border_color="#3468c9",
                                corner_radius=15)
    usernameFor.place(x=100,y=202)


    btn1 = ctk.CTkButton(root1,text="Get OTP",
                            height=38,
                            font=ctk.CTkFont(weight="bold",size=18),
                            command=get_otp)
    btn1.place(x=225,y=290)





    root.mainloop()
  