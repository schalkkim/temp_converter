# Kim Schalk
# 14/03/2022
# Rounding

# Import Packages
from tkinter import *
from PIL import Image, ImageTk

# Variable for button last pressed
last_button = 0

# Colours for program
background_colour = "#F6B26B"
button_colour = "#F4CCCC"
active_button_colour = "#EA9999"
entry_colour = "#FCE5CD"
checkbox_colour = "#D9D9D9"
box_colour = "#FCE5CD"

# Define Window
root = Tk()
root.title("Temperature Converter")
# Design Window
root.configure(bg=background_colour)


# Define Functions
# Help Window Function
def go_to_help():
    # Close help window function and enables help button
    def close_help():
        help_button.config(state=NORMAL)
        help_window.destroy()
    # Disable help button
    help_button.config(state=DISABLED)
    # Create help window
    help_window = Toplevel()
    help_window.configure(bg=background_colour)
    # Closes help window and enables help button when X is pressed
    help_window.protocol("WM_DELETE_WINDOW", close_help)
    # Define Frames
    # Groups the help information
    information_frame = Frame(help_window, bg=box_colour, bd=3)
    information_frame.grid(row=1, column=0, padx=20, pady=(10, 15), stick="nw")
    information_frame.grid_rowconfigure(0, weight=1)
    information_frame.grid_columnconfigure(0, weight=1)
    information_frame.grid_propagate(False)

    # Add canvas, so scrollbar can be added
    information_canvas = Canvas(information_frame, bg=box_colour)
    information_canvas.grid(row=0, column=0, sticky="news")

    # Create Scrollbar
    information_scrollbar = Scrollbar(information_frame, orient="vertical", command=information_canvas.yview)
    information_scrollbar.grid(row=0, column=1, stick="ns", padx=5, pady=5)

    information_canvas.configure(yscrollcommand=information_scrollbar.set)

    # Add a frame for the information labels
    information_labels_frame = Frame(information_canvas, bg=box_colour)
    information_canvas.create_window((0, 0), window=information_labels_frame, anchor="nw")

    # Define Labels
    help_label = Label(help_window, text="Help", fg="black", bg=background_colour, font=("Arial", 20, "bold"),
                       justify=CENTER)
    help_label.grid(row=0, column=0, padx=5, pady=(10, 0), ipadx=2, ipady=2)

    information_textvariable = StringVar()
    information_textvariable.set("""Enter a number into one of the boxes (either Centigrade or Fahrenheit), press convert to view the conversion which will appear in the other box (either Fahrenheit or Centigrade).

If an error appears, check that your number is in the format ‘7’ rather than ‘seven’. Also check that your number is not lower than absolute 0 (-273.15℃ or -459.67℉).

To exit, press the ‘x’ at the top of the window, this will close the program.
    """)
    information_label = Label(information_labels_frame, textvariable=information_textvariable, bg=box_colour, bd=0,
                              fg="black", font=("Arial", 11), wraplength=260, justify=LEFT)
    information_label.grid(row=0, column=0)

    history_label = Label(information_labels_frame, text="History", bg=box_colour, bd=0, fg="black",
                          font=("Arial", 11, "bold"), justify=LEFT)
    history_label.grid(row=1, column=0, padx=(0, 205))

    history_information_textvariable = StringVar()
    history_information_textvariable.set("""Press ‘View history’ to see your last 8 conversions. To view more you can export your history by pressing the ‘Export’ button. Once in that window type in your filename and press export. Your file will appear in the folder where this program is located. 

To clear your history, press the ‘Clear’ button. This will delete your history from the program, however, if you have a file saved, the history will not be deleted from there. You will have to delete the file by going to the folder it is located in and deleting it there.

When finished press the back button to return to the home window.""")
    history_information_label = Label(information_labels_frame, textvariable=history_information_textvariable,
                                      bg=box_colour, bd=0, fg="black", font=("Arial", 11), wraplength=260, justify=LEFT)
    history_information_label.grid(row=2, column=0)

    # Define Button
    back_button = Button(help_window, text="Back", fg="black", bg=background_colour, bd=0,
                         font=("Arial", 11, "underline"), justify=LEFT, activebackground=background_colour,
                         command=close_help)
    back_button.grid(row=2, column=0, padx=(10, 285), pady=(5, 10))

    # Allows resizing of labels
    information_labels_frame.update_idletasks()

    # Change size of the box
    information_frame.config(width=310, height=350)

    # Set scrolling region
    information_canvas.config(scrollregion=information_canvas.bbox("all"))


# Celsius to Fahrenheit Function
def celsius_to_fahrenheit():
    last_button = 1
    centigrade = centigrade_variable.get()
    centigrade = int(centigrade)
    fahrenheit = (centigrade * 9/5) + 32
    fahrenheit_variable.set(fahrenheit)


