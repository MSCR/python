# Start market list
market_list = ['eggs', 'beef_meat', 'chicken_meat', 'box_bread', 'milk', 'sugar', 'carrots', 'potatoes']
print(market_list)

#lenght of list
length = len(market_list)

# Print first element
print(market_list[0])

# Access last item
print(market_list[length-1])
print(market_list[-1])

# Append an item
market_list.append('oil')
length = len(market_list)
print(market_list)

# Insert an item in the middle
market_list.insert(3,'coffee')
print(market_list)

# Delet an item
del(market_list[4])
print(market_list)

# Pop an item
print(market_list.pop())
print(market_list)
print(market_list.pop(1))
print(market_list)

# Remove an specific item
market_list.remove('carrots')
print(market_list)

# Organize list temporally
print(sorted(market_list))
print(market_list)

# Organize list temporally inverse
print(sorted(market_list,reverse=True))
print(market_list)

# Organize list temporally
market_list.sort()
print(market_list)

# Organize list temporally inverse
market_list.sort(reverse=True)
print(market_list)

market_list.reverse()
print(market_list)
print(len(market_list))