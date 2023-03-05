sandwich_orders = ['pastrami','egg','jam','pastrami','cheese','tuna']
finished_sandwiches = []

print("New orders")
print(sandwich_orders)
print("\nI'm sorry, we have run out of pastrami\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"We are preparing a {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print(finished_sandwiches)