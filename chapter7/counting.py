# While loops execute code while a condition remains true
# The next program counts thru 1 to 10 but only prints odd numbers
current_number = 0
while current_number < 10:
    current_number += 1

    if (current_number % 2) == 0:
        continue
    print(current_number)