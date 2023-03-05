import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
Entry
With entry you can get information from the user in form of text. Creating and
styling an Entry works as Labels and buttons
"""
entry = tk.Entry(fg="yellow", bg="blue", width=50)

"""
There are three ways to get input from a user with entry.
1. Retrieving text with .get()
2. Deleting text with .delete()
3. Inserting text with .insert()
"""
label = tk.Label(text="Name")
entry2 = tk.Entry()

name = entry2.get()

entry2.delete(0)
entry2.delete(0,4)
entry2.delete(0, tk.END)

entry2.insert(0, "Python")
entry2.insert(0, "Real")

"""
This command add the Label widget in the window
"""
entry.pack()
entry2.pack()

"""
This line run the event loop of Tkinter, this is needed in a python file to run Tkinter.
This method tells Python to run the event loop, then it listens from events, such as
button clicks or keypresses, and blocks any code that comes after it from running until
the window is close.
"""
window.mainloop()