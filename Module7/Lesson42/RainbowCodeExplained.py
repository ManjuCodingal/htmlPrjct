import turtle 
t = turtle.Turtle() # Creates a turtle object t (this is the pen that draws).
s = turtle.Screen() # Creates the screen (window) where drawing happens.
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] # A list of colors used for the rainbow effect.
s.bgcolor('black')  # Sets the background color to black (so colors stand out).
t.speed('fastest') # Sets drawing speed to maximum.
t.hideturtle() # Hides the turtle cursor (so only the drawing is visible).
while True: # Runs the drawing continuously (infinite animation).
  for x in range(200):  # Runs from 0 to 199.Controls how big and long the spiral grows.
    t.pencolor(colors[x%len(colors)])
#     Changes color each step.
# x % len(colors) cycles through the color list repeatedly.
# 👉 Example:
# 0 → red
# 1 → purple
# 2 → blue
# ... repeats again
    t.width(x/100 + 1) # Gradually increases pen thickness.Starts thin, gets thicker as x increases.
    t.forward(x)  # Moves forward by x units. Each step is longer than the previous → creates spiral growth.
    t.left(59) # Turns left by 59 degrees. This angle creates the spiral pattern.
  t.right(239)  # Rotates the turtle to prepare for drawing back (erasing effect). 239° is chosen to align with the spiral shape.
  for x in range(200, 0, -1): # Counts backward from 200 to 1. Retraces the spiral in reverse.
    t.pencolor('black') # Draws with black color (same as background). This makes it look like the spiral is being erased.
    t.width(x/100 + 7) # Uses a thicker pen to fully cover the previous lines.
    t.forward(x) # Moves forward again along the same path.
    t.right(59) # Turns right (opposite direction of earlier left turns). Helps retrace the spiral path.

# Increasing step size → spiral grows outward
# Angle (59°) → creates symmetry
# Color cycling → rainbow effect
# Erasing loop → animation illusion