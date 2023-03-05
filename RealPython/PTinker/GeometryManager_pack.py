import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
Application layout in TKinter is controlled with geometry managers. There are
three geometry managers:
- .pack()
- .place()
- .grid()
Each window or Frame can use only one geometry manager. However, different frames
can use different geometry managers, even if they're assigned to a frame or
window using another geometry manager.

.pack Geometry manager
It use a packing algorithm to place widgets in a Frame or window in a specified
order. It has two primary steps
- Compute a rectangular are called a parcel that's just tall(or wide) enough to
hold the widget and fills the remaining width(or height) in the window with
blank space.
- Center the widget in the parcel unless a different location is specified
"""
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")

#frame1.pack()
#frame2.pack()
#frame3.pack()
"""
.pack accepts the argument fill to specify in which direction the frames should
be fill.
- tk.X: to fill in the horizontal direction
- tk.Y: to fill in the vertical direction
- tk.BOTH: to fill in both directions
Depending on the fill attribute, height and weight could be not necessary.
Additionally, the fill attribute is responsive to window resizing
"""
#frame1.pack(fill=tk.X)
#frame2.pack(fill=tk.X)
#frame3.pack(fill=tk.X)

"""
The side keyworkd argument of .pack() specifies on which side of the window the
widget should be placed.
- tk.TOP (default value)
- tk.BOTTOM
- tk.LEFT
- tk.RIGHT
"""
#frame1.pack(fill=tk.Y, side=tk.LEFT)
#frame2.pack(fill=tk.Y, side=tk.LEFT)
#frame3.pack(fill=tk.Y, side=tk.LEFT)

"""
To make the layout tryly responsive, an initial size for the frame need to be set
using the width and height attributes. Then, set the fill keyword argument of
.pack() to tk.BOTH and set the expand keyboard argument to true
"""
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()