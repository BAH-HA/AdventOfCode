from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

def xmas():
    grid = make_coord_grid(get_input())

    down = [1j, 2j, 3j]
    up = [-1j, -2j, -3j]
    left = [-1, -2, -3]
    right = [1, 2, 3]
    diagonal_left_up = [-1-1j, -2-2j, -3-3j]
    diagonal_left_down = [-1+1j, -2+2j, -3+3j]
    diagonal_right_up = [1-1j, 2-2j, 3-3j]
    diagonal_right_down = [1+1j, 2+2j, 3+3j]

    positions = [down, up, left, right, diagonal_left_up, 
                 diagonal_left_down, diagonal_right_up, diagonal_right_down]
    final_sum = 0

    for elem in grid:
        if grid[elem] == 'X':
            for pos in positions:
                word = 'X'
                for coord in pos:
                    if elem + coord not in grid:
                        break
                    word += grid[elem + coord]
                if word == "XMAS":
                    final_sum += 1
    
    return final_sum

def make_coord_grid(string):
    lines = string.split('\n')
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x + y * 1j)] = lines[y][x]

    return grid

if __name__ == "__main__":
    print(xmas())
    print(f"Execution time: {time() - ts} seconds")

