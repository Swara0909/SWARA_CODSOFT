import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x450")
root.resizable(False, False)
custom_title = tk.Label(root, text="Welcome to my Calculator!", font=("Arial", 15,"italic"),fg="red")
custom_title.pack(pady=10)

# Global variable to store the expression
expression = ""

# Function to update the expression in the input field
def update_expression(symbol):
    global expression
    expression += str(symbol)
    input_text.set(expression)

# Function to clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression and show the result
def calculate():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)  # Set the result in the input field
        expression = result  # Save result for further calculations
    except:
        input_text.set("Error")
        expression = ""

# Input field to display the expression and results
input_text = tk.StringVar()

input_frame = tk.Frame(root, width=400, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side="top")

input_field = tk.Entry(input_frame, font=("Arial", 24), textvariable=input_text, width=50, bg="#eee", bd=0, justify="right")
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)  # Internal padding to increase height

# Create a frame for the buttons
btns_frame = tk.Frame(root, width=400, height=500, bg="grey",highlightbackground="black", highlightcolor="black", highlightthickness=2)
btns_frame.pack()

# First row
clear_btn = tk.Button(btns_frame,font=("Arial",9,"bold"),text="C", fg="black", width=32, height=3, bd=0, bg="#fff", cursor="hand2", command=clear)
clear_btn.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide_btn = tk.Button(btns_frame, font=("Arial",9,"bold"),text="/", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: update_expression("/"))
divide_btn.grid(row=0, column=3, padx=1, pady=1)

# Second row
btn7 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(7))
btn7.grid(row=1, column=0, padx=1, pady=1)

btn8 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(8))
btn8.grid(row=1, column=1, padx=1, pady=1)

btn9 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(9))
btn9.grid(row=1, column=2, padx=1, pady=1)

multiply_btn = tk.Button(btns_frame,font=("Arial",9,"bold"), text="*", fg="black", width=10, height=3, bd=0, bg="#FFF", cursor="hand2", command=lambda: update_expression("*"))
multiply_btn.grid(row=1, column=3, padx=1, pady=1)

# Third row
btn4 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(4))
btn4.grid(row=2, column=0, padx=1, pady=1)

btn5 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(5))
btn5.grid(row=2, column=1, padx=1, pady=1)

btn6 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(6))
btn6.grid(row=2, column=2, padx=1, pady=1)

minus_btn = tk.Button(btns_frame,font=("Arial",9,"bold"), text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression("-"))
minus_btn.grid(row=2, column=3, padx=1, pady=1)

# Fourth row
btn1 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(1))
btn1.grid(row=3, column=0, padx=1, pady=1)

btn2 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(2))
btn2.grid(row=3, column=1, padx=1, pady=1)

btn3 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(3))
btn3.grid(row=3, column=2, padx=1, pady=1)

plus_btn = tk.Button(btns_frame,font=("Arial",9,"bold"), text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression("+"))
plus_btn.grid(row=3, column=3, padx=1, pady=1)

# Fifth row
btn0 = tk.Button(btns_frame,font=("Arial",9,"bold"), text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression(0))
btn0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

decimal_btn = tk.Button(btns_frame, text=".",font=("Arial",9,"bold"), fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: update_expression("."))
decimal_btn.grid(row=4, column=2, padx=1, pady=1)

equals_btn = tk.Button(btns_frame, text="=",font=("Arial",9,"bold"), fg="black", width=10, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=calculate)
equals_btn.grid(row=4, column=3, padx=1, pady=1)

# Run the application
root.mainloop()
