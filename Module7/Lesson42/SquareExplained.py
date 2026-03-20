import turtle # Loads Python’s turtle graphics module so we can draw on a screen.

# creating canvas
turtle.Screen().bgcolor("Orange") # Creates a drawing window (screen) and sets its background color to orange.

sc = turtle.Screen() # Stores the screen object in variable sc so you can control it later.
sc.setup(400, 300) # Sets the window size: Width = 400 pixels; Height = 300 pixels

turtle.title("Welcome to Turtle Window") # Sets the title text shown at the top of the window.

# turtle object creation
board = turtle.Turtle() # Creates a turtle object named board. This turtle will draw on the screen.

# creating a square
for i in range(4): # Runs the loop 4 times (because a square has 4 sides).
	board.forward(100) # Moves the turtle forward by 100 units (draws one side).
	board.left(90) # Turns the turtle 90 degrees left. This creates a right angle for the square.
	i = i+1

# Orange background 🟧
# Title: Welcome to Turtle Window
# A square drawn with 4 equal sides ⬜