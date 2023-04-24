#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Five Xmas Presents (2 player game):
    Objective: Get 5 or more presents of your colour (either 
    red or green) in a row.
    Rows must be either vertical or horizontal (no diagonal wins)
    
    1. White sqaures are unclaimed present locations.
    2. Can not change the colour of pre-existing present. 
    3. Mis clicking or clicking a claimed sqaure may result
       in a loss of a turn. 
    4. Presents can be placed anywhere on th game board.
    
    
"""

#Names: 
#Sujaana Anton 
#Abani Jeevaharan 
#Vaishna Sritharan 


import turtle
from turtle import *
import numpy

from freegames import line
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pygame


#Import module that allows pygame to play music 
from pygame import mixer
from PIL import Image

#How music is played in the background
pygame.mixer.init() #Intializes the import of music from downloaded zip folder 
mixer.music.load(r'bell_sound.wav') #Loads music from a specific location on your computer, this should be from 'Downloads'
mixer.music.play(-1) #Allows music to be played in background of pygame, '-1' allows music to be played an infinite amount of times



turns = {'red': 'green', 'green': 'red'}# Alternate turns between each colour, ex;after red comes green and vice versa
state = {'player': 'green', 'rows': [0] * 8} #Assigns each turn as a different colour, either as red or green 
player_red = 0
player_green = 0
h_counter = 0



#in the array white =0, red=1, green=2
grid_array = numpy.zeros((8,8))



def grid():
    #Dimensions of grid and changes 
    """Draw Connect Four grid."""
    bgpic('snowwinter.gif')#Background picture of grid
    
    #coordinates of where the grid starts and ends 
    x = -185
    y = -185
    grid = [[square(30, 'white',x,y)],
                [square(30, 'white',x,y)]] #Initially sets all squares to be white before the players can click on it 
    
    while(y<200):
        x=-185
        while(x<175):
            grid.append([square(30, 'white',x,y)]) #Maps out grid to display to player, also sets up boundries so the squares will not exceed said boundries
            x+=50
        y+=50
    
        
    grid
            
            
    
    update()


def tap(x, y):
    #Takes into account where player place their coloured squares
    play = True 
    if(play != False):
        """Draw red or yellow squares in tapped row."""
        player = state['player'] #States which colour is in each square
        rows = state['rows']
    
        row = int((x + 200) // 50)
        count = rows[row]# Check whether row is full or not
    
        #sets (x,y) postion based on the users click so the right square can fill in
        if(x<-135):
            x = 0
        elif(x<-85):
            x = 1
        elif(x<-35):
            x=2
        elif(x<15):
            x = 3
        elif(x<65):
            x = 4
        elif(x<115):
            x = 5
        elif(x<165):
            x=6
        else:
            x=7
            
        if(y<-135):
            y = 0
        elif(y<-85):
            y = 1
        elif(y<-35):
            y=2
        elif(y<15):
            y = 3
        elif(y<65):
            y = 4
        elif(y<115):
            y = 5
        elif(y<165):
            y=6
        else:
            y=7
    
    
        up()
        if(y<=200): #Checks to make players are clicking on white squares, and ensure that square that is not already filled in
            if(grid_array[x,y]==0):
                square(30, player,-185+x*(50),-185+y*(50))
                if(player == "red"): 
                    grid_array[x,y] = 1
                elif(player =="green"):
                    grid_array[x,y] = 2
                
                update()
                
            if(winner(x,y)):
                window = Tk()
                bgpic('snowfall.gif')#background picture of grid 
        
              #Situations if either player wins  
                if(player == 'red'):
                    
            #Labels window with 'Red is winner!' when red wins, with a red background with white letters in a specific font
                    lbl1=Label(window, text= "Red", fg='white',bg = 'red', font=("MingLiU_HKSCS-LIU-LIU-Kungchi Ni-100001.ExtB", 24)) #describes colour, font, and size
                    lbl2=Label(window, text= 'is the Winner!',fg='white',bg = 'red', font=("MingLiU_HKSCS-LIU-LIU-Kungchi Ni-100001.ExtB", 23))
                    lbl1.place(x=170, y=100)#x,y coordinated of the labels (where it is placed on GUI)
                    lbl2.place(x=150, y=150)
                    #Displays the winner window 
                    window.title('Winner!')
                    window.geometry("400x300+10+10")#Dimensions of window displayed
                    window.configure(bg = 'red')
                    window.mainloop()
                    play = False
    
                else:
            
            #Labels window with 'green is winner!' when green wins, with a green background with white letters in a specific font
                    lbl1=Label(window, text= "Green", fg='white',bg = 'green', font=("MingLiU_HKSCS-LIU-LIU-Kungchi Ni-100001.ExtB", 24))
                    lbl2=Label(window, text= 'is the Winner!',fg='white',bg = 'green', font=("MingLiU_HKSCS-LIU-LIU-Kungchi Ni-100001.ExtB", 23))
                    lbl1.place(x=170, y=100)
                    lbl2.place(x=150, y=150)
                
                    window.title('Winner!')
                    window.geometry("400x300+10+10")#Dimensions of window displayed
                    window.configure(bg = 'green')#background colour 
                    window.mainloop()
                    play = False
                
            
    
        rows[row] = count + 1
        state['player'] = turns[player]#every other play is a different player 
        
def winner(x,y):
    player = state['player']
    #check is an int created based on the state of the player, later used to help check for a winner
    check = 0#orginally set to 0
    
    #set to 1 or 2 based on if current player/player who just clicked is red or green
    if(player =="red"):
        check = 1
    elif(player == 'green'):
        check = 2
        
    
    h_counter = 0 #counter counts when there are square in a row horizontally
    hit = None#used to tell compter that the right square before it is the same colour(when it is true) 
    for i in range(grid_array[x].size):
        #first time hitting a colour, or hitting the smae colour that has already been hit
        if(grid_array[i,y] == check and (hit == True or hit == None)): 
            h_counter +=1
            hit = True
        elif(grid_array[i,y] == check):#first time hitting a colour after a colour has already been hit
            h_counter = 1
            hit = True
        elif(grid_array[i,y] != check and hit != None):
            hit = False
            
   
    #returns true if there are 5 or more of the same colours in a row horizontally
    if(h_counter>=5):
        return True

    
    
    v_counter = 0#counter counts when there are square in a row vertically
    hit = None
    for i in range(grid_array[y].size):
        #first time hitting a colour, or hitting the smae colour that has already been hit
        if(grid_array[x,i] == check and (hit == True or hit == None)):
            v_counter +=1
            hit = True
        elif(grid_array[x,i] == check):#first time hitting a colour after a colour has already been hit
            hit = True
            v_counter =1
            
        elif(grid_array[x,i] != check and hit != None):
            hit = False
            
     #returns true if there are 5 or more of the same colours in a row vertically 
    if(v_counter>=5):
        return True

#Instead of dots, squares are drawn
def square(length,color,x,y):
    t = turtle.Turtle()
    t.fillcolor(color) #colour of the square initially 
    t.penup()#Initates drawing
    t.begin_fill()
    t.goto(x,y)
    t.forward(length)  
    t.left(90)  
    t.forward(length)  
    t.left(90) # Dimensions of a 90X90 square
    t.forward(length)  
    t.left(90)  
    t.forward(length)  
    t.left(90) 
    t.end_fill()
    t.penup()#Ends the drawing
    
if __name__ == "__main__": # Runs all major modules 
    setup(420, 420, 370, 0)# Dimensions of grid 
    hideturtle()
    tracer(False)
    grid()#Displays grid to players
    onscreenclick(tap) #Collects the amount of taps happening 
    done()
    
    
    
    