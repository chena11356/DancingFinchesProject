#Made by Jordan Ambrosio, Alex Chen, William Chen, and Imtiaz Rahman
#this is Alex's part --> finch 2

import notes
from finch import Finch
from time import sleep
from random import randint

#first define essentials

BLANK=[0,0,0]
GREEN=[0,255,0]
YELLOW=[255,255,38]
PINK=[255,32,200]
PURPLE=[205,88,250]
RED=[255,0,0]
BLUE=[0,0,255]
FAINTBLUE=[0,0,150]
FAINTERBLUE=[0,0,75]
FAINTESTBLUE=[0,0,30]
ORANGE=[250,165,37]
CYAN=[32,255,255]


def Connect(): #connect to Finch
    for i in range(2): #run twise
        try: #try to connect to physical Finch
            finch=Finch()
            return finch #if it works, connect Finch
        except: #if no connection
            if i==0: 
                print "Failure connecting to Finch on the first try."
                Quit(finch)
    finch=0 #return 0 if no connection on second try
    print "Failure connecting to Finch on the second try."
    return finch

def Quit(finch): #close connection to Finch
    finch.close()

def randomColor(): #return a random color
    return [randint(0,255),randint(0,255),randint(0,255)]

def move(finch,left,right,time,ledList): #moves by activating left and right motors
    finch.led(ledList[0],ledList[1],ledList[2]) #changes color
    finch.wheels(left,right) #moves
    sleep(time)

def wait(finch,ledList,time): #sleep repeats last action; thus, this actually makes Finch wait
    move(finch,0,0,0,ledList)
    sleep(time)

def rotate45(finch,ledList,lr): #rotates by performing different powers on each wheel
    if lr=="l":
        move(finch,0,1,0.25,ledList) #takes 0.25 seconds
    else:
        move(finch,1,0,0.25,ledList)

def rotate90(finch,ledList,lr): #works in same manner as rotate45
    rotate45(finch,ledList,lr)
    wait(finch,ledList,0.025)
    rotate45(finch,ledList,lr)#takes 0.5 seconds
    wait(finch,ledList,0.025)
    
def rotate180(finch,ledList,lr): #works in same manner as rotate90
    rotate90(finch,ledList,lr)
    rotate90(finch,ledList,lr) #takes 1 second

def rotate360(finch,ledList,lr): #works in same manner as rotate180
    rotate180(finch,ledList,lr)
    rotate180(finch,ledList,lr)#takes 2 seconds

def forward1(finch,power,time,ledList): #forward by same power on each wheel
    move(finch,power,power,time,ledList)

def backward1(finch,power,time,ledList): #backward by negative power on each wheel
    move(finch,-1*power,-1*power,time,ledList)

def wiggle(finch,power,time,ledList,direc):
    if str(direc)=="l":
        move(finch,-1*power,power,time,ledList) #rotate left
        move(finch,power,-1*power,time,ledList) #rotates right to starting position
    if str(direc)=="r":
        move(finch,power,-1*power,time,ledList) #rotate 
        move(finch,-1*power,power,time,ledList) #rotates
        
def wiggleWaggle(finch,power,time,ledList1,ledList2,iterations,direc):
    i=0
    t=1
    if direc == "r":
        t=-1
    while i<iterations: #loop determines how many times wiggle waggle is performed
        
        wiggle(finch,t*power,time,ledList1,direc) #wiggles left
        wiggle(finch,-1*t*power,time,ledList2,direc)
        i+=1

def wiggleForward(finch,ledList, firstDirec): #squiggles forward --> takes 1.5 seconds
    o = 0
    t = 0
    if str(firstDirec) == "l":
        t=1
    elif str(firstDirec) == "r":
        o=1
    move(finch,o,t,0.25,ledList) #rotate
    forward1(finch,1,0.5,ledList) #move forward
    move(finch,t,o,0.25,ledList) #rotate
    forward1(finch,1,0.5,ledList) #move forward



#now moving on to the composition of the dance --> each scene corresponds to number on schematic paper



def scene1(finch): #3 secs long --> wiggle forward then back to original position
    backward1(finch,0.5,1.5,randomColor())
    forward1(finch,0.5,1.5,randomColor())
    
def scene2(finch, direc): #6 secs long --> turn slowly to face each other while blinking
    for i in range(3):
        a=randomColor()
        finch.led(a)
        wait(finch,a,1)
    b=randomColor()
    rotate45(finch,b,str(direc))
    wait(finch,b,2.5)

def scene3(finch, direc): #5 secs long --> move backwards and wiggle waggle
    backward1(finch,0.5,1.5,YELLOW)
    wiggleWaggle(finch,0.5,1,GREEN,YELLOW,1,direc)
    wait(finch,YELLOW,1.5)

