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
        result = round(result, 4)
        label4.config(text = result)
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for arithmetic subtraction
def subtraction_num():
    try:
        result = float(num1.get()) - float(num2.get())
        result = round(result, 4)
        label4.config(text = result)
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for arithmetic multiplication
def multiplication_num():
    try:
        result = float(num1.get()) * float(num2.get())
        result = round(result, 4)
        label4.config(text = result)
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for arithmetic division
def division_num():
    try:
        result = float(num1.get()) / float(num2.get())
        result = round(result, 4)
        label4.config(text = result)
    except ZeroDivisionError:    # exception for zero division error
        messagebox.showerror('Error detected', 'Error: Cannot divide by zero')
    except ValueError:   # exception for value error
        messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

# define function for clear input
def clear():
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)

# define function for reiteration
def reiterate():
    clear()
    messagebox.showinfo('Retry', 'Please input new values for arithmetic calculations')

# define function for program exit
def exit_program():
    window.destroy()
    messagebox.showinfo('Message', 'Thank you for using this program!')

# create an instance for tkinter window
window = tk.Tk()
window.title("Simple Calculator")   # set title for the window
window.config(bg = "#E0FFFF")

# create label for first number
label1 = Label(window, text = "First Number: ", font = ("Verdana", 15.7, "Bold"), bg = "#536878", fg = "F0FFFF")
label1.grid(row = 0, column = 1, padx = 10, pady = 10)

# create textbox for first number input
num1 = Entry(window, font = ("Gotham Black", 14), fg = "#F9E076", justify = CENTER)
num1.grid(row = 0, column = 2)

# create label for second number
label2 = Label(window, text = "Second Number: ", font = ("Verdana", 15.7, "Bold"), bg = "#536878", fg = "#F0FFFF")
label2.grid(row = 1, column = 1, padx = 10)

# create textbox for second number input
num2 = Entry(window, font = ("Gotham Black", 14), fg = "F9E076", justify = CENTER)
num2.grid(row = 1, column = 2)

# create label for Result
labelr = Label(window, text = "Result: ", font = ("Stylus", 15, "Bold"), bg = "536878", fg = "F0FFFF")
labelr.grid(row = 2, column = 1, padx = 10, pady = 10)

# display result output
labeld = Label(window, text = "", font = ("Tahoma", 14.5, "Bold"), bg = "536878", fg = "F0FFFF", justify = CENTER)
labeld.grid(row = 2, column = 2)

# create button for addition operation
button_add = Button(window, text = "Add", width = 10.5, font = ("Futura", 14, "Bold"), bg = "#BDA55D", command = addition_num)
button_add.grid(row = 3, column = 1, padx= 15, pady = 5)

# create button for subtraction operation
button_sub = Button(window, text = "Subtract", width = 10.5, font = ("Futura", 14, "Bold"), bg = "#BDA55D", command = subtraction_num)
button_sub.grid(row = 3, column = 2, padx = 5, pady = 5)

# create button for multiplication operation
button_mul = Button(window, text = "Multiply", width = 10.5, font = ("Futura", 14, "Bold"), bg = "#BDA55D", command = multiplication_num)
button_mul.grid(row = 4, column = 1, padx = 5, pady = 5)

# create button for division operation
button_div = Button(window, text = "Divide", width = 10.5, font = ("Futura", 14, "Bold"), bg = "#BDA55D", command = division_num)
button_div.grid(row = 4, column = 2, padx = 5, pady = 5)

# create button for clear content
button_clear = Button(window, text = "Clear", width = 10.5, font = ("Helvetica", 12, "Bold"), bg = "#FBEC5D", command = clear)
button_clear.grid(row = 5, column = 1, padx = 5, pady = 20)

# create button for reiteration
button_reiterate = Button(window, text = "Try Again", width = 10.5, font = ("Helvetica", 12, "Bold"), bg = "#ED7117", command = reiterate)
button_reiterate.grid(row = 5, column = 1, padx = 5, pady= 20)

# create button for program exit
button_exit = Button(window, text = "Exit", width = 10.5, font = ("Helvetica", 12, "Bold"), bg = "#E3242B", command = exit_program)
button_exit.grid(row = 5, column = 1, padx = 5, pady = 20)

# insertion of mainloop in running GUI window
window.mainloop()