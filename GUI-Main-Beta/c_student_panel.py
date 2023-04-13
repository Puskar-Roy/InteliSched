import customtkinter as ctk
from time import strftime
import subprocess
import pyrebase
from tkinter import messagebox
from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from g_sched import sched

# cred = credentials.Certificate("firebase_clouddb.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client() #for cloud firestore


cred = credentials.Certificate("firebase_clouddb.json")
app = firebase_admin.initialize_app(cred,name="student")
db = firestore.client(app=app) #for cloud firestore


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

# result = db.collection("Student").document().get()
# user_data = 0
# if result.exists:
#     user_data = result.to_dict()


def handel_student_details(db_id):
    result = db.collection("Student").document(db_id).get()
    user_data = 0
    if result.exists:
        user_data = result.to_dict()
        
    def delete_page():
            for frame in main_frame.winfo_children():
                frame.destroy()

# =======================================================================Notice Page

    def xD(event):
            delete_page()
            frame1 = ctk.CTkFrame(main_frame,width=1100,height=750)



            img1 = PhotoImage(file="logo1 (1).png")
            label = ctk.CTkLabel(frame1, image=img1,text="",height=10,width=10)
            label.place(x=35,y=16)



            def time():
                string = strftime('%H:%M:%S %p')
                mark.configure(text = string)
                mark.after(1000, time)


            mark = ctk.CTkLabel(frame1, 
                        font = ('calibri', 20, 'bold'))
            mark.place(x=910,y=16)
            time()


            lablex= ctk.CTkLabel(frame1,text="Welcome",
                                font=ctk.CTkFont(weight="bold",size=40,family="Verdana"))
            lablex.place(x=100,y=15)

            labley= ctk.CTkLabel(frame1,text=user_data["Name"],
                                font=ctk.CTkFont(weight="bold",size=27,family="Helvetica"))
            labley.place(x=30,y=70)





            lable= ctk.CTkLabel(frame1,text="Notice Board",
                                font=ctk.CTkFont(weight="bold",size=35))
            lable.place(x=445,y=160)
            frame1.pack(pady=20)

    def log_out():
            response = messagebox.askyesno(title="Log Out",message="Confirm Exit?")
            if response == True:
                root.destroy()
            else:
                None

            subprocess.run(["python3","d_login_page.py"])    
