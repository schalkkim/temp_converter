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
help_label = Label(root, text="Help", fg="black", bg=background_colour, font=("Arial", 20, "bold"), justify=CENTER)
help_label.grid(row=0, column=0, padx=5, pady=(10, 0), ipadx=2, ipady=2)

information_textvariable = StringVar()
information_textvariable.set("""Enter a number into one of the boxes (either Centigrade or Fahrenheit), press convert to view the conversion which will appear in the other box (either Fahrenheit or Centigrade).

If an error appears, check that your number is in the format ‘7’ rather than ‘seven’. Also check that your number is not lower than absolute 0 (-273.15℃ or -459.67℉).

To exit, press the ‘x’ at the top of the window, this will close the program.
""")
information_label = Label(information_labels_frame, textvariable=information_textvariable, bg=box_colour, bd=0, fg="black",
                          font=("Arial", 11), wraplength=260, justify=LEFT)
information_label.grid(row=0, column=0)

history_label = Label(information_labels_frame, text="History", bg=box_colour, bd=0, fg="black", font=("Arial", 11, "bold"),
                      justify=LEFT)
history_label.grid(row=1, column=0, padx=(0, 205))

history_information_textvariable = StringVar()
history_information_textvariable.set("""Press ‘View history’ to see your last 8 conversions. To view more you can export your history by pressing the ‘Export’ button. Once in that window type in your filename and press export. Your file will appear in the folder where this program is located. 

To clear your history, press the ‘Clear’ button. This will delete your history from the program, however, if you have a file saved, the history will not be deleted from there. You will have to delete the file by going to the folder it is located in and deleting it there.

When finished press the back button to return to the home window.""")
history_information_label = Label(information_labels_frame, textvariable=history_information_textvariable, bg=box_colour, bd=0,
                                  fg="black", font=("Arial", 11), wraplength=260, justify=LEFT)
history_information_label.grid(row=2, column=0)

# Define Button
back_button = Button(root, text="Back", fg="black", bg=background_colour, bd=0, font=("Arial", 11, "underline"),
                     justify=LEFT, activebackground=background_colour)
back_button.grid(row=2, column=0, padx=(10, 285), pady=(5, 10))

# Allows resizing of labels
information_labels_frame.update_idletasks()

# Change size of the box
information_frame.config(width=310, height=350)

# Set scrolling region
information_canvas.config(scrollregion=information_canvas.bbox("all"))

# Close window
root.mainloop()
