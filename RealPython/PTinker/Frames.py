import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
Frame widgets are important for organizing the layout of your widgets in an
application.
.pack() methods packs the frame into the window so taht the window size itself
as small as possible to encompass the frame. An empty Frame widget is practically
invisible. Frames are best thought of as containers for other widgets.
Using the widget's attribute master, the widget can be assigned to a frame.
If the master argument is missing when creating a new widget instance, then
it'll be placed inside of the top-level window by default.
"""
# Create frames
frame_a = tk.Frame()
frame_b = tk.Frame()

# Create Label a and assign it to frame a
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

# Create Label b and assign it to frame b
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Pack frames to window
frame_a.pack()
frame_b.pack()

"""
Frame widgets are great for organzing widgets in a logical manner. Related
widgets can be assigned to the same fram so that, if the frame is ever moved
in the window, then the related widgets stay together.
"""

window.mainloop()