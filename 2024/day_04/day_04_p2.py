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

    diagonal_left_up = -1-1j
    diagonal_left_down = -1+1j
    diagonal_right_up = 1-1j
    diagonal_right_down = 1+1j

    down_up_diagonal =[diagonal_left_down, diagonal_right_up]
    up_down_diagonal = [diagonal_left_up, diagonal_right_down]

    final_sum = 0

    for elem in grid:
        if grid[elem] == 'A':
            if grid.get(elem + diagonal_left_up) and \
            grid.get(elem + diagonal_left_down) and \
            grid.get(elem + diagonal_right_up) and \
            grid.get(elem + diagonal_right_down):
                word1 = ["A"]
                word2 = ["A"]
                for pos in down_up_diagonal:
                    word1.append(grid.get(elem + pos))
                for pos in up_down_diagonal:
                    word2.append(grid.get(elem + pos))
                word1.sort()
                word2.sort()
                if word1 == ["A", "M", "S"] and word2 == ["A", "M", "S"]:
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

