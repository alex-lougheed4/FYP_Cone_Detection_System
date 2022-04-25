from tkinter import *
import pygame




ws = Tk()
pygame.mixer.init()
pygame.mixer.music.load('testSound.mp3')


ws.title("Demo")

window_width = 1200
window_height = 800

screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

ws.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


def onClickStartButton():
    newWindow = Toplevel(ws)

    newWindow.title("Confirm Start?")

    newWindow.geometry("400x200")
    
    messageLabel = Label(newWindow,text="Are you sure you want to Start?")

    confirmButton = Button(newWindow,text="Start",command=onClickConfirm)
    cancelButton = Button(newWindow,text="Cancel",command=newWindow.destroy)

    messageLabel.grid(row=0, column = 2)
    confirmButton.grid(row=1,column = 0)
    cancelButton.grid(row=1,column=3)

def onClickConfirm():
    ws.destroy()
    import main

def volume(x):
     pygame.mixer.music.set_volume(float(volumeSlider.get())/100)
     volume = volumeSlider.get()/100
     main.setVolume(volume)
     print(f'volume set to {volumeSlider.get()}')

def testVolume():
    print(f'Volume is at: {pygame.mixer.music.get_volume()}')
    pygame.mixer.music.play()

def getVolume():
    return volume
    
titleLabel = Label(ws,text="Cone Detection System Main Menu")
timeLabel = Label(ws,text="time placeholder")
soundTestButton = Button(ws,text="Test Volume",command=testVolume)
startButton = Button(ws,text="Start",command=onClickStartButton)

customConsole = Listbox(ws)

volumeSlider = Scale(ws, from_=100, to=0, orient=VERTICAL,command=volume)
volumeSlider.set(50)#Sets the default value of the volume slider

titleLabel.grid(row=0,column=0)
timeLabel.grid(row=0,column=1)
soundTestButton.grid(row=1,column=1)
volumeSlider.grid(row=1,column=2)
customConsole.grid(row=1,column=0)
startButton.grid(row=2,column=1)



ws.mainloop()