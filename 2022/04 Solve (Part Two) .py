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

def range_overlap(r1, r2):
    min2 = r2["min"]
    max2 = r2["max"]

    min1 = r1["min"]
    max1 = r1["max"]

    for i in range(min2, max2 +1):
        if i >= min1 and i <= max1 : return True 
    
    return False

def pair_overlaps(line):
    line_split = line.split(",")
    p1 = line_split[0]
    p2 = line_split[1]

    r1 = get_range(p1)
    r2 = get_range(p2)

    if range_overlap(r1, r2): return True
    if range_overlap(r2, r1): return True

    return False
    

def main():
    lines = get_lines()
    count = 0
    for line in lines:
        if pair_overlaps(line):
            print(line)
            count += 1
    
    print(count)

main()