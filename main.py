from tkinter import *
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

score = 0

rectangle_show = False
rectangle_timer = 0
rectangle_iter = 0
random_pos_x = None
random_pos_y = None

canvas = None
clicked = False

isRunning = True

def on_click(x, y, button, pressed):
    global rectangle_show, clicked, score, random_pos_x, random_pos_y, rectangle_width
    print("margins x:{}-{}  y:{}-{}".format(random_pos_x, random_pos_x+rectangle_width, random_pos_y, random_pos_y+rectangle_width))
    if button == mouse.Button.left and pressed==True:
        print("Left click: {},{}".format(x,y))
        if x>= random_pos_x-click_error and x<= random_pos_x+rectangle_width+click_error and y>= random_pos_y-click_error and y<= random_pos_y+rectangle_width+click_error :
            print("CLICKED OK")
            score=score+1
        clicked = True
    if button == mouse.Button.right and pressed ==True:
        print("Right click: {},{}".format(x,y))

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()    # Start mouse click listener

window = Tk()

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
w_ws = ws
w_hs = hs
#w_ws = math.ceil(ws/2) #reduce width
#w_hs = math.ceil(hs/2) #reduce height
window.wm_attributes('-topmost','true')
window.configure(background='black')
window.geometry("{}x{}+{}+{}".format(w_ws,w_hs,0,0))

# Function to create rectangles
def createRectangle(c):
    global rectangle_show, rectangle_timer, rectangle_iter, isRunning, rectangle_max_iter
    global random_pos_x, random_pos_y
    if rectangle_show == False:
        random_pos_x = random.randint(0+rectangle_width,w_ws-rectangle_width)
        random_pos_y = random.randint(0+rectangle_width,w_hs-rectangle_width)
        c.create_rectangle(random_pos_x, random_pos_y, random_pos_x+rectangle_width, random_pos_y+rectangle_width, fill="blue")
        rectangle_show = True
        rectangle_iter = rectangle_iter + 1
        rectangle_timer = time()


canvas = Canvas(window, width=w_ws, height=w_hs)
canvas.configure(background='black')
canvas.pack()

while True:    

    if rectangle_show == False:
        createRectangle(canvas)
        print("R: {},{}".format(random_pos_x,random_pos_y))
    if time()- rectangle_timer > max_timer_click or clicked: # 2 seconds to click
        canvas.delete("all")
        rectangle_show = False
        clicked = False
        rectangle_timer = time()

    if rectangle_iter>rectangle_max_iter:
        isRunning = False

    #if is_pressed('ctrl+space'):
    #    isRunning = False
    
    sleep(0.1)

    if isRunning == False:
        break

    window.update()

mouse_listener.stop()
window.destroy()

print("YOUR SCORE IS {} OF {}".format(score, rectangle_max_iter))
