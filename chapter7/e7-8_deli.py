sandwich_orders = ['egg','jam','cheese','tuna']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"We are preparing a {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print(finished_sandwiches)