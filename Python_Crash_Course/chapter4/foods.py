my_foods = ['pizza','falafel','carrot_cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice_cream')

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)


print("My favorite foods are:")
for food in my_foods:
	print(food.title())

print("My friend's favorite foods are:")
for food in friend_foods:
	print(food.title())