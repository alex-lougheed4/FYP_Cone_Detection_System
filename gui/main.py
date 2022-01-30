import tkinter as tk
from turtle import screensize, window_width

window = tk.Tk()
window.title("Demo")

window_width = 1200
window_height = 800

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


window.mainloop()