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

    correct_updates = []
    final_sum = 0

    for update in updates:
        is_correct = is_correct_update(page_order_map, update)

        if is_correct:
            correct_updates.append(update)

    for correct_update in correct_updates:
        correct_update = correct_update.split(',')
        final_sum += int(correct_update[len(correct_update) // 2])

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

