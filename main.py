from tkinter import *           # GUI package
from time import sleep, time
#from keyboard import is_pressed
from pynput.keyboard import Listener
from pynput import mouse
import math
import random

rectangle_max_iter  = 5   # max number of iterations
max_timer_click     = 2   # max timer to click image
rectangle_width     = 200 # rectangle width
click_error         = 0   # click error

score = 0   # score used to return right clicks

# variables to control program
rectangle_show = False  #indicates if the rectangle is on screen
rectangle_timer = 0     #used to control time
rectangle_iter = 0      #used to count program iterations
random_pos_x = None     #stores x rectangle's position
random_pos_y = None     #stores y rectangle's coordenate
clicked = False         #indicates if left click is pressed
isRunning = True        #indicates if program is running


canvas = None      #used to support rectangle un tkinter
  

#Function that is executed every time the mouse is clicked
#and get the position x,y of the cursor.
def on_click(x, y, button, pressed):
    global rectangle_show, clicked, score, random_pos_x, random_pos_y, rectangle_width

    print("margins x:{}-{}  y:{}-{}".format(random_pos_x, random_pos_x+rectangle_width, random_pos_y, random_pos_y+rectangle_width)) #debug

    if button == mouse.Button.left and pressed==True: #check if left button is clicked, pressed=Trye indicates pressed, False indicates release
        print("Left click: {},{}".format(x,y)) #debug: show cursor position on console
        if x>= random_pos_x-click_error and x<= random_pos_x+rectangle_width+click_error and y>= random_pos_y-click_error and y<= random_pos_y+rectangle_width+click_error : #check if click is inside rectangle+error area.
            print("CLICKED OK")
            score=score+1 #add 1 to score if is a right click, inside a rectangle+error area.
        clicked = True

    if button == mouse.Button.right and pressed ==True: #check if right click is pressed
        print("Right click: {},{}".format(x,y))

mouse_listener = mouse.Listener(on_click=on_click)     #sets mouse listener passing function prior defined
mouse_listener.start()                                 #starts mouse listener

window = Tk()   #init Tkinter window
window.title("Click Tracker v0.1")
ws = window.winfo_screenwidth() #gets the width of screen
hs = window.winfo_screenheight() #gets the heigth of screen

w_ws = ws+10
w_hs = hs-20
#w_ws = math.ceil(ws/2) #reduce width ,scale
#w_hs = math.ceil(hs/2) #reduce height, scale
window.wm_attributes('-topmost','true')
window.configure(background='black')
window.geometry("{}x{}+{}+{}".format(w_ws,w_hs,-10,-5)) #sets size of windows

# Function to create rectangles on screen, receive canvas as input
def createRectangle(c):
    global rectangle_show, rectangle_timer, rectangle_iter, isRunning, rectangle_max_iter
    global random_pos_x, random_pos_y

    if rectangle_show == False: # checks if rectangle is on screen, if not, create it
        random_pos_x = random.randint(0+rectangle_width,w_ws-rectangle_width) #random x position on screen
        random_pos_y = random.randint(0+rectangle_width,w_hs-rectangle_width) #random y position on screen
        c.create_rectangle(random_pos_x, random_pos_y, random_pos_x+rectangle_width, random_pos_y+rectangle_width, fill="blue") #create blue reactangle
        rectangle_show = True   # set true to indicates that rectangle is on screen
        rectangle_iter = rectangle_iter + 1 # add 1 to program iteration
        rectangle_timer = time()    # restart timer


canvas = Canvas(window, width=w_ws, height=w_hs) #create canvas with screen size
canvas.configure(background='black')    #set background color
canvas.pack()      #add canvas to window screen

#loop of program
while True:    

    if rectangle_show == False: #checks if rectangle is on screen, if not, create one
        createRectangle(canvas) #create rectangle
        print("R: {},{}".format(random_pos_x,random_pos_y))
    if time()- rectangle_timer > max_timer_click or clicked: # checks time of rectangle on screen or left button of mouse was clicked
        canvas.delete("all")    #delete all objects in canvas
        rectangle_show = False  #set false to create a new rectangle
        clicked = False         #set false to init click state
        rectangle_timer = time()    #restart timer

    if rectangle_iter>rectangle_max_iter:   #checks if program reach max iterations
        isRunning = False   #end program

    #if is_pressed('ctrl+space'):
    #    isRunning = False
    
    sleep(0.1)

    if isRunning == False:  #end program
        break

    window.update() #function mandatory to update tkinter gui

mouse_listener.stop()   #stop listener when program was ended
window.destroy()        #destroy windows of tkinter

print("YOUR SCORE IS {} OF {}".format(score, rectangle_max_iter))
