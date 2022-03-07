# Kim Schalk
# 08/03/2022
# Export Window Framework

# Import Libraries
from tkinter import *

# Window Colours
background_colour = "#F6B26B"
button_colour = "#F4CCCC"
active_button_colour = "#EA9999"
entry_colour = "#FCE5CD"

# Create Window
root = Tk()
root.title("Temperature Converter")
# Design window
root.configure(bg=background_colour, padx=10, pady=5)

# Define Labels
export_history_label = Label(root, text="Export History", fg="black", bg=background_colour, font=("Arial", 20, "bold"),
                             justify=CENTER)
export_history_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

export_information_variable = StringVar()
export_information_variable.set("Type in the desired file name and press export to convert the history to a txt file.")
export_information_label = Label(root, textvariable=export_information_variable, fg="black", bg=background_colour,
                                 font=("Arial", 11, "italic"), justify=LEFT, wraplength=310)
export_information_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Define Entries and Variables
file_name_variable = DoubleVar()
file_name_variable.set("")
file_name_entry = Entry(root, textvariable=file_name_variable, fg="black", bg=entry_colour, width=38,
                        font=("Arial", 11), justify=LEFT, bd=3)
file_name_entry.grid(row=2, column=0, columnspan=2, pady=5, padx=10, ipadx=5, ipady=2)

# Define Buttons
export_button = Button(root, text="Export", fg="black", bg=button_colour, activebackground=active_button_colour,
                       font=("Arial", 11), justify=CENTER, width=12)
export_button.grid(row=3, column=0, columnspan=2, pady=20, padx=5, ipadx=2, ipady=2)

back_button = Button(root, text="Back", fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Arial", 11, "underline"), justify=LEFT, bd=0)
back_button.grid(row=4, column=0, pady=(0, 5), padx=5, sticky="w")

help_button = Button(root, text="Help", fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Arial", 11, "underline"), justify=RIGHT, bd=0)
help_button.grid(row=4, column=1, pady=(0, 5), padx=5, sticky="e")

# Close Window
root.mainloop()
