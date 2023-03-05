import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
.grid Geometry Manager
.grid() works by splitting a window or Frame into rows and columns. It
use a row and column indices to the row and column keyword arguments.
Both start in 0.
"""
for i in range(3):
    """
    By using .columnconfigure() and .rowconfigure() on window object, rows and columns
    of the grid can grow as the window is resized. It requires 3 parameters
    - Index. Index of the column or row to be configure or a list of indexes to configure
    multiple rows or columns at the same time
    - Weight. A keyword argument that determines how the column or row should respond to window
    resizing
    - Minimum size. A keyword argument called minsize that sets the minimum size of the row height
    or column width in pixels
    """
    window.columnconfigure(index=i, weight=1, minsize=75)
    window.rowconfigure(index=i, weight=1, minsize=75)

    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        """
        To add some space around each frame, padding can be used on each cell.
        Padding is just some black space that surrounds a widget and visually sets
        its content apart. There are two types of padding,
        - External padding. It adds some space around the outside of a grid cell.
        It can be set using the keyword arguments padx and pady to .grid(). Both
        are measured in pixels. .pack() also has these parametes.
        """
        #frame.grid(row=i, column=j)
        frame.grid(row=i, column=j, padx=5, pady=5)     # NOTE: grid geometry manager attached to master: window
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        #label.pack()
        label.pack(padx=5, pady=5)  # NOTE: pack geometry manager attached to master: frame

window.mainloop()

"""
By default, widgets are centered in their grid cells.
"""

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)

window.mainloop()

"""
This can be change using the sticky parameter, which accepts a string
containint one or more of the following letters:
- "n" or "N" to align to the top-center of the cell
- "e" or "E" to align to the right-center of the cell
- "s" or "S" to align to the bottom-center of the cell
- "w" or "W" to align to the left-center of the cell
"""

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="s")

window.mainloop()

"""
This letters can be combined
"""

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")

window.mainloop()

"""
When a widget is positioned with sticky, the size of the widget is just big
enough to contain any text and other contents inside of it. It won't fill the
entire grid. In order to fill the grid, the widget can force it using "ns" for
vertical position or "ew" for horizontal position.
"""
window = tk.Tk()
window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()