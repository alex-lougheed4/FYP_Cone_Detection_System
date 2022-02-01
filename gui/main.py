from tkinter import *


root = Tk()

root.title("Main Page")

window_width = 1200
window_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


timeLabel = Label(root,text="time placeholder")

#soundTestButton = Button(root,text="Test Volume",command=testVolume)
#startButton = Button(root,text="Start",command=onClickStart)

customConsole = Listbox(root)

volumeSlider = Scale(root, from_=0, to=100)




root.mainloop()