# Import tkinter and webview libraries
from tkinter import *
import webview
import platform
import os
import applicationUI
tk = Tk()

# Functions & Global Variables
appName = "Hello World Application"
guiFileName = "main"
path = os.path.abspath(f"../main.html")
path = path.replace('\\', '/')
fileName = path
filePathForEngine = path
print(f"Located GUI File at: {filePathForEngine}")


def universalClear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Recreate UI File
f = open(fileName, 'w')
# Create GUI File
f.write(applicationUI.mainUI)
f.close()

# Basic Setups
tk.title('My App Name')

# get the screen dimension
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

# Set Window Width
window_width = int(screen_width/2)
window_height = int(screen_height/2)

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
tk.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Open website
webview.create_window(appName, filePathForEngine)
webview.start()

# root.mainloop()
