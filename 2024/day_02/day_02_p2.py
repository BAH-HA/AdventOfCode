from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

def reports():
    string = get_input()
    parsed_string = string.split("\n")
    final_count = 0

    for report in parsed_string:
        levels = [int(x) for x in report.split()]
        safe = is_safe(levels)
        if not safe:
            for i in range(len(levels)):
                new_report = levels[:i] + levels[i + 1:]
                if is_safe(new_report):
                    safe = True
                    break;
        if safe:
            final_count += 1
        
    return final_count

def is_safe(levels):
    #if increasing order, order = 1, else order = -1
    order = 1 if levels[0] < levels[1] else -1
    safe = True
    for i in range(len(levels) - 1):
        current_level = levels[i]
        next_level = levels[i + 1]
        if abs(current_level - next_level) > 3:
            safe = False
            break;
        match order:
            case 1:
                if current_level >= next_level:
                    safe = False
                    break;
            case -1:
                if current_level <= next_level:
                    safe = False
                    break;
    return safe

if __name__ == "__main__":
    print(reports())
    print(f"Execution time: {time() - ts} seconds")
