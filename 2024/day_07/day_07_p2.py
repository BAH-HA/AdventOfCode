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

        #total_combinations = 3^num_operators
        total_combinations = 3 ** num_of_operators

        for i in range(total_combinations):
            operators = generate_operators(num_of_operators, i)

            result = calculate(numbers, operators, target)
            if result == target:
                final_sum += target
                break
            
    return final_sum

def calculate(numbers, operators, target):
    result = numbers[0]
    for i in range(len(operators)):
        operator = operators[i]
        next_number = numbers[i + 1]
        if result > target: #Tried to optimize a bit ahahahah
            break
        if operator == "+":
            result += next_number
        elif operator == "*":
            result *= next_number
        elif operator == "||": 
            result = int(str(result) + str(next_number))

    return result

def generate_operators(num_operators, combination_index):
    operators = []
    temp_index = combination_index
    
    for _ in range(num_operators):
        # Get the "digit" (choice) using the modulo operator (base 3)
        choice = temp_index % 3
        
        # Map the choice to the operator symbol
        if choice == 0:
            operators.append('+')
        elif choice == 1:
            operators.append('*')
        elif choice == 2:
            operators.append('||') # The new third operator
            
        # Reduce the index for the next digit (right shift in base 3)
        temp_index //= 3
        
    return operators


if __name__ == "__main__":
    print(calibration_equations())
    print(f"Execution time: {time() - ts} seconds")

