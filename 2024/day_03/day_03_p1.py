from time import time
import re
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
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
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, string)
    final_sum = 0

    for match in matches:
        x, y = match[4:-1].split(",")
        final_sum += int(x) * int(y)
    
    return final_sum


if __name__ == "__main__":
    print(multiplication())
    print(f"Execution time: {time() - ts} seconds")

