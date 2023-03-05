import tkinter as tk

"""
Windows
A window is the basic for any GUI, the next command creates a window
"""
window = tk.Tk()

"""
A text widget is similar to an Entry with the difference that it may
contain multiple lines of text. Just like Entry widgets, Text widgets
support the following operations
- Retrieve text with .get()
- Delete text with .delete()
- Insert text with .insert()
Although the methods are the same, they work a little different that
in the Entry widget.
"""
text_box = tk.Text()
text_box.pack()

"""
You can get text from text_box like in Entry widget using the .get()
method, with the exception that using .get() without arguments will
raise an exception.
"""
#text_box.get()

"""
Method .get() requires at least one argument.
The arguments are indexes in the Text widget, this indices works
different than in Entry widgets. An index must contain two pieces
of information:
- The line number of a character. Line numbers start with 1 and character
position start with 0.
- The position of a character on that line
Index must be in the following string format "<line>.<char>"
Calling .get() with one argument returns a single character.
"""
# Assume the next input on the text box
# Hello
# World
text_box.get("1.0")
# Console output:'H'

"""
Using an start and end index will retrieve several characters. This works
just like Python string slices, in order to get the entire word from the
text box, the end index must be one more than the index of the last character
to be read.
"""
text_box.get("1.0", "1.5")
# Console output:'Hello'
text_box.get("2.0", "2.5")
# Console output:'World'

"""
To get all of text in a text box, set the starting index in "1.0" and use the
special tk.END constant for second index
"""
text_box.get("1.0", tk.END)
# Console output:'Hello/nWorld/n'

"""
Method .delete() is used to delete characters from a text box. It works just as
in Entry widgets. It can:
- Delete a single argument
- Delete two arguments
Using a single-argument version, only one character will be deleted
"""
text_box.delete("1.0")
# Text in the text box
# ello
# World

"""
With the two argument version, a range of characters will be deleted starting
at the first index and up to, but not including, the second index.
"""
text_box.delete("1.0", "1.4")
# Text in the text box
#
# World
"""
Note that there is still one character in the first line, a new line character.
If removed then first line will be deleted
"""
text_box.delete("1.0")
# Text in the text box
# World

"""
To clear out the text box, the tk.END constant can be used
"""
text_box.delete("1.0", tk.END)

"""
Method .insert() add text to the text box. This method requires an index and the
text to be inserted.
"""
text_box.insert("1.0", "Hello")
# Text in the text box
# Hello
"""
In order to add text in the second line use new line character.
.insert() will do one of two things:
- Insert text at the specified position if there's already text at or after that
position
- Append text to the specified line if the character number is greater than the
index of the last character in the text box.
"""
text_box.insert("2.0", "World")
# Text in the text box
# HelloWorld
text_box.insert("2.0", "\nWorld")
# Text in the text box
# HelloWorld
# World

"""
The best way to insert text at the end of a Text widget is to use tk.END to the
first paramter of .insert()
"""
text_box.insert(tk.END, "Put me at the end!")
# Text in the text box
# HelloWorld
# WorldPut me at the end!

window.mainloop()

"""
As a side note, to destroy a window using the interactive console,
use the following command
"""
#window.destroy()