# ========================================================================================================Deatails Page
                
    def home_page(event):
            delete_page()
            frame1 = ctk.CTkFrame(main_frame,width=1100,height=750)


            img1 = PhotoImage(file="logo1 (1).png")
            label = ctk.CTkLabel(frame1, image=img1,text="",height=10,width=10)
            label.place(x=35,y=16)



            def time():
                string = strftime('%H:%M:%S %p')
                mark.configure(text = string)
                mark.after(1000, time)


            mark = ctk.CTkLabel(frame1, 
                        font = ('calibri', 20, 'bold'))
            mark.place(x=910,y=16)
            time()


            lablex= ctk.CTkLabel(frame1,text="Welcome",
                                font=ctk.CTkFont(weight="bold",size=40,family="Verdana"))
            lablex.place(x=100,y=15)

            labley= ctk.CTkLabel(frame1,text=user_data["Name"],
                                font=ctk.CTkFont(weight="bold",size=27,family="Helvetica"))
            labley.place(x=30,y=70)


            lable= ctk.CTkLabel(frame1,text="Student Details",
                                font=ctk.CTkFont(weight="bold",size=35,family="Verdana"))
            lable.place(x=405,y=140)


            lable1 = ctk.CTkLabel(frame1,text="Name : "+user_data["Name"],
                                font=ctk.CTkFont(weight="bold",size=25,family="Helvetica"))
            lable1.place(x=40,y=240)
            # roll = user_data["Roll Number"] if roll store in db with int format then convert it into str
            # # roll1 = str(roll)
            
            lable2 = ctk.CTkLabel(frame1,text="Roll Number : "+ user_data["Roll Number"],
                                font=ctk.CTkFont(weight="bold",size=25,family="Helvetica"))
            lable2.place(x=550,y=240)

            lable3 = ctk.CTkLabel(frame1,text="Role : "+user_data["Role"],
                                font=ctk.CTkFont(weight="bold",size=25,family="Helvetica"))
            lable3.place(x=40,y=315)

            lable4 = ctk.CTkLabel(frame1,text="Depertment : "+user_data["Depertment"],
                                font=ctk.CTkFont(weight="bold",size=25,family="Helvetica"))
            lable4.place(x=550,y=315)

            lable6 = ctk.CTkLabel(frame1,text="Email : "+user_data["Email"],
                                font=ctk.CTkFont(weight="bold",size=25,family="Helvetica"))
            lable6.place(x=40,y=395)

            frame1.pack(pady=20)



    # ---------------------------------------------------------------------------------

    def sched_page(event):
            delete_page()
            frame1 = ctk.CTkFrame(main_frame,width=1100,height=750)


            img1 = PhotoImage(file="logo1 (1).png")
            label = ctk.CTkLabel(frame1, image=img1,text="",height=10,width=10)
            label.place(x=35,y=16)



            def time():
                string = strftime('%H:%M:%S %p')
                mark.configure(text = string)
                mark.after(1000, time)


            mark = ctk.CTkLabel(frame1, 
                        font = ('calibri', 20, 'bold'))
            mark.place(x=910,y=16)
            time()


            lablex= ctk.CTkLabel(frame1,text="Welcome",
                                font=ctk.CTkFont(weight="bold",size=40,family="Verdana"))
            lablex.place(x=100,y=15)

            labley= ctk.CTkLabel(frame1,text=user_data["Name"],
                                font=ctk.CTkFont(weight="bold",size=27,family="Helvetica"))
            labley.place(x=30,y=70)


            btn = ctk.CTkButton(frame1,text="View Schedule",
                                font=ctk.CTkFont(weight="bold",size=27,family="Helvetica"),
                                command=sched)
            btn.place(x=450,y=180)



            frame1.pack(pady=20)



















    # ---------------------------------------------------------------------------------




    def change_password():
        def update():
            if(cur_mail.get() == user_data["Password"]):
                if(new_pass.get()!= cur_mail.get()):
                    user_id = auth.sign_in_with_email_and_password(user_data["Email"],user_data["Password"])
                    idt = user_id["idToken"]
                    auth.delete_user_account(idt)
                    auth.create_user_with_email_and_password(user_data["Email"],new_pass.get())
                    db.collection("Student").document(user_data["Roll Number"]).update({"Password":new_pass.get()})
                    messagebox.showinfo(title="Updtae",message="Update Email Successfull")
                    root.destroy()
                else:
                    messagebox.showerror(title="Updtae",message="Your new email must be different from current email")
                                  
            else:
                messagebox.showerror(title="Updtae",message="Your current email did not match,Try Again")




        root = ctk.CTk()
        root.geometry("600x400")

        root1 =ctk.CTkFrame(root,height=300,width=370)
        root1.pack(pady=45)


        label1 = ctk.CTkLabel(root1,text="Update Password",font=ctk.CTkFont(size=30,weight="bold"))
        label1.place(x=55,y=30)

        label1 = ctk.CTkLabel(root1,text="Enter Current Password",font=ctk.CTkFont(size=15,weight="bold"))
        label1.place(x=20,y=90)

        cur_mail = ctk.CTkEntry(root1,placeholder_text="Enter Current Password",
                                height=32,
                                width=300,
                                corner_radius=10,
                                border_color="#3468c9",
                                font=ctk.CTkFont(size=15,weight="bold"))
        cur_mail.place(x=20,y=120)


        label1 = ctk.CTkLabel(root1,text="Enter New Password",font=ctk.CTkFont(size=15,weight="bold"))
        label1.place(x=20,y=170)

        new_pass = ctk.CTkEntry(root1,placeholder_text="Enter New Password",
                                height=32,
                                width=300,
                                corner_radius=10,
                                border_color="#3468c9",
                                font=ctk.CTkFont(size=15,weight="bold"))
        new_pass.place(x=20,y=200)

        btnx = ctk.CTkButton(root1,text="Change",
                            font=ctk.CTkFont(size=15,weight="bold"),
                            command=update)
        btnx.place(y=250,x=180)
        root.mainloop()





    # ---------------------------------------------------------------------------------
    # def update():
    #         rl = user_data["Roll Number"]   try to update main screen
    #         root.destroy()
    #         # change_email(rl)
    # ---------------------------------------------------------------------------------



    def change_email():
        def sub_update():
            if(cur_mail.get() == user_data["Email"]):
                if(new_mail.get()!= cur_mail.get()):
                    user_id = auth.sign_in_with_email_and_password(user_data["Email"],user_data["Password"])
                    idt = user_id["idToken"]
                    auth.delete_user_account(idt)
                    auth.create_user_with_email_and_password(new_mail.get(),user_data["Password"])
                    db.collection("Student").document(user_data["Roll Number"]).update({"Email":new_mail.get()})
                    messagebox.showinfo(title="Updtae",message="Update Email Successfull")
                    root.destroy()
                else:
                    messagebox.showerror(title="Updtae",message="Your new email must be different from current email")
                                  
            else:
                messagebox.showerror(title="Updtae",message="Your current email did not match,Try Again")
                 
                         




        root = ctk.CTk()
        root.geometry("600x400")
        root.title("Update Email")

        root1 =ctk.CTkFrame(root,height=300,width=370)
        root1.pack(pady=45)


        label1 = ctk.CTkLabel(root1,text="Update Email",font=ctk.CTkFont(size=30,weight="bold"))
        label1.place(x=95,y=30)

        label1 = ctk.CTkLabel(root1,text="Enter Current Email",font=ctk.CTkFont(size=15,weight="bold"))
        label1.place(x=20,y=90)

        cur_mail = ctk.CTkEntry(root1,placeholder_text="Enter Current Email",
                                height=32,
                                width=300,
                                corner_radius=10,
                                border_color="#3468c9",
                                font=ctk.CTkFont(size=15,weight="bold"))
        cur_mail.place(x=20,y=120)


        label1 = ctk.CTkLabel(root1,text="Enter New Email",font=ctk.CTkFont(size=15,weight="bold"))
        label1.place(x=20,y=170)

        new_mail = ctk.CTkEntry(root1,placeholder_text="Enter New Email",
                                height=32,
                                width=300,
                                corner_radius=10,
                                border_color="#3468c9",
                                font=ctk.CTkFont(size=15,weight="bold"))
        new_mail.place(x=20,y=200)

        btnx = ctk.CTkButton(root1,text="Change",
                            font=ctk.CTkFont(size=15,weight="bold"),command=sub_update)
        btnx.place(y=250,x=180)
        root.mainloop()




