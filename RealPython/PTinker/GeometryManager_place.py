import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
.place Geometry manager
This geometry manager helps to control the precise location that a widget
should occupy in a window or Frame. It needs two arguments, x and y, which
specify x- and y-coordinates for the top-left corner of the widget. Both
are measured in pixels, not text units
Remember that the origin of x and y is 0 and it's in the top left corner of
the Frame or window
"""
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")

label1.place(x=0, y=0)
label2.place(x=75, y=75)

"""
.place() has some drawbacks
- Layout can be difficult to manage with .place(). This is specially true if
the application has lots of widgets
- Layouts created with .place() aren't responsive. They don't change as the window
is resized
"""

window.mainloop()