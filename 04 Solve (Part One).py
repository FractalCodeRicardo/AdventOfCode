def get_lines():
    f = open("04 input (Part One).txt", "r")

    content = f.read()
    lists = content.split("\n")

    return lists 
def get_range(pair):
    range_split = pair.split("-")

    return {
        "min": int(range_split[0]),
        "max": int(range_split[1])
    }

def is_range_fully_contained_in(r1, r2):
    min2 = r2["min"]
    max2 = r2["max"]

    min1 = r1["min"]
    max1 = r1["max"]

    min_in_range = min2 <= min1 and min1 <= max2
    max_in_range = min2 <= max1 and max1 <= max2

    return min_in_range and max_in_range

def has_pair_fully_contained(line):
    line_split = line.split(",")
    p1 = line_split[0]
    p2 = line_split[1]

    r1 = get_range(p1)
    r2 = get_range(p2)

    if is_range_fully_contained_in(r1, r2): return True
    if is_range_fully_contained_in(r2, r1): return True

    return False
    

def main():
    lines = get_lines()
    count = 0
    for line in lines:
        if has_pair_fully_contained(line):
            print(line)
            count += 1
    
    print(count)

main()