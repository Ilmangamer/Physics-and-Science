"""
Tkinter is a standard Python library which is used to create GUI-based applications. To create a simple moving ball application, we can use the Canvas widget which allows the user to add images, draw shapes, and animating objects. The application has the following components,

A Canvas widget to draw the oval or ball in the window.

To move the ball, we have to define a function move_ball(). In the function, you have to define the position of the ball that will constantly get updated when the ball hits the canvas wall (left, right, top, and bottom).

To update the ball position, we have to use canvas.after(duration, function()) which reflects the ball to change its position after a certain time duration.

Finally, execute the code to run the application.

"""
import time
import tkinter as tk
from class_Ball import *

root = tk.Tk()
root.geometry("700x200")
WIDTH = 1900
HEIGHT = 1020
cc= tk.Canvas(root, bg="lightgrey", height=HEIGHT, width=WIDTH)
cc.place(x=1, y=2)


volley_balls = [Ball(cc, 0,0, 100, 1,1, "yellow"), 
Ball(cc, 0,0, 100, 3,2, "white"), 
Ball(cc, 0,0, 100, 2,3, "blue"), 
Ball(cc, 0,0, 100, 5,3, "purple"), 
Ball(cc, 0,0, 100, 6,4, "green"), 
Ball(cc, 0,0, 100, 7,4, "orange"), 
Ball(cc, 0,0, 100, 8,5, "red"), 
Ball(cc, 0,0, 100, 9,5, "powderblue"), 
Ball(cc, 0,0, 100, 10,6, "brown"), 
Ball(cc, 0,0, 100, 11,6, "black"), 
Ball(cc, 0,0, 100, 12,7, "grey"), 
Ball(cc, 0,0, 100, 13,7, "blue"),  
Ball(cc, 0,0, 100, 14,8, "pink")]

root.configure(bg="white")

while True:
    for i in volley_balls:
        i.move()


    root.update()
    time.sleep(0.000001)


root.mainloop()





"""
while True:
    volley_ball.move()
    volley_ball2.move()
    volley_ball3.move()
    volley_ball4.move()
    volley_ball5.move()
    volley_ball6.move()
    volley_ball7.move()
    volley_ball8.move()
    volley_ball9.move()
    volley_ball10.move()
    volley_ball11.move()
    volley_ball12.move()
    volley_ball13.move()
"""

"""
c1 = cc.create_oval(80,80,120,120, fill="powderblue")
c2 = cc.create_oval(140,140,180,180, fill="red")
c3 = cc.create_oval(180,180,240,240, fill="white")
"""

"""
volley_ball = Ball(cc, 0,0, 100, 1,1, "yellow")
volley_ball2 = Ball(cc, 0,0, 100, 3,2, "white")
volley_ball3 = Ball(cc, 0,0, 100, 2,3, "blue") 
volley_ball4 = Ball(cc, 0,0, 100, 5,3, "purple")
volley_ball5 = Ball(cc, 0,0, 100, 6,4, "green")
volley_ball6 = Ball(cc, 0,0, 100, 7,4, "orange")
volley_ball7 = Ball(cc, 0,0, 100, 8,5, "red")
volley_ball8 = Ball(cc, 0,0, 100, 9,5, "powderblue")
volley_ball9 = Ball(cc, 0,0, 100, 10,6, "brown")
volley_ball10 = Ball(cc, 0,0, 100, 11,6, "black")
volley_ball11 = Ball(cc, 0,0, 100, 12,7, "grey")
volley_ball12 = Ball(cc, 0,0, 100, 13,7, "blue")
volley_ball13 = Ball(cc, 0,0, 100, 14,8, "pink")
"""