from tkinter import *
import imageio
from PIL import Image, ImageTk


ws = Tk()

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


    
titleLabel = Label(ws,text="Main")
timeLabel = Label(ws,text="time placeholder")

stopButton = Button(ws,text="Stop",command=onClickEndButton)

customConsole = Listbox(ws)


canvas = Canvas(ws, width = 400, height = 300)      
      
img = PhotoImage(file="placeholder.png")      
canvas.create_image(20,20, anchor=NW, image=img) 

titleLabel.grid(row=0,column=0)
timeLabel.grid(row=0,column=1)
canvas.grid(row=1,column=0)


customConsole.grid(row=2,column=0)
stopButton.grid(row=2,column=1)



ws.mainloop()
