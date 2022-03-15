from tkinter import *
from PIL import Image, ImageTk
import datetime, time, subprocess
import os, os.path, re

fps = 30
Crop_Width = Crop_Height = 600
input_path = f"Image_Capture/"
outputPath = f"Detected_Images/"
#detectorScript = os.path.join(os.path.dirname(__file__), '../ConeDetection/cone_detector_image.py')

ws = Tk()
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
ws.title("Main Page")

window_width = 1200
window_height = 800

screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

ws.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


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
    #Take image from output Data folder in order 
    canvas.delete("all")
    canvas.img = PhotoImage(file=f"{outputPath}{image[:-4]}-detection.jpg")
    canvas.create_image(20,20, anchor=NW, image=canvas.img)
    return
    
titleLabel = Label(ws,text="Main")
timeLabel = Label(ws,text=f"Time: {st}")

stopButton = Button(ws,text="Stop",command=onClickEndButton)

customConsole = Listbox(ws)


canvas = Canvas(ws, width = 400, height = 300)      
      
canvas.img = PhotoImage(file="gui/placeholder.png")      
canvas.create_image(20,20, anchor=NW, image=canvas.img) 

titleLabel.grid(row=0,column=0)
timeLabel.grid(row=0,column=1)
canvas.grid(row=1,column=0)

def detectImage(image):
    os.chdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection')
    subprocess.Popen(f"/opt/homebrew/Caskroom/miniforge/base/envs/testcv/bin/python cone_detector_image.py --image {input_path}{image} --output-dir {outputPath} -c 600".split(" ")) #images not being outputted??
    #can't use run or window won't open

imageList = os.listdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection/Image_Capture')
if('.DS_Store' in imageList):
    imageList.remove('.DS_Store')
imageList.sort(key=lambda f: int(re.sub('\D', '', f)))

os.chdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection/Image_Capture')

#subprocess.run('pip list', shell=True)
for i in imageList:
    detectImage(i) #detected image should be in Detected Images NOT WORKING FOR SOME REASON
    print(f"{i} detected.")
    print(f"dierectory: {os.getcwd()}")
    os.chdir('/Users/alexlougheed/Git Repos/FYP_Cone_Detection_System/ConeDetection/Image_Capture')
    os.remove(i) #original image should be in deleted from Image Capture REMOVING BEFORE DETECTION SCRIPT FINISHES.
    print(f"{i} removed.")
    changeImage(i)



customConsole.grid(row=2,column=0)
stopButton.grid(row=2,column=1)

#ws.after(33,changeImage)



ws.mainloop()
