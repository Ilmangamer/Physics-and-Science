"""

To move the ball, I have to define a function move_ball(). In the function, I have to define the position of the ball that will constantly get updated when the ball hits the canvas wall (left, right, top, and bottom).

To update the ball position, I have to use canvas.after(duration, function()) which reflects the ball to change its position after a certain time duration.

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