# ===============================================================================



    def sched_new():
        delete_page()
        root = ctk.CTkFrame(main_frame,width=1100,height=750)

        ctk.set_appearance_mode("Light")
        root1 = ctk.CTkFrame(root,height=40,width=130)

        root1.place(x=10,y=10)

        root2 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root2,text="Monday",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=25,y=5)
        root2.place(x=160,y=10)

        root3 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root3,text="Tuesday",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=20,y=5)
        root3.place(x=310,y=10)

        root4 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root4,text="Wednesday",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=10,y=5)
        root4.place(x=460,y=10)

        root5 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root5,text="Thursday",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=20,y=5)
        root5.place(x=610,y=10)

        root6 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root6,text="Friday",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=35,y=5)
        root6.place(x=760,y=10)
        # =================================================================================

        root7 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root7,text="IT Workshop",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root7,text="(PCC-IT-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root7.place(x=760,y=60)
        root7.configure(fg_color="#33DF9B")


        root8 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root8,text="Engneering Biology",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root8,text="(BSC-BS-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root8.place(x=610,y=60)
        root8.configure(fg_color="#33DF9B")



        root9 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root9,text="Digital Logic",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root9,text="(ECE-CSE-302)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root9.place(x=460,y=60)
        root9.configure(fg_color="#33DF9B")


        root10 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root10,text="Analog Electronic ",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root10,text="(ECE-EC-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root10.place(x=310,y=60)
        root10.configure(fg_color="#33DF9B")


        root11 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root11,text="Data Structure & Algorithms",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=6,y=0)
        label1 = ctk.CTkLabel(root11,text="(PCC-IT-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=35,y=17)
        root11.place(x=160,y=60)
        root11.configure(fg_color="#33DF9B")



        root12 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root12,text="10:00-10:50",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root12.place(x=10,y=60)


        # ================================================================================


        root13 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root13,text="Engneering Biology",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root13,text="(BSC-BS-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root13.place(x=760,y=110)
        root13.configure(fg_color="#33DF9B")


        root14 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root14,text="Digital Logic",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root14,text="(ECE-CSE-302)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root14.place(x=610,y=110)
        root14.configure(fg_color="#33DF9B")


        root15 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root15,text="IT Workshop",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root15,text="(PCC-IT-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root15.place(x=460,y=110)
        root15.configure(fg_color="#33DF9B")


        root16 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root16,text="Data Structure & Algorithms",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=6,y=0)
        label1 = ctk.CTkLabel(root16,text="(PCC-IT-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=35,y=17)
        root16.place(x=310,y=110)
        root16.configure(fg_color="#33DF9B")


        root17 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root17,text="Analog Electronic ",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root17,text="(ECE-EC-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root17.place(x=160,y=110)
        root17.configure(fg_color="#33DF9B")


        root18 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root18,text="10:50-11:40",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root18.place(x=10,y=110)



        # =======================================================================================

        root19 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root19,text="Digital Logic",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root19,text="(ECE-CSE-302)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root19.place(x=760,y=160)
        root19.configure(fg_color="#33DF9B")


        root20 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root20,text="Analog Electronic ",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root20,text="(ECE-EC-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root20.place(x=610,y=160)
        root20.configure(fg_color="#33DF9B")


        root21 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root21,text="Differential Calculus",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root21,text="(BSC-M-302)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root21.place(x=460,y=160)
        root21.configure(fg_color="#EC706C")


        root22 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root22,text="Data Structure & Algorithms",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=6,y=0)
        label1 = ctk.CTkLabel(root22,text="(PCC-IT-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=35,y=17)
        root22.place(x=310,y=160)
        root22.configure(fg_color="#33DF9B")


        root23 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root23,text="Engneering Biology",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root23,text="(BSC-BS-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root23.place(x=160,y=160)
        root23.configure(fg_color="#33DF9B")


        root24 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root24,text="11:40-12:30",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root24.place(x=10,y=160)

        # =======================================================================================

        root25 = ctk.CTkFrame(root,height=40,width=130)
        root25.place(x=760,y=210)

        root26 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root26,text="Differential Calculus",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root26,text="(BSC-M-302)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root26.place(x=610,y=210)
        root26.configure(fg_color="#33DF9B")


        root27 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root27,text="Linguistic & Oral Communication",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=6,y=0)
        label1 = ctk.CTkLabel(root27,text="(HSM-HU-381)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=35,y=17)
        root27.place(x=460,y=210)
        root27.configure(fg_color="#33DF9B")


        root28 = ctk.CTkFrame(root,height=40,width=130)
        root28.place(x=310,y=210)

        root29 = ctk.CTkFrame(root,height=40,width=130)
        root29.place(x=160,y=210)

        root30 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root30,text="12:30-13:20",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root30.place(x=10,y=210)

        # =======================================================================================


        root31 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root31,text="K",font=ctk.CTkFont(size=30,weight="bold"))
        label.place(x=55,y=3)
        root31.place(x=760,y=260)
        root31.configure(fg_color="#e0ce00")

        root32 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root32,text="A",font=ctk.CTkFont(size=30,weight="bold"))
        label.place(x=55,y=3)
        root32.place(x=610,y=260)
        root32.configure(fg_color="#e0ce00")


        root33 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root33,text="E",font=ctk.CTkFont(size=30,weight="bold"))
        label.place(x=55,y=3)
        root33.place(x=460,y=260)
        root33.configure(fg_color="#e0ce00")


        root34 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root34,text="R",font=ctk.CTkFont(size=30,weight="bold"))
        label.place(x=55,y=3)
        root34.place(x=310,y=260)
        root34.configure(fg_color="#e0ce00")


        root35 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root35,text="B",font=ctk.CTkFont(size=30,weight="bold"))
        label.place(x=55,y=3)
        # label.configure(fg_color="black")
        root35.place(x=160,y=260)
        root35.configure(fg_color="#e0ce00")


        root36 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root36,text="13:20-14:10",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root36.place(x=10,y=260)

        # ===========================================================================================


        root37 = ctk.CTkFrame(root,height=40,width=130)
        root37.place(x=760,y=310)

        root38 = ctk.CTkFrame(root,height=40,width=130)
        root38.place(x=610,y=310)

        root39 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root39,text="IT Workshop",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root39,text="(PCC-IT-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root39.place(x=460,y=310)
        root39.configure(fg_color="#6ED8EA")


        root40 = ctk.CTkFrame(root,height=40,width=130)
        root40.place(x=310,y=310)

        root41 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root41,text="Analog Electronic ",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root41,text="(ECE-EC-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root41.place(x=160,y=310)
        root41.configure(fg_color="#6ED8EA")


        root42 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root42,text="14:10-15:00",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root42.place(x=10,y=310)

        # ====================================================================================================


        root43 = ctk.CTkFrame(root,height=40,width=130)
        root43.place(x=760,y=360)

        root44 = ctk.CTkFrame(root,height=40,width=130)
        root44.place(x=610,y=360)

        root45 = ctk.CTkFrame(root,height=40,width=130)
        root45.place(x=460,y=360)

        root46 = ctk.CTkFrame(root,height=40,width=130)
        root46.place(x=310,y=360)

        root47 = ctk.CTkFrame(root,height=40,width=130)
        root47.place(x=160,y=360)

        root48 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root48,text="15:00-15:50",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root48.place(x=10,y=360)

        # =======================================================================================


        root49 = ctk.CTkFrame(root,height=40,width=130)
        root49.place(x=760,y=410)

        root50 = ctk.CTkFrame(root,height=40,width=130)
        root50.place(x=610,y=410)

        root51 = ctk.CTkFrame(root,height=40,width=130)
        root51.place(x=460,y=410)

        root52 = ctk.CTkFrame(root,height=40,width=130)
        root52.place(x=310,y=410)

        root53 = ctk.CTkFrame(root,height=40,width=130)
        root53.place(x=160,y=410)

        root54 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root54,text="15:50-16:40",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root54.place(x=10,y=410)

        # =======================================================================================

        root55 = ctk.CTkFrame(root,height=40,width=130)
        root55.place(x=760,y=460)

        root56 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root56,text="Digital Logic",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=30,y=0)
        label1 = ctk.CTkLabel(root56,text="(ECE-CSE-302)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=38,y=17)
        root56.place(x=610,y=460)
        root56.configure(fg_color="#6ED8EA")


        root57 = ctk.CTkFrame(root,height=40,width=130)
        root57.place(x=460,y=460)

        root58 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root58,text="Data Structure & Algorithms",font=ctk.CTkFont(size=7,weight="bold"))
        label.place(x=6,y=0)
        label1 = ctk.CTkLabel(root58,text="(PCC-IT-301)",font=ctk.CTkFont(size=7,weight="bold"))
        label1.place(x=35,y=17)
        root58.place(x=310,y=460)
        root58.configure(fg_color="#6ED8EA")


        root59 = ctk.CTkFrame(root,height=40,width=130)
        root59.place(x=160,y=460)

        root60 = ctk.CTkFrame(root,height=40,width=130)
        label = ctk.CTkLabel(root60,text="16:40-17:30",font=ctk.CTkFont(size=20,weight="bold"))
        label.place(x=6,y=7)
        root60.place(x=10,y=460)

        root.pack(pady=20)
    




