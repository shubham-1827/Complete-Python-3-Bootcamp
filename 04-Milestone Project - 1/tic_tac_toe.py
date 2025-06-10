from typing import List


# function to generate the grid
def generate_grid():
    return [[" "] * 3 for _ in range(3)]


# lets create a function to display the tic tac toe grid
def display_grid(lst: List[List[str]]):
    for i in range(3):
        print(f"{lst[i][0]} | {lst[i][1]} | {lst[i][2]}")
        if i < 2:
            print("----------")


# now lets create a function to take the user input and validate it if its in range
def range_choice(o_or_x):
    tries = 5
    while True:
        try:
            ch = input(
                f"For {o_or_x}, select row and column (0-2) separated by space: "
            ).split()
            ch = list(map(int, ch))
            if len(ch) == 2 and all(0 <= x <= 2 for x in ch):
                return ch
            else:
                print("Invalid range. Please enter two numbers between 0 and 2.")
        except ValueError:
            if tries == 5:
                print("You have tried 5 times, please try again")
            print("Invalid input. Please enter numbers only.")


# winning logic
def check_winner(grid: List[List[str]]) -> str | None:
    lines = grid + list(zip(*grid))
    lines.append([grid[i][i] for i in range(3)])
    lines.append([grid[i][2 - i] for i in range(3)])

    for line in lines:
        if line == ["O"] * 3 or line == ["X"] * 3:
            return line[0]
    return None


# now the function for final game logic
def tic_tac_toe():
    grid = generate_grid()
    ox_arr = ["O", "X"]
    won = False
    moves_available = True
    count = 0
    while not won and moves_available:
        display_grid(grid)
        choice = range_choice(ox_arr[count % 2])
        print("\033c", end="")
        if grid[choice[0]][choice[1]] != " ":
            print("Cell already occupied!!!!")
            continue
        grid[choice[0]][choice[1]] = ox_arr[count % 2]
        count += 1
        if count == 9:
            print("Game Drawn")
            display_grid(grid)
            moves_available = False

        winner = check_winner(grid)
        if winner:
            print(f"Team {winner}, Won the Game in {count} moves!!!!!!")
            won = True
            break


def replay():
    choice = input("Want to play again : ")
    if choice.lower() == "y":
        return True
    return False


if __name__ == "__main__":
    while True:
        tic_tac_toe()
        if not replay():
            break
