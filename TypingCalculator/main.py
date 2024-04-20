from time import *
import random as r
def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error=error+1
        except:
             error=error+1
    return error
# print(time)

def speed_time(time_s,time_e,userinput):
    delay_time=time_e-time_s 
    time_R=round(delay_time,2)
    speed=len(userinput)/time_R
    return round(speed)
    
           
test=["Hey Brother my name is sandeep verma from the maharajganj and now software engineer in infotiqq",
     "now these day i am learnig python secure career in tech ", "development is crucial nowadays" ]
      
test1=r.choice(test)
print("*********** typing speed ****************")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter : ")
time_2=time()

print('Speed: ', speed_time(time_1,time_2,testinput), "w/sec")
print("Error: " , mistake(test1,testinput))

