#!/usr/bin/env python
"""
PURPOSE: Outline for my January 8th presentation to SLCPy Meetup Group
AUTHOR: Dylan Gregersen
DATE: Tue Jan  6 18:22:12 2015
"""
# ########################################################################### #

import os
from glob import glob

# Modules for plotting
import numpy as np 
import matplotlib.pylab as plt
# or as a shortcut
import pylab as plt 

# ########################################################################### #

# Define some data to make plots of

fl = glob("example_data/*.dat")
star_data = {}
for fp in fl:
    fn = os.path.basename(fp)
    name = fn.replace(".dat","").replace("_"," ")
    star_data[name] = np.genfromtxt(fp)

x,y = star_data['Sun'].T

# ########################################################################### #

# Basic line plot which connects all the x,y pairs
# this creates a figure and adds the lines
plt.plot(x,y)

# you then use plt.show to show the figure in a gui 
# or use plt.savefig to save figure to a file
plt.show()
# plt.savefig("solar_spectrum.png")

# ########################################################################### #

# Matplotlib is stateful so if you can edit by calling commands
plt.plot(x,y)
plt.title("The Sun!") # modify the title of the plot
plt.show()

# ########################################################################### #

# PRO-TIP: use matplotlib as object-oriented and stateLESS as you can

fig = plt.figure() # create a figure in the state
ax = fig.add_subplot(1,1,1) # add subplot to the figure object
ax.plot(x,y)
ax.set_title("The Sun!")
plt.show()

# ########################################################################### #


ax = plt.figure().add_subplot(111) # shortcut to pervious
x,y = star_data['Sun'].T
# modify parameters of the figure using keywords
ax.plot(x,y,color='g',label="The Sun")
# add another object onto the plot
x,y = star_data['Arcturus'].T
ax.plot(x,y,color='#FF0808',label="Arcturus")
# To modify items on the plot
ax.set_xlabel("Wavelength (Angstroms)")
ax.set_ylabel("Flux")
ax.legend()
ax.grid(True)
plt.show()


# ASIDE-1: try out `help(ax.plot)` to review other keywords  
# ASIDE-2: Other functions work very similarly (e.g. ax.scatter, ax.imshow)

# ########################################################################### #

# PRO-TIP: make your own plot objects and plot modifcation functions

class PlotItemStar (object):
    def __init__ (self,star_data,name,ax=None):
        """ Plots a star's spectrum """
        if ax is None:
            ax = plt.gca()
        x,y = star_data[name].T 
        self.line, = ax.plot(x,y,label=name)
        self.ax = ax 
        self.name = name 
        self.star_data = star_data         

def apply_spectrum_axes (ax):
    """ Applys parameters to the axes """
    ax.set_xlabel("Wavelength (Angstroms)")
    ax.set_ylabel("Flux")
    ax.legend()
    ax.grid(True)

ax = plt.figure().add_subplot(111)
PlotItemStar(star_data,"Sun",ax)
PlotItemStar(star_data,"Arcturus",ax)
apply_spectrum_axes(ax)
plt.show()


# ########################################################################### #

# Now with functions creating two axes on on figure is easy

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
PlotItemStar(star_data,"Sun",ax)
apply_spectrum_axes(ax)

ax = fig.add_subplot(1,2,2)
PlotItemStar(star_data,"Arcturus",ax)
apply_spectrum_axes(ax)

plt.show()


# ########################################################################### #

# PRO-TIP: Seporate out your plotting keyword arguments

# ASIDE: dictionaries, do you know what they are/ what methods they have

x,y = star_data['Sun'].T
ax = plt.figure().add_subplot(111)
kws = dict(\
    color = 'r',
    lw=3,
    alpha=0.9,
    )
ax.plot(x,y,**kws)
plt.show()


# ########################################################################### #

# Write your functions to use arbitrary arguments

class PlotItemStar (object):
    def __init__ (self,star_data,name,ax=None,**kws):
        """ Plots a star's spectrum """
        if ax is None:
            ax = plt.gca()
        x,y = star_data[name].T 
        kws.setdefault("label",name)
        kws.setdefault("color","r")
        kws.setdefault("linestyle","-")
        self.line, = ax.plot(x,y,**kws)
        self.ax = ax 
        self.name = name 
        self.star_data = star_data 

ax = plt.figure().add_subplot(111)
PlotItemStar(star_data, 'Sun',ax)
PlotItemStar(star_data, 'Arcturus', ax=ax, color='b', label="ARCTURUS")
apply_spectrum_axes(ax)
plt.show()


# ########################################################################### #

# PRO-TIP: use matplotlib artist objects

ax = plt.figure().add_subplot(111)
x,y = star_data['Vega'].T 
line, = ax.plot(x,y,color='g')

def key_press_callback (event):
    """ """
    if event.inaxes != ax:
        return
    print("key = {}".format(event.key))
    if event.key == '1':
        print("Yay! You're #1")
        x,y = star_data['Betelgeuse'].T 
        ax.set_title("Betelgeuse")
        line.set_xdata(x)
        line.set_ydata(y) 
        line.set_color("r")
        line.set_marker('*')
        ax.figure.canvas.draw()

ax.figure.canvas.mpl_connect("key_press_event",key_press_callback)
plt.show()

# ########################################################################### #

# PRO-TIP: random, but try to use ax.plot(x,y,ls='none',marker='o') instead of
# ax.scatter(x,y) because it works better

ax = plt.figure().add_subplot(111)
x,y = star_data['Sun'].T
ax.plot(x,y,ls="none",marker="o")
plt.show() 

# ########################################################################### #


# The real way I learned Matplotlib was looking at their gallery. I found a 
# plot exemplifying what I want the looked at the source code to recreate. 

# Check out http://matplotlib.org/gallery.html









