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
    
    direction = -1j
    final_sum = 0
    for coord in grid:
        current_coord = initial_coord
        seen = {}
        seen[initial_coord] = [direction]
        if grid[coord] != '.':
            continue
        grid[coord] = "#"
        while True:
            if grid.get(current_coord + direction):
                if grid.get(current_coord + direction) == '#':
                    direction *= 1j
                else:
                    if seen.get(current_coord + direction):
                        if direction in seen[current_coord + direction]:
                            final_sum += 1
                            break
                    seen[current_coord + direction] = \
                        seen.get(current_coord + direction, []) + [direction]
                    current_coord += direction
            else:
                break
        grid[coord] = '.'
        direction = -1j

    return final_sum

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

