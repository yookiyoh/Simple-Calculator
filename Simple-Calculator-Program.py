# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 5
# Simple Calculator Program

# General Instructions

# 1: The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication, and Division)
# 2: The application will ask the user for two numbers
# 3: Display the result
# 4: The application will ask is the user wants to try again or not
# 5: If yes, repeat Step 1
# 6: If no, display "Thank you!" and the program will exit
# 7: Use Python Function and appropriate Exceptions to capture errors during runtime

# Pseudocode

# import necessary libraries or modules
import tkinter as tk   # import tkinter for GUI
from tkinter import *
from tkinter import messagebox   # import messagebox for the error message

# define function for arithmetic addition
def addition_num():
    try:
        result = float(num1.get()) + float(num2.get())
        result = round(result, 2)
        labeld.config(text = result)
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for arithmetic subtraction
def subtraction_num():
    try:
        result = float(num1.get()) - float(num2.get())
        result = round(result, 2)
        labeld.config(text = result)
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for arithmetic multiplication
def multiplication_num():
    try:
        result = float(num1.get()) * float(num2.get())
        result = round(result, 2)
        labeld.config(text = result)
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for arithmetic division
def division_num():
    try:
        result = float(num1.get()) / float(num2.get())
        result = round(result, 2)
        labeld.config(text = result)
    except ZeroDivisionError:    # exception for zero division error
        messagebox.showerror('Error detected', 'Error: Cannot divide by zero')
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for clear input
def clear_input():
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)

# define function for reiteration
def reiterate_program():
    clear_input()
    messagebox.showinfo('Retry', 'Please input new values for arithmetic calculations')

# define function for motivation
def motivate_message():
    messagebox.showinfo('?', 'You are worthy. I hope you know that :3\nKeep moving forward!')

# define function for program exit
def exit_program():
    window.destroy()
    messagebox.showinfo('Message', 'Thank you for using this program!')

# create an instance for tkinter window
window = tk.Tk()
window.title("Simple Calculator")   # set title for the window
window.config(bg = "#007FFF")

# create label for first number
label1 = tk.Label(window, text = "First Number: ", font = ("Arial", 15, "bold"), bg = "#536878", fg = "#007FFF")
label1.grid(row = 0, column = 1, padx = 10, pady = 10)

# create textbox for first number input
num1 = tk.Entry(window, font = ("Gotham Black", 14), fg = "#F9E076", justify = CENTER)
num1.grid(row = 0, column = 2)

# create label for second number
label2 = tk.Label(window, text = "Second Number: ", font = ("Arial", 15, "bold"), bg = "#536878", fg = "#007FFF")
label2.grid(row = 1, column = 1, padx = 10)

# create textbox for second number input
num2 = tk.Entry(window, font = ("Gotham Black", 14), fg = "#F9E076", justify = CENTER)
num2.grid(row = 1, column = 2)

# create label for Result
labelr = tk.Label(window, text = "Result: ", font = ("Stylus", 15, "bold"), bg = "#536878", fg = "#007FFF")
labelr.grid(row = 2, column = 1, padx = 10, pady = 10)

# display result output
labeld = tk.Label(window, text = "", font = ("Tahoma", 15, "bold"), bg = "#536878", fg = "#007FFF", justify = CENTER)
labeld.grid(row = 2, column = 2)

# create button for addition operation
button_add = tk.Button(window, text = "Add", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = addition_num)
button_add.grid(row = 3, column = 1, padx = 5, pady = 5)

# create button for subtraction operation
button_sub = tk.Button(window, text = "Subtract", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = subtraction_num)
button_sub.grid(row = 3, column = 2, padx = 5, pady = 5)

# create button for multiplication operation
button_mul = tk.Button(window, text = "Multiply", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = multiplication_num)
button_mul.grid(row = 4, column = 1, padx = 5, pady = 5)

# create button for division operation
button_div = tk.Button(window, text = "Divide", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = division_num)
button_div.grid(row = 4, column = 2, padx = 5, pady = 5)

# create button for clear content
button_clear = tk.Button(window, text = "Clear", width = 11, font = ("Helvetica", 12, "bold"), bg = "#FBEC5D", command = clear_input)
button_clear.grid(row = 5, column = 1, padx = 5, pady = 15)

# create button for reiteration
button_reiterate = tk.Button(window, text = "Try Again", width = 11, font = ("Helvetica", 12, "bold"), bg = "#ED7117", command = reiterate_program)
button_reiterate.grid(row = 5, column = 2, padx = 5, pady= 15)

# create button for motivation
button_motivation = tk.Button(window, text = "?", width = 11, font = ("Helvetica", 12, "bold"), bg = "#5DBB63", command = motivate_message)
button_motivation.grid(row = 6, column = 2, padx = 5, pady= 15)

# create button for program exit
button_exit = tk.Button(window, text = "Exit", width = 11, font = ("Helvetica", 12, "bold"), bg = "#E3242B", command = exit_program)
button_exit.grid(row = 6, column = 1, padx = 5, pady = 15)

# insertion of mainloop in running GUI window
window.mainloop()

# trial testing
# omissions and remodifications of coding elements
# re-editing codes
# testing was successful