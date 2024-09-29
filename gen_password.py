import random
import string
from tkinter import *
# Function to generate the password
def generate_password():
    password_length_str = entry.get()  # Get the input from the entry widget
    if password_length_str:
        password_length = int(password_length_str)
    else:
        password_length = 8
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_characters) for i in range(password_length))
    password_label.config(text=f"Generated password is: {password}")  # Update label to show password

root = Tk()
root.title("Password Generator")
root.geometry("250x200")
# Entry to input password length
Label(root, text="Enter password length:").pack(pady=10)
entry = Entry(root)
entry.pack(pady=10)
# Button to generate the password
pswrd = Button(root, text="Generate password", font=("Arial", 12, "bold"), command=generate_password,width=15)
pswrd.pack(pady=10)
# Label to display the generated password
password_label = Label(root, text="")
password_label.pack(pady=10)
# Start the GUI loop
root.mainloop()
