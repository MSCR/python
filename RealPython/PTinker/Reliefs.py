import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
Widgets can be configured with a relief attribute that creates a border around
a frame. This attribute can be set with the following values:
- tk.FLAT: Has no border effect(default value)
- tk.SUNKEN: Creates a sunken effect
- tk.RAISED: Creates a raised effect
- tk.GROOVE: Creates a groove border effect
- tk.RIDGE: Creates a ridget effect
Additionally, to apply the border effect, the attribute borderwidth must be set
to a value greater than 1. This attribute adjust the width of the border in pixels.
"""
border_effects =\
{
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
}

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    # The side attribute tells Tkinter in which direction to pack the frame object
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()