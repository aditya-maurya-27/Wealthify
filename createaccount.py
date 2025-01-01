import customtkinter as ctk
from tkinter import *
from PIL import Image,ImageTk
def createaccountfunction():
    global createaccountwindow
    createaccountwindow=ctk.CTk()
    createaccountwindow.title(" Create an Account")
    createaccountwindow.geometry("650x650")
    lowerframe=ctk.CTkFrame(master=createaccountwindow, width=550, height=625, corner_radius=20,
                             fg_color="#ee8319", border_width=0)
    lowerframe.place(x=50, y=-20)
    middleframe=ctk.CTkFrame(master=createaccountwindow, width=549, height=580, corner_radius=20,
                              fg_color="#3f3f3f", border_width=0, bg_color="#ee8319")
    middleframe.place(x=50, y=-20)
    upperframe=ctk.CTkFrame(master=createaccountwindow, width=549, height=120, corner_radius=20,
                             fg_color="#ee8319", bg_color="#3f3f3f", border_width=0)
    upperframe.place(x=50, y=-20)
    startwealthifying=Label(master=upperframe, text="Let's start wealthifying!",foreground="white",
                             background="#ee8319", font="Calibri 30 bold")
    
    namephoto=ImageTk.PhotoImage(Image.open("name.png"))
    namelabel=Label(master=middleframe, image=namephoto, borderwidth=0)
    namelabel.place(x=100, y=234)
    emailphoto=ImageTk.PhotoImage(Image.open("mail.png"))
    emaillabel=Label(master=middleframe, image=emailphoto, borderwidth=0)
    emaillabel.place(x=100, y=360)
    lockphoto=ImageTk.PhotoImage(Image.open("lock.png"))
    locklabel=Label(master=middleframe, image=lockphoto, borderwidth=0)
    locklabel.place(x=102, y=482)

    nameentry=ctk.CTkEntry(master=middleframe, width=350, corner_radius=0, text_color="#ee8319",
                         border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Full Name")
    nameentry.place(x=108, y=190)
    emailentry=ctk.CTkEntry(master=middleframe, width=350, corner_radius=0, text_color="#ee8319",
                         border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Permanent Email")
    emailentry.place(x=108, y=290)
    passwordentry=ctk.CTkEntry(master=middleframe, width=350, corner_radius=0, text_color="#ee8319",
                         border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Create Password")
    passwordentry.place(x=108, y=389)


    underlineframe1=ctk.CTkFrame(master=middleframe, width=400, height=3, bg_color="#3f3f3f",
                                  fg_color="#ee8319")
    underlineframe1.place(x=69, y=220)
    underlineframe2=ctk.CTkFrame(master=middleframe, width=400, height=3, bg_color="#3f3f3f",
                                  fg_color="#ee8319")
    underlineframe2.place(x=69, y=320)
    underlineframe3=ctk.CTkFrame(master=middleframe, width=400, height=3, bg_color="#3f3f3f",
                                  fg_color="#ee8319")
    underlineframe3.place(x=69, y=420)
    checkbox=ctk.CTkCheckBox(master=middleframe, fg_color="#ee8319", hover_color="#95510f", corner_radius=8,
                             text="I am above the age of 18 years.", font=("Calibri",16))
    checkbox.place(x=155, y=460)
    submit=ctk.CTkButton(master=middleframe, width=130, height=30, text="Submit", font=("Calibri",18),
                           fg_color="#ee8319", hover_color="#95510f", corner_radius=8)
    submit.place(x=205, y=510)
    startwealthifying.place(x=140, y=57)
    createaccountwindow.resizable(False, False)
    createaccountwindow.grab_set()
    createaccountwindow.mainloop()

createaccountfunction()