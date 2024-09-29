import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    result_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        messagebox.showinfo("Result", "It's a tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
        messagebox.showinfo("Result", "You win!")
    else:
        messagebox.showinfo("Result", "Computer wins!")

# Setting up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
instruction_label.pack(pady=20)

rock_button = tk.Button(root, text="Rock", font=("Helvetica", 12), width=15, command=lambda: play('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=("Helvetica", 12), width=15, command=lambda: play('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=("Helvetica", 12), width=15, command=lambda: play('Scissors'))
scissors_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the main loop
root.mainloop()

