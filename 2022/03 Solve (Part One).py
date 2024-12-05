import math

def get_lines():
    f = open("03 input.txt", "r")

    content = f.read()
    lists = content.split("\n")

    return lists 

def get_priority(letter):
    ascii_code = ord(letter)

    if ascii_code >= 97 and ascii_code <= 122: # a-z
        return ascii_code - 96;
    
    if ascii_code >= 65 and ascii_code <= 90: # A-Z
        return ascii_code - 65 + 27;
    
    raise Exception("Letra no válida")

def find_duplicated(line):
    size = len(line)
    half = math.floor(size / 2)
    first_compartment = line[0:half]
    second_compartment = line[half:size]
    
    for letter in first_compartment:
        if letter in second_compartment:
            return letter
    
    return None

def main():
    lines = get_lines()
    sum = 0
    for line in lines:
        duplicated = find_duplicated(line)
        sum += get_priority(duplicated)
    
    print(sum)

main()
