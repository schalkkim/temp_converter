# Kim Schalk
# 24/02/2022
# Version 1 - Framework

# Import Packages
from tkinter import *
from PIL import Image, ImageTk

# Colours for program
background_colour = "#F6B26B"
button_colour = "#F4CCCC"
entry_colour = "#FCE5CD"

# Define Window
root = Tk()
root.title("Temperature Converter")
    # Design Window
root.configure(bg=background_colour)

# Define Frames
    # Groups the title, and the instructions
top_frame = Frame(root, bg=background_colour)
top_frame.grid(row=0, column=0, sticky="NSEW", pady=10)

    # Groups the centigrade and fahrenheit labels, entries, and buttons, as well as the image
middle_frame = Frame(root, bg=background_colour)
middle_frame.grid(row=1, column=0, padx=15, pady=10)

    # Groups the formula, rounded number and view history and help components
bottom_frame = Frame(root, bg=background_colour)
bottom_frame.grid(row=2, column=0)

# Define Labels
temperature_converter_label = Label(top_frame, text="Temperature Converter", fg="black", bg=background_colour, font=("Arial", 20, "bold"))
temperature_converter_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

instruction_label = Label(top_frame, text="Type in a number and push the 'convert' button to convert it.", fg="black", bg=background_colour, font=("Arial", 12, "italic"), wraplength=375, justify=LEFT)
instruction_label.grid(row=1, column=0, columnspan=3, padx=20, pady=5)

centigrade_label = Label(middle_frame, text="Centigrade (°C)", fg="black", bg=background_colour, font=("Arial", 11, "bold"), wraplength=100, justify=RIGHT)
centigrade_label.grid(row=1, column=0)

fahrenheit_label = Label(middle_frame, text="Fahrenheit (°F)", fg="black", bg=background_colour, font=("Arial", 11, "bold"), wraplength=100, justify=LEFT)
fahrenheit_label.grid(row=1, column=2)

# Define Entries and Variables
centigrade_variable = DoubleVar()
centigrade_variable.set("")
centigrade_entry = Entry(middle_frame, textvariable=centigrade_variable, width=9, bg=entry_colour, fg="black", font=("Arial", 11), justify=CENTER, bd=3)
centigrade_entry.grid(row=2, column=0, pady=5, ipady=5, ipadx=5)

fahrenheit_variable = DoubleVar()
fahrenheit_variable.set("")
fahrenheit_entry = Entry(middle_frame, textvariable=fahrenheit_variable, width=9, bg=entry_colour, fg="black", font=("Arial", 11), justify=CENTER, bd=3)
fahrenheit_entry.grid(row=2, column=2, pady=5, ipady=5, ipadx=5)

# Define Buttons
centigrade_convert_button = Button(middle_frame, text="Convert", fg="black", bg=button_colour, width=8, font=("Arial", 11))
centigrade_convert_button.grid(row=3, column=0, pady=5, ipadx=2, ipady=2)

fahrenheit_convert_button = Button(middle_frame, text="Convert", fg="black", bg=button_colour, width=8, font=("Arial", 11))
fahrenheit_convert_button.grid(row=3, column=2, pady=5, ipadx=2, ipady=2)

#End of window
root.mainloop()