def scene4(finch,d1,d2): #7 secs long --> go forward and dance
    forward1(finch,0.5,1.5,YELLOW) #1.5 sec
    rotate360(finch,GREEN,d1) #2 sec
    rotate360(finch,YELLOW,d2) #2 sec
    wait(finch,PINK,1.5) #1.5 sec

def scene5(finch, semiDirec, fullDirec): #5 secs long --> turn around
    rotate180(finch,GREEN,str(semiDirec)) #1 sec
    rotate360(finch,YELLOW,str(fullDirec)) #2 sec
    finch.led(PINK)
    wait(finch,PINK,1)
    finch.led(GREEN)
    wait(finch,GREEN,1)

def scene6(finch,direc): #2 secs long --> wiggle forward
    wiggleForward(finch,YELLOW,direc)
    wait(finch,PINK,0.5)

def scene7(finch, direc): #4 secs long --> first all face up and go up, then go down
    rotate90(finch,PURPLE,str(direc)) #takes 0.5 secs
    forward1(finch,0.5,1,YELLOW) #takes 1 sec
    backward1(finch,0.5,1,PURPLE) #1 sec
    wait(finch,YELLOW,1.5) #1.5 sec of waiting for finches 1 and 2
    #finches 3 and 4 --> rotate 180 and then wait 0.5 seconds

def scene8(finch, direc): #6 secs long --> move back and forward and rotate
    backward1(finch,0.5,2,GREEN)
    forward1(finch,0.5,2,GREEN)
    rotate90(finch,GREEN,direc)
    wait(finch,GREEN,1.5)

def scene9(finch,semiDirec,rightDirec): #4.75 secs long --> loop around until top two face bottom two
    rotate180(finch,GREEN,str(semiDirec)) #1 sec
    forward1(finch,0.5,0.75,YELLOW) #0.75 sec
    rotate90(finch,YELLOW,str(rightDirec)) #0.5 sec
    forward1(finch,0.5,0.75,PINK) #0.75 sec
    rotate90(finch,PINK,str(rightDirec)) #0.5 sec
    forward1(finch,0.5,0.75,GREEN) #0.75 sec
    rotate90(finch,GREEN,str(rightDirec)) #0.5 sec
    forward1(finch,0.5,0.75,YELLOW) #0.75 sec

def scene10(finch,direc): #1.25 secs long --> shake and turn color
    wiggleWaggle(finch,1,0.25,BLUE,GREEN,2,direc)
    wait(finch,GREEN,0.25)

def scene11(finch,direc): #3 secs long --> move up, shake
    backward1(finch,0.5,1,GREEN) #will be forward and blue for finches 3 and 4
    wiggleWaggle(finch,1,0.25,BLUE,GREEN,4,direc)

def scene12(finch): #4 secs long --> color wave going from 1 to 2 to 3 to 4
    finch.led(YELLOW) #when it comes finch 2's turn, flash blue
    wait(finch,YELLOW,1)
    wait(finch,BLANK,3)    

def scene13(finch,rightDirec,wwDirec): #3 secs long --> left and right turn to face each other, slam into each other, get angry
    rotate90(finch,YELLOW,str(rightDirec)) #takes 0.5 secs
    forward1(finch,0.5,1,YELLOW) #1 sec --> slam into finch 2
    wiggleWaggle(finch,1,0.25,RED,RED,2,wwDirec) #1 sec --> wiggle and turn red
    wait(finch,RED,0.5)

def scene14(finch,semiDirec): #6 secs long --> turn around and slam each other harder
    backward1(finch,0.5,0.25,RED) #0.25 sec --> back up
    rotate180(finch,RED,str(semiDirec)) #1 sec --> turn around
    forward1(finch,0.5,1.5,RED) #1.5 sec --> prepare to ram
    rotate180(finch,RED,str(semiDirec)) #1 sec --> turn around
    forward1(finch,0.5,1.75,RED) #1.75 sec
    wait(finch,RED,0.5) #0.5 sec

def scene15(finch): #4 secs long --> go to blue, then fade to blank
    finch.led(BLUE)
    wait(finch,BLUE,1)
    finch.led(FAINTBLUE)
    wait(finch,BLUE,1)
    finch.led(FAINTERBLUE)
    wait(finch,BLUE,1)
    finch.led(FAINTESTBLUE)
    wait(finch,BLUE,1)

def main():
    finch=Connect() #connect finch
    if finch==0: #if no connection, print cannot connect and return nothing
        print "Cannot connect."
        return
    scene1(finch) #call each scene (there doesn't seem to be a more efficient way)
    scene2(finch,"r")
    scene3(finch,"l")
    scene4(finch, "r","l")
    scene5(finch,"l","r")
    scene6(finch,"l")
    scene7(finch,"r")
    scene8(finch,"r")
    scene9(finch,"r","l")
    scene10(finch,"l")
    scene11(finch,"l")
    scene12(finch)
    scene13(finch,"l","r")
    scene14(finch,"r")
    scene15(finch)
    Quit(finch)


#call main after running the program so that there's no delay
