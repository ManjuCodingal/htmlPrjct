import turtle # Imports the turtle module.

turtle.Screen().bgcolor("Orange") # Creates a window and sets the background color to orange.
board = turtle.Turtle() # Creates a turtle named board that will draw on the screen.
 
# first triangle for star
board.forward(100) # draw base
# Moves forward 100 units (first side of triangle). 

board.left(120) # Turns left 120°. (Exterior angle)
board.forward(100) # Draws second side.
 
board.left(120) # Turns left again.
# 👉 Each angle is 120° because:
# Exterior angle of an equilateral triangle = 120°
board.forward(100) # Draws third side → completes an equilateral triangle.
 
# 🚫 Move without drawing 
board.penup() # Lifts the pen → turtle moves without drawing.
board.right(150) # Rotates right 150° to reposition for the second triangle.
board.forward(50) # Moves forward to a new position (center of star).
 
# second triangle for star (inverted)
board.pendown() # Puts the pen down → drawing resumes.
board.right(90) # Turns right 90° to orient the second triangle.
board.forward(100) # Draws first side.
 
board.right(120) # Turns right 120°.
board.forward(100) # Draws second side.
 
board.right(120) # Turns right again.
board.forward(100) # Draws third side → completes second triangle.
 
turtle.done() # Keeps the window open until you close it manually.

# ⭐ What the program creates
# First triangle ▲
# Second inverted triangle ▼
# Together they form a star shape (✡)

# forward() → draws lines
# left() / right() → changes direction
# penup() → move without drawing
# pendown() → draw again