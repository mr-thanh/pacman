import random
import time
import subprocess
from handle_arr import version_1
# def replace_all_value_square_array(array,old_value,new_value):
#     dimension = len(array)
#     for i in range(dimension):
#         for j in range(dimension):
#             if array[i][j] == old_value:
#                 array[i][j] = new_value
#
# def position_value_array(array,value):
#     dimension = len(array)
#     check = False
#     for i in range(dimension):
#         if check:
#             i = i - 1
#             break
#         for j in range(dimension):
#             if array[i][j] == value:
#                 check = True
#                 break
#     if check:
#         return i,j
#     else:
#         raise ValueError("No value matches")

# function return random index that is random step of pacman
# up/down/right/left of 1 unit
def random_step(x,y):
    step = random.choice(["up","down","right","left"])
    if step == "up":
        x = x - 1
    elif step == "down":
        x = x + 1
    elif step == "right":
        y = y + 1
    else:
        y = y - 1
    return (x,y)

# function return random index in slice of array[1:5,[1:5]
# this is position of pacman when it do a step meeting wall
def random_reset():
    x_y = random.choices((1,2,3,4),k=2)
    return tuple(x_y)

# function display all out of screen
def display_pacman(array):
    subprocess.run("cls", shell=True)
    print()
    print("    [@]: Pacman"
          "\n    [c]: Cherry + 5 point + 1 life"
          "\n    [b]: Banana + 2 point"
          "\n    [*]: Ghost - 1 life"
          "\n    [M]: Medal")
    print("    -------------------------------")
    print(f"    Point: {point} - Life: {life} - Step {steps} ")
    print()
    for item in array:
        print("    {}  {}  {}  {}  {}  {}".format(item[0],item[1],item[2],item[3],item[4],item[5]))
    print()


def start_pacman():
    global life , point , steps
    grid = [['=', '=', '=', '=', '=', '='],
            ['=', '@', 'c', 'b', 'c', '='],
            ['=', 'b', '*', 'b', 'c', '='],
            ['=', 'c', 'b', 'c', '*', '='],
            ['=', 'c', 'b', '*', 'M', '='],
            ['=', '=', '=', '=', '=', '=']]
    life, point, steps = 0, 0, 0
    while True:
        display_pacman(grid)
        time.sleep(2)

        # get position of pacman
        current_position = version_1.position_value_array(grid,"@")
        x = current_position[0]
        y = current_position[1]

        #get new position at which pacman move to
        new_position = random_step(x,y)
        new_x = new_position[0]
        new_y = new_position[1]

        version_1.replace_all_value_square_array(grid,"@","-")
        while True:
            #if pacman meet Cherry, increasing life, point and step
            if grid[new_x][new_y] == "c":
                life += 1
                point += 5
                steps += 1
                grid[new_x][new_y] = "@"
                display_pacman(grid)
                print("    Pacman get 1 Cherry.")
                time.sleep(1)
                break
            # if pacman meet Banana, increasing point and step
            if grid[new_x][new_y] == "b":
                point += 2
                steps += 1
                grid[new_x][new_y] ="@"
                display_pacman(grid)
                print("    Pacman get 1 Banana.")
                time.sleep(1)
                break
            # if pacman meet Ghost, decreasing life, increasing step
            if grid[new_x][new_y] == "*":
                life -= 1
                steps += 1
                grid[new_x][new_y] = "@"
                display_pacman(grid)
                print("    Pacman meet 1 Ghost.")
                time.sleep(1)
                if life < 0:
                    print("    Not enough life. Pacman died. Game Over!")
                    time.sleep(1)
                    if input("    Do you restart Pacman? [Y]es or [N]o: ").lower() == "y" :
                        start_pacman()
                    else:
                        exit()
                break
            # if pacman meet Medal, Pacman Win
            if grid[new_x][new_y] == "M":
                print(("    Pacman win"))
                time.sleep(1)
                if input("    Do you want to restart Pacman? [y]es or [n]o: ").lower() == "y":
                    start_pacman()
                else:
                    exit()
            # if pacman meet empty position, increasing step
            if grid[new_x][new_y] == "-":
                steps += 1
                grid[new_x][new_y] ="@"
                break
            # if pacman meet wall, get a random new postion inside map that pacman land at
            if grid[new_x][new_y] == "=":
                random_new_position = random_reset()
                new_x = random_new_position[0]
                new_y = random_new_position[1]
                steps += 1
                display_pacman(grid)
                print(f"    Pacman hit the wall."
                    f"\n    Pacman will land on a new random position.")
                time.sleep(2)

start_pacman()

# if __name__ == "__main__":
#     start_pacman()

