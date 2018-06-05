#!/usr/bin/env python

####################################
#Author: Ethan Hicks               #
#Published on: 11/3/2016           #
#contact: misterethan85@gmail.com  #
####################################
# Pre Requisites,
# Image must be a PNG 
# Image must be scaled properly 1600*900 pixels. 

try:
    #sysmods
    import socket
    import struct
    from itertools import cycle
    import io
    import os
except Exception as ex:
    print(ex)

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''
    def __init__(self, image_files, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.minsize(width=1600,height=900)
        self.maxsize(width=1605,height=905)
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        #
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
    def show_slides(self):
        
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)


    def run(self):
        self.mainloop()
# set milliseconds time between slides
delay = 5000
# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are
image_files = [
'C:/Users/Ethan/Pictures/testing/msi_logo.png',
'C:/Users/Ethan/Pictures/testing/Nvidia_logo.png',
'C:/Users/Ethan/Pictures/testing/python_logo.png',
'C:/Users/Ethan/Pictures/testing/windows.png'
]
# upper left corner coordinates of app window
x = 10
y = 10
app = App(image_files, x, y, delay)
app.show_slides()
app.run()

