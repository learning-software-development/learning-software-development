# Functions, parameters, return values

starting_position = 5


# def move_player(by_amount):
#     global position
#     position += by_amount


def move_player(current_position, by_amount):
    position = current_position + by_amount
    return position


print(starting_position)
new_position = move_player(starting_position, 2)
print(new_position)
new_position = move_player(new_position, -2)
print(new_position)
print("difference between start and end is ", starting_position - new_position)
