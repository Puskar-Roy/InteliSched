import customtkinter as ctk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase_clouddb.json")
firebase_admin.initialize_app(cred)
db = firestore.client() #for cloud firestore
# docs = db.collection("Schedule").get()
# for doc in docs:
#     print(doc.to_dict())
# user_data = 0
# if result.exists:
# user_data = result["11"].to_dict()

def sched():
    root = ctk.CTk()
    root.geometry("1450x850")
    mnd1 = db.collection("Schedule").document("11").get()
    mnd2 = db.collection("Schedule").document("12").get()
    mnd3 = db.collection("Schedule").document("13").get()
    mnd4 = db.collection("Schedule").document("14").get()

    tus1 = db.collection("Schedule").document("21").get()
    tus2 = db.collection("Schedule").document("22").get()
    tus3 = db.collection("Schedule").document("23").get()
    tus4 = db.collection("Schedule").document("24").get()
    tus5 = db.collection("Schedule").document("25").get()


    wed1 = db.collection("Schedule").document("31").get()
    wed2 = db.collection("Schedule").document("32").get()
    wed3 = db.collection("Schedule").document("33").get()
    wed4 = db.collection("Schedule").document("34").get()
    wed5 = db.collection("Schedule").document("35").get()
    wed6 = db.collection("Schedule").document("36").get()
    wed7 = db.collection("Schedule").document("37").get()
    wed8 = db.collection("Schedule").document("38").get()
    wed9 = db.collection("Schedule").document("39").get()


    thu1 = db.collection("Schedule").document("40").get()
    thu2 = db.collection("Schedule").document("41").get()
    thu3 = db.collection("Schedule").document("42").get()
    thu4 = db.collection("Schedule").document("43").get()
    thu5 = db.collection("Schedule").document("44").get()
    thu6 = db.collection("Schedule").document("45").get()
    thu7 = db.collection("Schedule").document("46").get()
    thu8 = db.collection("Schedule").document("47").get()
    thu9 = db.collection("Schedule").document("48").get()

    fri1 = db.collection("Schedule").document("51").get()
    fri2 = db.collection("Schedule").document("52").get()
    fri3 = db.collection("Schedule").document("53").get()
    fri4 = db.collection("Schedule").document("54").get()
    fri5 = db.collection("Schedule").document("55").get()
    fri6 = db.collection("Schedule").document("56").get()
    fri7 = db.collection("Schedule").document("57").get()
    fri8 = db.collection("Schedule").document("58").get()
    fri8 = db.collection("Schedule").document("59").get()









    user_data = 0
    d1 = mnd1.to_dict()
    d2 = mnd2.to_dict()
    d3 = mnd3.to_dict()
    d4 = mnd4.to_dict()

    tus_d1 = tus1.to_dict()
    tus_d2= tus2.to_dict()
    tus_d3 = tus3.to_dict()
    tus_d4 = tus4.to_dict()
    tus_d5 = tus5.to_dict()

    wed_d1 = wed1.to_dict()
    wed_d2= wed2.to_dict()
    wed_d3 = wed3.to_dict()
    wed_d4 = wed4.to_dict()
    wed_d5 = wed5.to_dict()
    wed_d6 = wed6.to_dict()
    wed_d7 = wed7.to_dict()
    wed_d8 = wed8.to_dict()
    wed_d9 = wed9.to_dict()


    thu_d1 = thu1.to_dict()
    thu_d2 = thu2.to_dict()
    thu_d3 = thu3.to_dict()
    thu_d4 = thu4.to_dict()
    thu_d5 = thu5.to_dict()
    thu_d6 = thu6.to_dict()
    thu_d7 = thu7.to_dict()
    thu_d8 = thu8.to_dict()
    thu_d9 = thu9.to_dict()


    fri_d1 = fri1.to_dict()
    fri_d2 = fri2.to_dict()
    fri_d3 = fri3.to_dict()
    fri_d4 = fri4.to_dict()
    fri_d5 = fri5.to_dict()
    fri_d6 = fri6.to_dict()
    fri_d7 = fri7.to_dict()
    fri_d8 = fri8.to_dict()
    # root = ctk.CTkFrame(main_frame,width=1450,height=850)


    root55 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root55,text="       ",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root55.place(x=10,y=10)

    root56 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root56,text="Monday",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root56.place(x=230,y=10)

    root57 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root57,text="Tuesday",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root57.place(x=450,y=10)

    root58 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root58,text="Wednesday",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=20,y=5)
    root58.place(x=670,y=10)

    root59 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root59,text="Thursday",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root59.place(x=890,y=10)

    root60 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root60,text="Friday",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root60.place(x=1110,y=10)



    # =========================================================

    root2 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root2,text="10:00 - 10:50",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root2.place(x=10,y=80)

    root3 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root3,text=d1["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=15,y=5)
    root3.place(x=230,y=80)
    if (d1["status"]=="true"):
        root3.configure(fg_color="#33DF9B")
    elif(d1["status"]=="false"):
        root3.configure(fg_color="#ec706c")
    elif(d1["status"]=="null"):
        root3.configure(fg_color="#ffffff")
    elif(d1["status"]=="lab"):
        root3.configure(fg_color="#6ED8EA")







    root4 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root4,text=tus_d1["subject"],font=ctk.CTkFont(size=9,weight="bold"))
    label.place(x=10,y=5)
    root4.place(x=450,y=80)
    # root4.configure(fg_color="#33DF9B")
    if (tus_d1["status"]=="true"):
        root4.configure(fg_color="#33DF9B")
    elif(tus_d1["status"]=="false"):
        root4.configure(fg_color="#ec706c")
    elif(tus_d1["status"]=="null"):
        root4.configure(fg_color="#ffffff")
    elif(tus_d1["status"]=="lab"):
        root4.configure(fg_color="#6ED8EA")



    root5 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root5,text=wed_d1["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root5.place(x=670,y=80)
    # root5.configure(fg_color="#33DF9B")

    if (wed_d1["status"]=="true"):
        root5.configure(fg_color="#33DF9B")
    elif(wed_d1["status"]=="false"):
        root5.configure(fg_color="#ec706c")
    elif(wed_d1["status"]=="null"):
        root5.configure(fg_color="#ffffff")
    elif(wed_d1["status"]=="lab"):
        root5.configure(fg_color="#6ED8EA")

    root6 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root6,text=thu_d1["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=30,y=5)
    root6.place(x=890,y=80)
    # root6.configure(fg_color="#33DF9B")
    if (thu_d1["status"]=="true"):
        root6.configure(fg_color="#33DF9B")
    elif(thu_d1["status"]=="false"):
        root6.configure(fg_color="#ec706c")
    elif(thu_d1["status"]=="null"):
        root6.configure(fg_color="#ffffff")
    elif(thu_d1["status"]=="lab"):
        root6.configure(fg_color="#6ED8EA")

    root7 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root7,text=fri_d1["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=15,y=5)
    root7.place(x=1110,y=80)
    if (fri_d1["status"]=="true"):
        root7.configure(fg_color="#33DF9B")
    elif(fri_d1["status"]=="false"):
        root7.configure(fg_color="#ec706c")
    elif(fri_d1["status"]=="null"):
        root7.configure(fg_color="#ffffff")
    elif(fri_d1["status"]=="lab"):
        root7.configure(fg_color="#6ED8EA")    


    # ====================================================

    root8 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root8,text="10:50 - 11:40",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root8.place(x=10,y=150)



    root9 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root9,text=d2["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root9.place(x=230,y=150)
    if (d2["status"]=="true"):
        root9.configure(fg_color="#33DF9B")
    elif(d2["status"]=="false"):
        root9.configure(fg_color="#ec706c")
    elif(d2["status"]=="null"):
        root9.configure(fg_color="#ffffff")
    elif(d2["status"]=="lab"):
        root9.configure(fg_color="#6ED8EA")

    root10 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root10,text=tus_d2["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=25,y=5)
    root10.place(x=450,y=150)
    # root10.configure(fg_color="#33DF9B")
    if (tus_d2["status"]=="true"):
        root10.configure(fg_color="#33DF9B")
    elif(tus_d2["status"]=="false"):
        root10.configure(fg_color="#ec706c")
    elif(tus_d2["status"]=="null"):
        root10.configure(fg_color="#ffffff")
    elif(tus_d2["status"]=="lab"):
        root10.configure(fg_color="#6ED8EA")    

    root11 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root11,text=wed_d2["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root11.place(x=670,y=150)
    root11.configure(fg_color="#33DF9B")


    root12 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root12,text=thu_d2["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root12.place(x=890,y=150)
    root12.configure(fg_color="#33DF9B")

    root13 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root13,text=fri_d2["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root13.place(x=1110,y=150)
    root13.configure(fg_color="#33DF9B")



    # ============================================
    root14 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root14,text="11:40 - 12:30",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root14.place(x=10,y=220)

    root15 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root15,text=d3["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root15.place(x=230,y=220)
    root15.configure(fg_color="#33DF9B")

    root16 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root16,text=tus_d3["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root16.place(x=450,y=220)
    root16.configure(fg_color="#33DF9B")

    root17 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root17,text=wed_d3["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root17.place(x=670,y=220)
    root17.configure(fg_color="#ec706c")


    root18 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root18,text=thu_d3["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root18.place(x=890,y=220)
    root18.configure(fg_color="#33DF9B")

    root19 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root19,text=fri_d3["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=35,y=5)
    root19.place(x=1110,y=220)
    # root19.configure(fg_color="#33DF9B")
    root19.configure(fg_color="#ec706c")



    # ================================================================

    root20 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root20,text="12:30 - 13:20",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root20.place(x=10,y=290)

    root21 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root21,text=d4["subject"],font=ctk.CTkFont(size=11,weight="bold"))
    label.place(x=25,y=5)
    root21.place(x=230,y=290)

    root21 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root21,text=tus_d4["subject"],font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root21.place(x=450,y=290)

    root22 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root22,text=wed_d4["subject"],font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root22.place(x=670,y=290)
    root22.configure(fg_color="#33DF9B")

    root23 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root23,text=thu_d4["subject"],font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root23.place(x=890,y=290)
    root23.configure(fg_color="#33DF9B")

    root24 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root24,text=fri_d4["subject"],font=ctk.CTkFont(size=12,weight="bold"))
    label.place(x=25,y=5)
    root24.place(x=1110,y=290)


    # =======================================================================

    # ===========================================================================


    root25 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root25,text="13:20 - 14:10",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=10)
    root25.place(x=10,y=360)


    root26 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root26,text="B",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=85,y=10)
    root26.place(x=230,y=360)
    root26.configure(fg_color="#e0ce00")

    root27 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root27,text="R",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=85,y=10)
    root27.place(x=450,y=360)
    root27.configure(fg_color="#e0ce00")

    root28 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root28,text="E",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=85,y=10)
    root28.place(x=670,y=360)
    root28.configure(fg_color="#e0ce00")

    root29 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root29,text="A",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=85,y=10)
    root29.place(x=890,y=360)
    root29.configure(fg_color="#e0ce00")


    root30 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root30,text="K",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=85,y=10)
    root30.place(x=1110,y=360)
    root30.configure(fg_color="#e0ce00")




    # =========================================================

    root31 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root31,text="14:10 - 15:00",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root31.place(x=10,y=430)

    root32 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root32,text="Analog Electronic\nCircuits(PPS)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=32,y=5)
    root32.place(x=230,y=430)
    root32.configure(fg_color="#6ED8EA")

    root33 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root33,text="",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root33.place(x=450,y=430)

    root34 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root34,text="IT Workshop\n(IP)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=32,y=5)
    root34.place(x=670,y=430)
    root34.configure(fg_color="#6ED8EA")

    root35 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root35,text="",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root35.place(x=890,y=430)

    root36 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root36,text="",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root36.place(x=1110,y=430)


    # ====================================================

    root37 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root37,text="15:00 - 15:50",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root37.place(x=10,y=500)

    root38 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root38,text="Analog Electronic\nCircuits(PPS)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root38.place(x=230,y=500)
    root38.configure(fg_color="#6ED8EA")

    root39 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root39,text="Data structures &\nAlgorithms(CK)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root39.place(x=450,y=500)
    root39.configure(fg_color="#6ED8EA")

    root40 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root40,text="IT Workshop\n(IP)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root40.place(x=670,y=500)
    root40.configure(fg_color="#6ED8EA")

    root41 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root41,text="Digital Logic\n(CK)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root41.place(x=890,y=500)
    root41.configure(fg_color="#6ED8EA")

    root42 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root42,text=" ",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root42.place(x=1110,y=500)


    # ============================================
    root43 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root43,text="15:50 - 16.40",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root43.place(x=10,y=570)

    root44 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root44,text="Analog Electronics\nCircuits(PPS)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root44.place(x=230,y=570)
    root44.configure(fg_color="#6ED8EA")

    root45 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root45,text="Data Structures &\nAlgorithms(CK)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root45.place(x=450,y=570)
    root45.configure(fg_color="#6ED8EA")

    root46 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root46,text="IT Workshop\n(IP)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root46.place(x=670,y=570)
    root46.configure(fg_color="#6ED8EA")

    root47 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root47,text="Digital Logic\n(CK)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root47.place(x=890,y=570)
    root47.configure(fg_color="#6ED8EA")

    root48 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root48,text=" ",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root48.place(x=1110,y=570)



    # ================================================================

    root49 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root49,text="16:40 - 17:30",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=5,y=5)
    root49.place(x=10,y=640)

    root50 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root50,text=" ",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root50.place(x=230,y=640)

    root51 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root51,text="Data Structures &\nAlgorithms(CK)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root51.place(x=450,y=640)
    root51.configure(fg_color="#6ED8EA")

    root52 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root52,text=" ",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root52.place(x=670,y=640)

    root53 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root53,text="Digital Logic\n(CK)",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=35,y=5)
    root53.place(x=890,y=640)
    root53.configure(fg_color="#6ED8EA")

    root54 = ctk.CTkFrame(root,height=60,width=200)
    label = ctk.CTkLabel(root54,text=" ",font=ctk.CTkFont(size=30,weight="bold"))
    label.place(x=35,y=5)
    root54.place(x=1110,y=640)




    # =======================================================================

    root61 = ctk.CTkFrame(root,height=60,width=200)
    rootxd = ctk.CTkFrame(root61,height=40,width=40)
    rootxd.place(x=10,y=10)
    rootxd.configure(fg_color="#33DF9B")
    label = ctk.CTkLabel(root61,text="Theory Class",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=65,y=14)
    root61.place(x=100,y=710)

    root62 = ctk.CTkFrame(root,height=60,width=200)
    rootxd = ctk.CTkFrame(root62,height=40,width=40)
    rootxd.place(x=10,y=10)
    rootxd.configure(fg_color="#ec706c")
    label = ctk.CTkLabel(root62,text="Cancelled Class ",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=65,y=14)
    root62.place(x=320,y=710)

    root63 = ctk.CTkFrame(root,height=60,width=200)
    rootxd = ctk.CTkFrame(root63,height=40,width=40)
    rootxd.place(x=10,y=10)
    rootxd.configure(fg_color="#ffffff")
    label = ctk.CTkLabel(root63,text="Free Period",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=65,y=14)
    root63.place(x=540,y=710)

    root64 = ctk.CTkFrame(root,height=60,width=200)
    rootxd = ctk.CTkFrame(root64,height=40,width=40)
    rootxd.place(x=10,y=10)
    rootxd.configure(fg_color="#e0ce00")
    label = ctk.CTkLabel(root64,text="Recess",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=65,y=14)
    root64.place(x=760,y=710)

    root64 = ctk.CTkFrame(root,height=60,width=200)
    rootxd = ctk.CTkFrame(root64,height=40,width=40)
    rootxd.place(x=10,y=10)
    rootxd.configure(fg_color="#6ED8EA")
    label = ctk.CTkLabel(root64,text="Laboratory Period",font=ctk.CTkFont(size=15,weight="bold"))
    label.place(x=60,y=14)
    root64.place(x=980,y=710)

    root.mainloop()
    




if __name__ == "__main__":
    # print(result.to_dict())
    # docs = db.collection("Schedule").get()
    # for doc in docs:
    #     print(doc.to_dict())
    # mnd1 = db.collection("Schedule").document("11").get()
    # mnd2 = db.collection("Schedule").document("12").get()
    # mnd3 = db.collection("Schedule").document("13").get()
    # mnd4 = db.collection("Schedule").document("14").get()

    # tus1 = db.collection("Schedule").document("21").get()
    # tus2 = db.collection("Schedule").document("22").get()
    # tus3 = db.collection("Schedule").document("23").get()
    # tus4 = db.collection("Schedule").document("24").get()
    # tus5 = db.collection("Schedule").document("25").get()


    # wed1 = db.collection("Schedule").document("31").get()
    # wed2 = db.collection("Schedule").document("32").get()
    # wed3 = db.collection("Schedule").document("33").get()
    # wed4 = db.collection("Schedule").document("34").get()
    # wed5 = db.collection("Schedule").document("35").get()
    # wed6 = db.collection("Schedule").document("36").get()
    # wed7 = db.collection("Schedule").document("37").get()
    # wed8 = db.collection("Schedule").document("38").get()
    # wed9 = db.collection("Schedule").document("39").get()


    # thu1 = db.collection("Schedule").document("40").get()
    # thu1 = db.collection("Schedule").document("41").get()
    # thu2 = db.collection("Schedule").document("42").get()
    # thu3 = db.collection("Schedule").document("43").get()
    # thu4 = db.collection("Schedule").document("44").get()
    # thu5 = db.collection("Schedule").document("45").get()
    # thu6 = db.collection("Schedule").document("46").get()
    # thu7 = db.collection("Schedule").document("47").get()
    # thu8 = db.collection("Schedule").document("48").get()

    # fri1 = db.collection("Schedule").document("51").get()
    # fri2 = db.collection("Schedule").document("52").get()
    # fri3 = db.collection("Schedule").document("53").get()
    # fri4 = db.collection("Schedule").document("54").get()
    # fri5 = db.collection("Schedule").document("55").get()
    # fri6 = db.collection("Schedule").document("56").get()
    # fri7 = db.collection("Schedule").document("57").get()
    # fri8 = db.collection("Schedule").document("58").get()
    # fri8 = db.collection("Schedule").document("59").get()









    # user_data = 0
    # d1 = mnd1.to_dict()
    # d2 = mnd2.to_dict()
    # d3 = mnd3.to_dict()
    # d4 = mnd4.to_dict()

    # tus_d1 = tus1.to_dict()
    # tus_d2= tus2.to_dict()
    # tus_d3 = tus3.to_dict()
    # tus_d4 = tus4.to_dict()
    # tus_d5 = tus5.to_dict()

    # wed_d1 = wed1.to_dict()
    # wed_d2= wed2.to_dict()
    # wed_d3 = wed3.to_dict()
    # wed_d4 = wed4.to_dict()
    # wed_d5 = wed5.to_dict()
    # wed_d6 = wed6.to_dict()
    # wed_d7 = wed7.to_dict()
    # wed_d8 = wed8.to_dict()
    # wed_d9 = wed9.to_dict()


    # thu_d1 = thu1.to_dict()
    # thu_d2 = thu2.to_dict()
    # thu_d3 = thu3.to_dict()
    # thu_d4 = thu4.to_dict()
    # thu_d5 = thu5.to_dict()
    # thu_d6 = thu6.to_dict()
    # thu_d7 = thu7.to_dict()
    # thu_d8 = thu8.to_dict()


    # fri_d1 = fri1.to_dict()
    # fri_d2 = fri2.to_dict()
    # fri_d3 = fri3.to_dict()
    # fri_d4 = fri4.to_dict()
    # fri_d5 = fri5.to_dict()
    # fri_d6 = fri6.to_dict()
    # fri_d7 = fri7.to_dict()
    # fri_d8 = fri8.to_dict()
    # thu_d9 = thu9.to_dict()


    # if result.exists:
    #     user_data = result.to_dict() 
    # print(d1["subject"])    
    # print(d2["subject"])    
    # print(d3["subject"])    
    # print(d4["subject"])

    # print(tus_d1["subject"])    
    # print(tus_d2["subject"])    
    # print(tus_d3["subject"])    
    # print(tus_d4["subject"])    
    # print(tus_d5["subject"])   

    # print(wed_d1["subject"])    
    # print(wed_d2["subject"])    
    # print(wed_d3["subject"])    
    # print(wed_d4["subject"])    
    # print(wed_d5["subject"])    


    # print(thu_d1["subject"])    
    # print(thu_d2["subject"])    
    # print(thu_d3["subject"])    
    # print(thu_d4["subject"])    
    # print(thu_d5["subject"])  
    # print(thu_d6["subject"])  
    # print(thu_d7["subject"])  
    # print(thu_d8["subject"])  



    # print(fri_d1["subject"])    
    # print(fri_d2["subject"])    
    # print(fri_d3["subject"])    
    # print(fri_d4["subject"])    
    # print(fri_d5["subject"])  
    # print(fri_d6["subject"])  
    # print(fri_d7["subject"])  
    # print(fri_d8["subject"]) 
    sched()
