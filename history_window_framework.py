# Kim Schalk
# 07/03/2022
# History Window Framework

# Import libraries
from tkinter import *
from tkinter import ttk

# Colours for program
background_colour = "#F6B26B"
button_colour = "#F4CCCC"
active_button_colour = "#EA9999"

# Define Window
root = Tk()
root.title("Temperature Converter")
# Design window
root.configure(bg=background_colour)

# Define Labels
history_label = Label(root, text="History", fg="black", bg=background_colour, font=("Arial", 20, "bold"),
                      justify=CENTER)
history_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

history_information_one = StringVar()
history_information_one.set("")

history_information_one_label = Label(root, textvariable=history_information_one, fg="black", bg=background_colour,
                                      font=("Arial", 11), wraplength=50)
history_information_one_label.grid(row=1, column=0, padx=5, pady=5)

history_information_two = StringVar()
history_information_two.set("")

history_information_two_label = Label(root, textvariable=history_information_two, fg="black", bg=background_colour,
                                      font=("Arial", 11), wraplength=50)
history_information_two_label.grid(row=1, column=2, padx=5, pady=5)

# Define Buttons
export_button = Button(root, text="Export", fg="black", bg=button_colour, width=8, font=("Arial", 11),
                       activebackground=active_button_colour)
export_button.grid(row=2, column=0, pady=(15, 5), padx=5, ipadx=2, ipady=2)

clear_button = Button(root, text="Clear", fg="black", bg=button_colour, width=8, font=("Arial", 11),
                      activebackground=active_button_colour)
clear_button.grid(row=2, column=2, pady=(15, 5), padx=5, ipadx=2, ipady=2)

back_button = Button(root, text="Back", fg="black", bg=background_colour, bd=0, font=("Arial", 11, "underline"),
                     justify=LEFT, activebackground=background_colour)
back_button.grid(row=3, column=0, pady=5, padx=(5, 50))

help_button = Button(root, text="Help", fg="black", bg=background_colour, bd=0, font=("Arial", 11, "underline"),
                     justify=RIGHT, activebackground=background_colour)
help_button.grid(row=3, column=2, pady=5, padx=(50, 5))

# Add line as a separator
# Style separator
line_style = ttk.Style()
line_style.configure("Line.TSeparator", background="black")
line = ttk.Separator(root, orient=VERTICAL, style="Line.TSeparator")
line.grid(row=1, column=1, sticky="ns")

# Close Window
root.mainloop()
