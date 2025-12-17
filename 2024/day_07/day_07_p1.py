from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

def calibration_equations():
    lines = get_input().split("\n")
    final_sum = 0
    for line in lines:
        target, numbers = line.split(": ")
        numbers = numbers.split(" ")
        numbers = [int(x) for x in numbers]
        target = int(target)

        num_of_operators = len(numbers) - 1

        #total_combinations = 2^num_operators
        total_combinations = 1 << num_of_operators

        for i in range(total_combinations):
            operators = []
            for j in range(num_of_operators):
                if (i >> j) & 1:
                    operators.append("*")
                else:
                    operators.append("+")

            result = calculate(numbers, operators)
            if result == target:
                final_sum += target
                break
            
    return final_sum

def calculate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        operator = operators[i]
        next_number = numbers[i + 1]
        if operator == "+":
            result += next_number
        elif operator == "*":
            result *= next_number

    return result



if __name__ == "__main__":
    print(calibration_equations())
    print(f"Execution time: {time() - ts} seconds")

