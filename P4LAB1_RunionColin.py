# Colin Runion
# 10/15/2026
# Use a for loop and a while loop to draw shapes

import turtle

# Set up the window and drawing object (turtle)
window = turtle.Screen()
timmy = turtle.Turtle()

timmy.pensize(3)
timmy.pencolor("purple")

#  For loop to draw a square
for side in range(4):
    timmy.forward(200)
    timmy.right(90)
    
# while loop that draws a triangle
num = 1
while num <= 3:
    # draw a side
    timmy.forward(200)
    timmy.left(120)
    # Increment num
    num = num + 1



# Keep window open
window.mainloop()