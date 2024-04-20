from tkinter import *
import os

def Restart():
    os.system("shutdown /r /t 1")
def Restart_time():
    os.system("shutdown /r /t 20")
def Logout():
    os.system("shutdown -1")
def Shutdown():
    os.system("shutdown /s /t 1")

st=Tk()
st.title("ShutDown App")
st.geometry("500x600")
st.config(bg="blue")

r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="Log out ",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Logout)
lg_button.place(x=150,y=270,height=50,width=200)

st_button=Button(st,text="shut down",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()