maze = [
    ['S', 0, 1, 0, 'E'],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

# start and end
player_pos = (0, 0)
end_pos = (0, 4)

# move
def move_player(direction, position):
    x, y = position
    if direction == 'up':
        x -= 1
    elif direction == 'down':
        x += 1
    elif direction == 'left':
        y -= 1
    elif direction == 'right':
        y += 1
    return x, y

# check
def is_valid_move(maze, position):
    x, y = position
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        return maze[x][y] != 1
    return False

# Manhattan distance
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos1[0]) + abs(pos1[1] - pos2[1])

# circle游戏循环
print("This is a little invisible maze game!")
print(
    "You need to control yourself to walk in an invisible maze, guess the location of the walls, and reach the exit.")
print("I will inform you of your current location and the distance to the exit after each action you take.")
print()

# check if ready
ready = input("Are you ready? ")
if ready.lower() not in ['yes', 'y', 'sure', 'ok']:
    print("Ok......I'll ask you again 🥹")
else:
    while True:
        print(f"Your current location: {player_pos}")
        distance = calculate_distance(player_pos, end_pos)
        print(f"The distance between you and the exit: {distance}")

        move = input("Please enter the direction of movement (up/down/left/right): ")

        # check the direction检查输入方向的有效性
        if move not in ['up', 'down', 'left', 'right']:
            print("Invalid direction! Please enter 'up', 'down', 'left', or 'right'.")
            continue

        new_pos = move_player(move, player_pos)

        if is_valid_move(maze, new_pos):
            player_pos = new_pos
            print(f"You moved to: {player_pos}")
            if maze[player_pos[0]][player_pos[1]] == 'E':
                print("Congratulations😄, you found the exit!")
                break
        else:
            print("Unable to move to that location, please choose another direction.")