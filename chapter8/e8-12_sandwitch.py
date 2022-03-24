def make_sandwitch(*items):
    """This function print the items of a sandwitch"""
    print("Your sandwitch has")
    for item in items:
        print(f"- {item}")

make_sandwitch("jam","cheese","tomate")
make_sandwitch("pepperoni","cream")