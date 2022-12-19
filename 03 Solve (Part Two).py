def get_lines():
    f = open("03 input (Part Two).txt", "r")

    content = f.read()
    lists = content.split("\n")

    return lists 

def find_duplicated(l1, l2, l3):    
    for letter in l1:
        if letter in l2 and letter in l3:
            return letter

    return None

def get_priority(letter):
    ascii_code = ord(letter)

    if ascii_code >= 97 and ascii_code <= 122: # a-z
        return ascii_code - 96;
    
    if ascii_code >= 65 and ascii_code <= 90: # A-Z
        return ascii_code - 65 + 27;
    
    raise Exception("Letra no válida")

def main():

    i = 0
    lines = get_lines()
    sum = 0
    while (i < len(lines)):
        items_elf1 = lines[i]
        items_elf2 = lines[i + 1]
        items_elf3 = lines[i + 2]

        duplicated = find_duplicated(items_elf1, items_elf2, items_elf3)
        sum += get_priority(duplicated)
        i += 3

    print(sum)
main()