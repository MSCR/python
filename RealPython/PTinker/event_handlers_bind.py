import tkinter as tk

# Create a window object
window = tk.Tk()

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

"""
To call an event handler whenever an event occurs on a widget, use
.bind(). The event handler is said to be bound to the event because
it's called every time the event occurs. It takes at least two
arguments:
- An event that's represented by a string of the form "<event_name>",
where event_name can be any of Tkinter events
- An event handler that's the name of the function to be called
whenever the event occurs.
When the event handler is called, the event object is passed to the
event handler function.
"""
window.bind("Key", handle_keypress)

"""
An event handler can be bind to any widget in an application.
In the case for buttons the next events are valid:
<Button-1> -> Left mouse button
<Button-2> -> Middle mouse button
<Button-3> -> Right mouse button
For more information about event types, check
https://web.archive.org/web/20190512164300/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html
"""
def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

"""
.mainloop() takes care of two parts of the loop for you
- It maintains a list of events that have occurred
- It runs an event handler any time a new event is added to that list
"""
# Run the event loop
window.mainloop()