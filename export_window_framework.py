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
root.configure(bg=background_colour)

# Define Labels
export_history_label = Label(root, text="Export History", fg="black", bg=background_colour, font=("Arial", 20, "bold"),
                             justify=CENTER)
export_history_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

export_information_variable = StringVar()
export_information_variable.set("Type in the desired file name and press export to convert the history to a txt file.")
export_information_label = Label(root, textvariable=export_information_variable, fg="black", bg=background_colour,
                                 font=("Arial", 11, "italic"), justify=LEFT, wraplength=350)
export_information_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Close Window
root.mainloop()
