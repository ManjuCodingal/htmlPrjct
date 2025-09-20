import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())   # get length from user
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

# Main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

# Label + Entry for password length
tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Button to generate password
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Generated Password will appear here")
result_label.pack(pady=10)

# Run app
root.mainloop()
