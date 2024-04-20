from tkinter import *
# import speedtest
from speedtest import Speedtest 

# functions
def speedchecker():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    uploading=str(round(sp.upload()/(10**6),3))+"Mbps"
    down.config(text=down)
    lab_up.config(text=uploading)
    

var=Tk()
var.title("Internet speed test")
var.geometry("600x700")
var.config(bg="Pink")

lab =Label(var,text="Internet Speed Test", font=("Time New Roman",20,"bold"))
lab.place(x=100,y=60,height=60,width=380) 

lab =Label(var,text="downloading speed", font=("Time New Roman",20,"bold"),fg="Black")
lab.place(x=100,y=130,height=60,width=380)

down =Label(var,text="00", font=("Time New Roman",20,"bold"),fg="Black")
down.place(x=100,y=200,height=60,width=380)

upld =Label(var,text="Uploading speed", font=("Time New Roman",20,"bold"),fg="Black")
upld.place(x=100,y=290,height=60,width=380)

lab =Label(var,text="00", font=("Time New Roman",20,"bold"),fg="Black")
lab.place(x=100,y=360,height=60,width=380)

button=Button(var,text="CHECK",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedchecker)
button.place(x=100,y=440,height=60,width=380)

var.mainloop() 

# --------------python----------
# from tkinter import *
# import speedtest

# # functions
# def speedchecker():
#     sp = speedtest.Speedtest()
#     sp.get_servers()
#     down_speed = str(round(sp.download() / (10**6), 3)) + "Mbps"
#     upload_speed = str(round(sp.upload() / (10**6), 3)) + "Mbps"
#     down_label.config(text=down_speed)
#     up_label.config(text=upload_speed)

# var = Tk()
# var.title("Internet speed test")
# var.geometry("600x700")
# var.config(bg="Pink")

# lab = Label(var, text="Internet Speed Test", font=("Time New Roman", 20, "bold"))
# lab.place(x=100, y=60, height=60, width=380)

# lab_down = Label(var, text="downloading speed", font=("Time New Roman", 20, "bold"), fg="Black")
# lab_down.place(x=100, y=130, height=60, width=380)

# down_label = Label(var, text="00", font=("Time New Roman", 20, "bold"), fg="Black")
# down_label.place(x=100, y=200, height=60, width=380)

# lab_up = Label(var, text="Uploading speed", font=("Time New Roman", 20, "bold"), fg="Black")
# lab_up.place(x=100, y=290, height=60, width=380)

# up_label = Label(var, text="00", font=("Time New Roman", 20, "bold"), fg="Black")
# up_label.place(x=100, y=360, height=60, width=380)

# button = Button(var, text="CHECK", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="Red", command=speedchecker)
# button.place(x=100, y=440, height=60, width=380)

# var.mainloop()

