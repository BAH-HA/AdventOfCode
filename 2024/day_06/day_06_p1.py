from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

def patrol():
    string = get_input()
    grid, initial_coord = make_coord_grid(string)
    seen = set()
    seen.add(initial_coord)
    direction = -1j
    current_coord = initial_coord
    while True:
        if grid.get(current_coord + direction):
            if grid.get(current_coord + direction) == '#':
                direction *= 1j
            else:
                seen.add(current_coord + direction)
                current_coord += direction
        else:
            break

    return len(seen)

def make_coord_grid(string):
    lines = string.split('\n')
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x + y * 1j)] = lines[y][x]
            if lines[y][x] == '^':
                coord = x + y * 1j


    return grid, coord

if __name__ == "__main__":
    print(patrol())
    print(f"Execution time: {time() - ts} seconds")

