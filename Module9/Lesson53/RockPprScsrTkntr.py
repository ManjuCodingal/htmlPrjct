import tkinter as tk
import random

# Function to play the game
def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"

    if user_choice == computer_choice:
        result_text += "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_text += "🎉 You Win!"
    else:
        result_text += "😢 Computer Wins!"

    result_label.config(text=result_text)


# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

# Heading
heading = tk.Label(root, text="Rock, Paper, Scissors!", font=("Arial", 14, "bold"))
heading.pack(pady=10)

# Buttons for user choice
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="Rock ✊", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

# Use of lambda?
# In Tkinter, the command option expects a function reference (not the result of a function).
# But our function play() needs an argument ("Rock", "Paper", or "Scissors").
# If we just wrote command=play("Rock"), Python would call the function immediately when the button is created, instead of waiting for the click. ❌
# So we use lambda to create an anonymous (inline) function that calls play("Rock") only when clicked.

paper_btn = tk.Button(btn_frame, text="Paper ✋", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors ✌️", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12), wraplength=250, justify="center")
result_label.pack(pady=20)

# Run app
root.mainloop()
