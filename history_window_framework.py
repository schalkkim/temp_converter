# Kim Schalk
# 07/03/2022
# History Window Framework

# Import libraries
from tkinter import *

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
history_information_two_label.grid(row=1, column=3, padx=5, pady=5)

# Close Window
root.mainloop()
