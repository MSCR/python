import tkinter as tk

"""
Label widget doesn't have a .get() method as Entry or Text,
but the value of the text's label can be retrieved by accessing
the text attribute with a dictionary style subscript notation
"""
def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

"""
Every Button widget has a command attribute that can be
assigned to a function. Whenever the button is pressed,
the function is executed.
"""

window = tk.Tk()
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_decrease = tk.Button(master=window, text="+", command=increase)
btn_decrease.grid(row=0, column=2, sticky="nsew")

window.mainloop()