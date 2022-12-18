def find_pairs(fp):
    full_pairs = 0

    for line in fp:
        # pair = ['start1-stop1', 'start2-stop2']
        pair = line.strip('\n').split(',')
        start1 = int(pair[0].split('-')[0])
        stop1 = int(pair[0].split('-')[1])
        start2 = int(pair[1].split('-')[0])
        stop2 = int(pair[1].split('-')[1])

        if start1 <= start2 and stop1 >= stop2:
            full_pairs += 1
        elif start2 <= start1 and stop2 >= stop1:
            full_pairs += 1

    print(full_pairs)

def find_all_overlaps(fp):
    pair_count = 0

    for line in fp:
        # pair = ['start1-stop1', 'start2-stop2']
        pair = line.strip('\n').split(',')
        start1 = int(pair[0].split('-')[0])
        stop1 = int(pair[0].split('-')[1])
        start2 = int(pair[1].split('-')[0])
        stop2 = int(pair[1].split('-')[1])

        overlap_found = False

        for i in range(start1, stop1+1):
            if i == start2 or i == stop2:
                pair_count += 1
                overlap_found = True
                break
        if not overlap_found:
            for i in range(start2, stop2+1):
                if i == start1 or i == stop1:
                    pair_count += 1
                    break

    print(pair_count)


if __name__ =="__main__":
    with open("input/day4_test", "r") as file:
        # find_pairs(file)
        find_all_overlaps(file)
    with open("input/day4_input", "r") as file:
        # find_pairs(file)
        find_all_overlaps(file)