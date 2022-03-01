# Kim Schalk
# 01/03/2022
# Help Window Framework

# Import Packages
from tkinter import *

# Colours for program
background_colour = "#F6B26B"
box_colour = "#FCE5CD"

# Define Window
root = Tk()
root.title("Temperature Converter")
# Design Window
root.configure(bg=background_colour)

# Define Frames
# Groups the help information
information_frame = Frame(root, bg=box_colour, bd=3)
information_frame.grid(row=1, column=0, padx=15, pady=(10, 15), stick="nw")

# Define Labels
help_label = Label(root, text="Help", fg="black", bg=background_colour, font=("Arial", 20, "bold"), justify=CENTER)
help_label.grid(row=0, column=0, padx=5, pady=(10, 0), ipadx=2, ipady=2)

information_textvariable = StringVar()
information_textvariable.set("""Enter a number into one of the boxes (either Centigrade or Fahrenheit), press convert to view the conversion which will appear in the other box (either Fahrenheit or Centigrade).

If an error appears, check that your number is in the format ‘7’ rather than ‘seven’. Also check that your number is not lower than absolute 0 (-273.15℃ or -459.67℉).

To exit, press the ‘x’ at the top of the window, this will close the program.
""")
information_label = Label(information_frame, textvariable=information_textvariable, bg=box_colour, bd=0, fg="black",
                          font=("Arial", 11), wraplength=300, justify=LEFT)
information_label.grid(row=0, column=0)

history_label = Label(information_frame, text="History", bg=box_colour, bd=0, fg="black", font=("Arial", 11, "bold"),
                      justify=LEFT)
history_label.grid(row=1, column=0, padx=(0, 245))

history_information_textvariable = StringVar()
history_information_textvariable.set("""Press ‘View history’ to see your last 8 conversions. To view more you can export your history by pressing the ‘Export’ button. Once in that window type in your filename and press export. Your file will appear in the folder where this program is located. 

To clear your history, press the ‘Clear’ button. This will delete your history from the program, however, if you have a file saved, the history will not be deleted from there. You will have to delete the file by going to the folder it is located in and deleting it there.

When finished press the back button to return to the home window.""")
history_information_label = Label(information_frame, textvariable=information_textvariable, bg=box_colour, bd=0,
                                  fg="black", font=("Arial", 11), wraplength=300, justify=LEFT)
history_information_label.grid(row=2, column=0)

# Define Button
back_button = Button(root, text="Back", fg="black", bg=background_colour, bd=0, font=("Arial", 11, "underline"),
                     justify=LEFT, activebackground=background_colour)
back_button.grid(row=2, column=0, padx=(10, 275), pady=(5, 10))

# Close window
root.mainloop()