# ==================================================================================Update Profile
    def edite_page(event):
            delete_page()
            frame1 = ctk.CTkFrame(main_frame,width=1100,height=750)
            img1 = PhotoImage(file="logo1 (1).png")
            label = ctk.CTkLabel(frame1, image=img1,text="",height=10,width=10)
            label.place(x=35,y=16)



            def time():
                string = strftime('%H:%M:%S %p')
                mark.configure(text = string)
                mark.after(1000, time)


            mark = ctk.CTkLabel(frame1, 
                        font = ('calibri', 20, 'bold'))
            mark.place(x=910,y=16)
            time()


            lablex= ctk.CTkLabel(frame1,text="Welcome",
                                font=ctk.CTkFont(weight="bold",size=40,family="Verdana"))
            lablex.place(x=100,y=15)

            labley= ctk.CTkLabel(frame1,text=user_data["Name"],
                                font=ctk.CTkFont(weight="bold",size=27,family="Helvetica"))
            labley.place(x=30,y=70)

            l1 =ctk.CTkLabel(frame1,text="Update Profile",
                            font=ctk.CTkFont(weight="bold",size=35,family="Verdana"))
            l1.place(x=415,y=160)

            l2 =ctk.CTkLabel(frame1,text="Update :  ",
                            font=ctk.CTkFont(weight="bold",size=20))
            l2.place(x=420,y=250)

            bt1 =ctk.CTkButton(frame1,
                            text="Email",
                            font=ctk.CTkFont(weight="bold",size=20),
                            command=change_email)
            bt1.place(x=520,y=248)


            l3 =ctk.CTkLabel(frame1,text="Update :  ",
                            font=ctk.CTkFont(weight="bold",size=20))
            l3.place(x=420,y=310)

            bt2 =ctk.CTkButton(frame1,
                            text="Password",
                            font=ctk.CTkFont(weight="bold",size=20),
                            command=change_password)
            bt2.place(x=520,y=310)

            frame1.pack(pady=20)

    # ----------------------------------------------------------------------
    root = ctk.CTk()
    root.geometry("1300x550")
    root.title("InteliSched")

    option_frame = ctk.CTkFrame(root,border_color="#101B46")


    home_btn = ctk.CTkLabel(option_frame,text="Student Details",
                                    font=ctk.CTkFont(weight="bold",size=25),
                                    corner_radius=25,width=250)
    home_btn.place(y=40)
    home_btn.bind("<Button-1>",home_page)


    home_btn1 = ctk.CTkLabel(option_frame,text="Update Profile",
                                    font=ctk.CTkFont(weight="bold",size=25),
                                    corner_radius=25,width=250)
    home_btn1.place(y=100)
    home_btn1.bind("<Button-1>",edite_page)


    home_btn2  = ctk.CTkLabel(option_frame,text="View Schedule",
                                    font=ctk.CTkFont(weight="bold",size=25),
                                    corner_radius=25,width=250)
    home_btn2.place(y=160)
    home_btn2.bind("<Button-1>",sched_page)


    home_btn3 = ctk.CTkLabel(option_frame,text="View Notice",
                                    font=ctk.CTkFont(weight="bold",size=25),
                                    corner_radius=25,width=250)
    home_btn3.place(y=220)
    home_btn3.bind("<Button-1>",xD)



    home_btn4 = ctk.CTkButton(option_frame,text="Log Out",
                                    font=ctk.CTkFont(weight="bold",size=20),
                                    corner_radius=5,
                                    width=250,
                                    height=35,
                                    command=log_out)
    home_btn4.place(y=280)


    option_frame.pack(side=ctk.LEFT)
    option_frame.configure(width=250,height = 750)


    main_frame = ctk.CTkFrame(root,bg_color="#333740")
    main_frame.pack(side=ctk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(width=1150,height=750)
    img1 = PhotoImage(file="logo1 (1).png")
    label = ctk.CTkLabel(main_frame, image=img1,text="",height=10,width=10)
    label.place(x=35,y=16)



    def time():
        string = strftime('%H:%M:%S %p')
        mark.configure(text = string)
        mark.after(1000, time)


    mark = ctk.CTkLabel(main_frame, 
                            font = ('calibri', 20, 'bold'))
    mark.place(x=910,y=35)
    time()
    lablex1= ctk.CTkLabel(main_frame,text="IntelliSched",
                                    font=ctk.CTkFont(weight="bold",size=40))
    lablex1.place(x=100,y=15)

    lablex2= ctk.CTkLabel(main_frame,text="Welcome",
                                    font=ctk.CTkFont(weight="bold",size=55,family="Verdana"))
    lablex2.place(x=400,y=155)

    lablex2= ctk.CTkLabel(main_frame,text=user_data["Name"],
                                    font=ctk.CTkFont(weight="bold",size=35,family="Helvetica"))
    lablex2.place(x=427,y=230)

    root.mainloop()



if __name__ == "__main__":
     handel_student_details("20221013")
    # print(user_data["Name"])