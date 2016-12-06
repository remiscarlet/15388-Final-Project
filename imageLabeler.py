import Tkinter as tk
import os
import PIL.Image
import PIL.ImageTk
import time

# events-example3.py
# Demos timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.squareLeft = 50
    data.squareTop = 50
    data.squareFill = "yellow"
    data.squareSize = 25
    data.circleCenters = [ ]
    data.counter = 0
    data.headingRight = True
    data.headingDown = True
    data.isPaused = False
    data.timerDelay = 1000
    data.index = 1
    updateImage(data)

def mousePressed(event, data):
    newCircleCenter = (event.x, event.y)
    data.circleCenters.append(newCircleCenter)

def updateImage(data):
    cwd = os.path.abspath(os.path.dirname(__file__))
    data.imagePath = cwd+("/testPics/image01_crop%d.png" % data.index)
    image = PIL.Image.open(data.imagePath)

    data.index += 1
    photo = PIL.ImageTk.PhotoImage(image)
    data.image = photo

def keyPressed(event, data):
    if event.keysym in ["Left", "Right", "Up"]:
      if (event.keysym == "Left"):
          logGender(data, False)
      elif (event.keysym == "Right"):
          logGender(data, True)
      elif (event.keysym == "Up"):
          logGender(data, None)
      updateImage(data)

def logGender(data, doWhat):
    if doWhat != None:
      gender = "Female" if doWhat else "Male"
      print data.imagePath + " is a " + gender 
    else:
      print "Image was not even of a face"

def redrawAll(canvas, data):

    canvas.create_image(250,250, anchor="center", image=data.image)



####################################
# use the run function as-is
####################################

def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds

    # create the root and the canvas
    root = Tk()
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)

