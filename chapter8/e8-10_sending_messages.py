def show_messages(messages):
    for msg in messages:
        print(msg)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

text_messages = ["Who the hell do you think I am!!","Make possible the impossible", "Belive in the you, who belives in you"]
sent_messages = []

send_messages(text_messages, sent_messages)

print("\ntext_messages")
print(text_messages)
print("sent_messages")
print(sent_messages)