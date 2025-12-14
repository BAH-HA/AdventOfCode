from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string



def locations_ids():
    string = get_input()
    parsed_string = string.split("\n")
    list_1 = []
    list_2 = []
    final_sum = 0
    for pair in parsed_string:
        n1, n2 = pair.split()
        list_1.append(int(n1))
        list_2.append(int(n2))


    for i in range(len(list_1)):
        mult = list_2.count(list_1[i])
        final_sum += list_1[i] * mult
    
    return final_sum

if __name__ == "__main__":
    print(locations_ids())
    print(f"Execution time: {time() - ts} seconds")
