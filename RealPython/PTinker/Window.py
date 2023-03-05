import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
Labels
A widget is any element contained in a window, the next code create a Label
but doesn't add it to the previous created window
"""
greeting = tk.Label(text="Hello Tkinter")

"""
To control foreground and background colors, Label widget also accept those values
"""
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",     # Set the text color to white
    background="black"      # Set the background color to black
)

"""
Colors can be specified also in hexadeximal
"""
label2 = tk.Label(text="Hello Tkinter", background="#34A2FE")

"""
There are shorthand names for some parameters
"""
label3 = tk.Label(text="Hello Tkinter", fg="white", bg="black")

"""
Width and height can also be specified, note that the size is text unit
not inches, centimeters or pixels, this is to ensure consistent behaviour of
the application across platforms
"""
label4 = tk.Label(
    text="Hello, Tkinter",
    fg="white",     # Set the text color to white
    bg="black",     # Set the background color to black
    width=10,       # Set width to 10
    height=10       # Set height to 10
)

"""
This command add the Label widget in the window
"""
greeting.pack()
label.pack()
label2.pack()
label3.pack()
label4.pack()

"""
This line run the event loop of Tkinter, this is needed in a python file to run Tkinter.
This method tells Python to run the event loop, then it listens from events, such as
button clicks or keypresses, and blocks any code that comes after it from running until
the window is close.
"""
window.mainloop()

"""
This other method is used to update the windows that is already open
"""
# window.update()
