from time import time
ts = time()

# Toggle this to True to use example input
TEST_MODE = False
EXAMPLE_INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def get_input():
    if TEST_MODE:
        string = EXAMPLE_INPUT.strip()
    else:
        with open("input", "r") as f:
            string = f.read().strip()
    return string

def manual_updates():
    string = get_input()
    page_order_list, updates = string.split('\n\n')

    page_order_list = page_order_list.split('\n')
    updates = updates.split('\n')

    #The keys can only be printed if the values are already printed
    page_order_map = make_page_order_map(page_order_list)

    incorrect_updates = []
    final_sum = 0

    for update in updates:
        is_correct = is_correct_update(page_order_map, update)

        if not is_correct:
            incorrect_updates.append(update)

    for incorrect_update in incorrect_updates:
        corrected_update = correct_update(page_order_map, incorrect_update)
        corrected_update = corrected_update.split(',')
        final_sum += int(corrected_update[len(corrected_update) // 2])

    return final_sum

def is_correct_update(page_order_map, update):
    printed_pages = set()
    pages_to_be_printed = set(update.split(','))
    pages = update.split(',')
    safe = True

    for page in pages:
        if page_order_map.get(int(page)):
            for page_num in page_order_map.get(int(page)):
                if str(page_num) in pages_to_be_printed:
                    if page_num not in printed_pages:
                        safe = False
                        break
                printed_pages.add(int(page))
        else:
            printed_pages.add(int(page))

    return safe

def correct_update(page_order_map, update):
    # Start with the list of integers
    pages = [int(p) for p in update.split(',')]
    
    while True:
        # Convert to string for the check and history tracking
        current_state = ",".join(map(str, pages))
        if is_correct_update(page_order_map, current_state):
            return current_state
        
        made_swap = False
        
        for i, page_to_print in enumerate(pages):
            if page_to_print in page_order_map:
                prerequisites = page_order_map[page_to_print]
                
                for prereq_page in prerequisites:
                    if prereq_page in pages:
                        prereq_index = pages.index(prereq_page)
                        
                        # Violation: Prerequisite is located AFTER the dependent page
                        if prereq_index > i:
                            
                            # Swap: Move the prerequisite (prereq_page) to the position 
                            # of the dependent page (page_to_print)
                            pages[i], pages[prereq_index] = pages[prereq_index], pages[i]
                            
                            made_swap = True
                            break 
                
            if made_swap:
                break

def make_page_order_map(page_order_list):
    page_order_map = {}
    for page_order in page_order_list:
        x, y = page_order.split('|')
        x = int(x)
        y = int(y)
        page_order_map[y] = page_order_map.get(y, []) + [x]

    return page_order_map


if __name__ == "__main__":
    print(manual_updates())
    print(f"Execution time: {time() - ts} seconds")

