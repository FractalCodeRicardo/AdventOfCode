
def get_elves_lists():
    f = open("01 input.txt", "r")

    content = f.read()
    lists = content.split("\n\n")

    return lists 


def sum_items(items):
    sum = 0
    for item in items:
        sum += int(item)
    
    return sum

def save_max(sum, max_items):
    max_items.sort()

    i = 0
    while i < 3:
        if max_items[i] == 0 | max_items[i] < sum:
            max_items[i] = sum;
            break;

        i += 1

def solve():
    elves_lists = get_elves_lists()
    
    max_items = [0, 0, 0]

    for elf_list in elves_lists:
        items = elf_list.split("\n")
        sum = sum_items(items)        
        save_max(sum, max_items)    
        
    print(max_items)

solve()
