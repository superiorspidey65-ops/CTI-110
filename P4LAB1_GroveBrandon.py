# Brandon Grove
# 11/4/2026
# P4LAB1
# Use turtle and loops to draw a square and triangle

#import the library
import turtle

# Create the turtle window
window = turtle.Screen()
pen = turtle.Turtle()


# set turtle options
pen.pensize(5)
pen.pencolor("pink")
pen.shape("turtle")
window.bgcolor("lightgreen")
pen.fillcolor("pink")

pen.begin_fill()

# draw the shapes
for side in range(6):
    pen.forward(150)
    pen.left(90)

#while loop executes 3 times to draw a triangle
sides = 4

while sides > 0:
    pen.forward(150)
    pen.left(-120)
    sides = sides - 1
    
    
pen.end_fill()


#wait for user to close window
window.mainloop()