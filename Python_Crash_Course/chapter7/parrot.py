# In a while loop, if there are several condition that when they come true
# can finish the loop, you can use a flag variable to only check one condition
# in the while loop
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)