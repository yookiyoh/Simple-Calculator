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

# create textbox for first number input

# create label for second number

# create textbox for second number input

# create label for Result

# display result output

# create button for addition operation

# create button for subtraction operation

# create button for multiplication operation

# create button for division operation

# create button for clear content

# create button for reiteration

# create button for program exit

# insertion of mainloop in running GUI window

