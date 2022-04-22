from tkinter import *
from PIL import Image, ImageTk
import datetime, time, subprocess
import os, os.path, re, threading, sys
import pygame

import home

from pydub import AudioSegment
from pydub.playback import play

sys.path.insert(0, '/Database/')
from Database import DataBaseController as dbController

import Collision

fps = 30
Crop_Width = Crop_Height = 600
input_path = f"Image_Capture/"
outputPath = f"Detected_Images/"

collisionSound = AudioSegment.from_mp3("CollisionSound.mp3")
hotAreaColisionSound = AudioSegment.from_mp3("HotArea_Collision.mp3")
hotAreaPreCollisionSound = AudioSegment.from_mp3("HotArea_PreCollision.mp3")

speed = 0
currentImage= ""

boxList = []



ws = Tk()
pygame.mixer.init()
pygame.mixer.music.set_volume(home.getVolume())

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
ws.title("Main Page")

window_width = 1200
window_height = 800

screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

timeStamp = ""
coneAhead, inHotArea = FALSE

longitude,latitude = 0

ws.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    timeStamp = (f"{hour + ':' + minute + ':' + second}")

    timeLabel.config(text=hour + ':' + minute + ':' + second)
    timeLabel.after(1000,clock)

def onClickEndButton():
    newWindow = Toplevel(ws)

    newWindow.title("Confirm End?")

    newWindow.geometry("400x200")
    
    messageLabel = Label(newWindow,text="Are you sure you want to Stop?")

    confirmButton = Button(newWindow,text="Stop",command=onClickStop)
    cancelButton = Button(newWindow,text="Cancel",command=newWindow.destroy)

    messageLabel.grid(row=0, column = 2)
    confirmButton.grid(row=1,column = 0)
    cancelButton.grid(row=1,column=3)

def onClickStop(): 
    ws.destroy()
    import home

def changeImage(image):
    os.chdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection/Detected_Images')
    #Take image from output Data folder in order 
    canvas.delete("all")
    currentImage = f"{image[:-4]}-detection.jpg"
    canvas.img = ImageTk.PhotoImage(Image.open(f"{image[:-4]}-detection.jpg"))
    canvas.create_image(20,20, anchor=NW, image=canvas.img)
    return

def playConeHitSound(angle):
    customConsole.insert(END, f"{timeStamp}: Collision Sound Played")
    #pan audio by angle
    pannedColision = collisionSound.pan(panValue(angle))
    pygame.mixer.music.load(pannedColision) #changed to panned version
    pygame.mixer.music.play()
    pygame.mixer.music.unload()


def playEnterHotArea():
    customConsole.insert(END, f"{timeStamp}: Hot Area Sound Played")
    pygame.mixer.music.load('Entered_HotArea.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.unload()
    
def playHotAreaCollision(angle):
    customConsole.insert(END, f"{timeStamp}: Hot Area Collision Sound Played")
    #pan audio by angle
    pannedHotColision = hotAreaColisionSound.pan(panValue(angle))
    pygame.mixer.music.load(pannedHotColision) #changed to panned version
    pygame.mixer.music.load('HotArea_Collision.mp3') #changed to panned version
    pygame.mixer.music.play()
    pygame.mixer.music.unload()


def playHotAreaPreCollision(): #called when a cone in image is in central 10 (example) degrees and 2 seconds away
    customConsole.insert(END, f"{timeStamp}: Hot Area Pre-Collision Sound Played")
    #pan audio by angle
    pannedHotPreColision = hotAreaPreCollisionSound.pan(panValue(angle))
    pygame.mixer.music.load(pannedHotPreColision) #changed to panned version
    pygame.mixer.music.load('HotArea_PreCollision.mp3') #changed to panned version
    pygame.mixer.music.play()
    pygame.mixer.music.unload() 

def checkGPSLocation():
    currentPos = (longitude,latitude)
    if(dbController.searchForGPS(currentPos)):
        customConsole.insert(END, f"{timeStamp}: Entered Hot Area at {currentPos}")
        inHotArea = TRUE
        playEnterHotArea()

def panValue(angle): #for 125 degree frontal field of view range -62.5 to 62.5 
    if(angle > 0):
        return angle/62.5
    elif (angle < 0):
        return (angle/62.5)*-1
    else: 
        return angle


def collisionOccurred(angle):
    customConsole.insert(END, f"{timeStamp}: Collision detected")
    Collision.makeCollision(longitude,latitude,timeStamp)
    if(inHotArea):
        playHotAreaCollision(angle) #pass in angle
    else:
        playConeHitSound(angle) #pass in angle

def setLongitude(val):
    longitude = val

def setLatitude(val):
    latitude = val    

titleLabel = Label(ws,text="Main")
timeLabel = Label(ws,text=f"")
clock()

stopButton = Button(ws,text="Stop",command=onClickEndButton)

customConsole = Listbox(ws,bg= "black", fg="white",)


canvas = Canvas(ws, width = 400, height = 300)      
      
canvas.img = PhotoImage(file="gui/placeholder.png")      
canvas.create_image(20,20, anchor=NW, image=canvas.img) 

titleLabel.grid(row=0,column=0)
timeLabel.grid(row=0,column=1)
canvas.grid(row=1,column=0,columnspan=2)

def detectImage(image):
    os.chdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection')
    boxes = subprocess.run(f"/opt/homebrew/Caskroom/miniforge/base/envs/testcv/bin/python cone_detector_image.py --image {input_path}{image} --output-dir {outputPath} -c 600".split(" "))
    return boxes
os.chdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection/Image_Capture')

def distanceOfCone(box): #return distance of cone in m
    pixelWidth = box.xmax - box.ymax 
    focalLength = 5118.11 #Focal Length ALL UNITS IN M 
    trueWidth = 0.127
    #check size of box compared to size of known distance box 
    return (trueWidth * focalLength) / pixelWidth



def detection():
    imageList = os.listdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection/Image_Capture')
    if('.DS_Store' in imageList):
        imageList.remove('.DS_Store')
    imageList.sort(key=lambda f: int(re.sub('\D', '', f)))

    for i in imageList:
        boxList = detectImage(i) 
        print(f"{i} detected.")
        customConsole.insert(END, f"{timeStamp}: image {i} detected")
        print(f"dierectory: {os.getcwd()}")
        os.chdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection/Image_Capture')
        os.remove(i) 
        print(f"{i} removed.")
        changeImage(i)
        customConsole.insert(END, f"{timeStamp}: image {i} showing")
        #check if any in boxes is in the central "strip" of image check space to left and right of x coordinates
        for box in boxList:
            #check space on respective side of minX and maxX based on image size (or pixels since all images should be of the same size)
            if(box.minX >=2*(i.width/5)) and (box.maxX <= 3*(i.width/5)):
                coneAhead = TRUE
                if(distanceOfCone(box) / speed == 2 + marginOfError) or  (distanceOfCone(box) / speed == 2 - marginOfError): # if Time away from the cone at current speed is 2s +/- a margin of error
                    if(inHotArea): #if the vehicle is in a hotArea
                        playHotAreaPreCollision() 
                    #else:
                        #playAreaPreCollision()
                #play relevant sound for pre collision
            

        

threading.Thread(target=detection).start()




customConsole.grid(row=2,column=0)
stopButton.grid(row=2,column=1)



ws.mainloop()
