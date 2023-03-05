import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
Buttons
Buttons and labels are very similar, a button is a label that can be clicked.
The same arguments used in Label works for buttons
"""
button = tk.Button(
    text="Click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)

"""
This command add the Label widget in the window
"""
button.pack()

"""
This line run the event loop of Tkinter, this is needed in a python file to run Tkinter.
This method tells Python to run the event loop, then it listens from events, such as
button clicks or keypresses, and blocks any code that comes after it from running until
the window is close.
"""
window.mainloop()