# Fahrenheit to Celsius Function
def fahrenheit_to_celsius():
    last_button = 2
    fahrenheit = fahrenheit_variable.get()
    fahrenheit = int(fahrenheit)
    centigrade = (fahrenheit - 32) * 5/9
    centigrade_variable.set(centigrade)


# Round to last 0 in number Function
def round_0s(last_converted):
    number = last_converted.get()
    # If a whole number, round to an integer
    if number % 1 == 0:
        number = int(number)
    else:
        number = str(number)
        number_length = len(number)
        # Remove extra zeros at the end
        for zero in range(number_length):
            if number[-zero] == "0":
                number.pop()
            else:
                break
        # Find number of decimal places
        for decimal in range(number_length):
            if number[decimal] == ".":
                decimal_place = decimal
        # If less than 4dp, print number
        if number_length - (decimal_place + 1) < 4:
            number = float(number)
            print(number)
        # If greater than 4dp, round to 4dp
        else:
            number = float(number)
            number = "{:.4f}".format(number)
    last_converted.set(number)


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
temperature_converter_label = Label(top_frame, text="Temperature Converter", fg="black", bg=background_colour,
                                    font=("Arial", 20, "bold"))
temperature_converter_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

instruction_label = Label(top_frame, text="Type in a number and push the 'convert' button to convert it.",
                          fg="black", bg=background_colour, font=("Arial", 12, "italic"), wraplength=375, justify=LEFT)
instruction_label.grid(row=1, column=0, columnspan=3, padx=20, pady=5)

centigrade_label = Label(middle_frame, text="Centigrade (°C)", fg="black", bg=background_colour,
                         font=("Arial", 11, "bold"), wraplength=100, justify=RIGHT)
centigrade_label.grid(row=1, column=0)

fahrenheit_label = Label(middle_frame, text="Fahrenheit (°F)", fg="black", bg=background_colour,
                         font=("Arial", 11, "bold"), wraplength=100, justify=LEFT)
fahrenheit_label.grid(row=1, column=2)

formula_label = Label(bottom_frame, text="Formula", fg="black", bg=background_colour, font=("Arial", 11, "italic"),
                      justify=CENTER)
formula_label.grid(row=0, column=1, padx=(50, 100))

# Define Entries and Variables
centigrade_variable = DoubleVar()
centigrade_variable.set("")
centigrade_entry = Entry(middle_frame, textvariable=centigrade_variable, width=9, bg=entry_colour, fg="black",
                         font=("Arial", 11), justify=CENTER, bd=3)
centigrade_entry.grid(row=2, column=0, pady=5, ipady=5, ipadx=5)

fahrenheit_variable = DoubleVar()
fahrenheit_variable.set("")
fahrenheit_entry = Entry(middle_frame, textvariable=fahrenheit_variable, width=9, bg=entry_colour, fg="black",
                         font=("Arial", 11), justify=CENTER, bd=3)
fahrenheit_entry.grid(row=2, column=2, pady=5, ipady=5, ipadx=5)

# Define Buttons
centigrade_convert_button = Button(middle_frame, text="Convert", fg="black", bg=button_colour, width=8,
                                   font=("Arial", 11), activebackground=active_button_colour,
                                   command=celsius_to_fahrenheit)
centigrade_convert_button.grid(row=3, column=0, pady=(5, 40), ipadx=2, ipady=2)

fahrenheit_convert_button = Button(middle_frame, text="Convert", fg="black", bg=button_colour, width=8,
                                   font=("Arial", 11), activebackground=active_button_colour, command=fahrenheit_to_celsius)
fahrenheit_convert_button.grid(row=3, column=2, pady=(5, 40), ipadx=2, ipady=2)

view_history_button = Button(bottom_frame, text="View History", fg="black", bg=background_colour, bd=0,
                             font=("Arial", 11, "underline"), justify=LEFT, activebackground=background_colour)
view_history_button.grid(row=2, column=0, padx=(10, 2), pady=(5, 10))

help_button = Button(bottom_frame, text="Help", fg="black", bg=background_colour, bd=0, font=("Arial", 11, "underline"),
                     justify=RIGHT, activebackground=background_colour, command=go_to_help)
help_button.grid(row=2, column=2, padx=(2, 10), pady=(5, 10))

# Define Image and format it
original_thermometer_image = Image.open("thermometer_image.png")
resized_thermometer_image = original_thermometer_image.resize((140, 150), Image.ANTIALIAS)
thermometer_image = ImageTk.PhotoImage(resized_thermometer_image)

image_label = Label(middle_frame, image=thermometer_image, bd=0)
image_label.image = thermometer_image
image_label.grid(row=0, column=1, rowspan=7, padx=5)

# Define Checkbutton
rounded_number_checkbutton = Checkbutton(bottom_frame, text="Rounded number", fg="black", bg=background_colour,
                                         font=("Arial", 11), justify=CENTER, bd=3, selectcolor=checkbox_colour,
                                         activebackground=background_colour)
rounded_number_checkbutton.grid(row=1, column=1, padx=(25, 75), pady=5)

# End of window
root.mainloop()
