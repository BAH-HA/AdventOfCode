from time import time
import re
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

def multiplication():
    string = get_input()
    pattern = r"mul\(\d{1,3},\d{1,3}\)|(?:do|don't)\(\)"
    matches = re.findall(pattern, string)
    final_sum = 0
    do = True

    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif do:
            x, y = match[4:-1].split(",")
            final_sum += int(x) * int(y)
    
    return final_sum


if __name__ == "__main__":
    print(multiplication())
    print(f"Execution time: {time() - ts} seconds")

