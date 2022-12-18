def match_groups(file):
    sacks = file.readlines()
    groups = {}
    group_num = 0
    sack_num = 0
    # Split into groups of 3
    while sack_num < len(sacks):
        groups[group_num] = sacks[sack_num:sack_num+3]
        group_num += 1
        sack_num += 3

    # Calculate frequency for each group
    total_priority = 0
    for group, sacks in groups.items():
        hash_map = [0] * 52
        for sack in sacks:
            found_items = set()
            sack = sack.strip('\n')
            for item in sack:
                index = get_index(item)
                if item not in found_items:
                    hash_map[index] += 1
                    found_items.add(item)
                    if hash_map[index] == 3:
                        total_priority += index + 1
    print(total_priority)

def reorganize_rucksacks(sacks):
    total_priority = 0
    for line in sacks:
        sack = line.strip('\n')
        total_priority += reorganize_rucksack(sack)
    print(total_priority)


def reorganize_rucksack(sack):
    hash_map = [0] * 52
    priority_sum = 0
    i = 0

    # Get items in first compartment
    while i < len(sack)/2:
        item = sack[i]
        i += 1
        hash_map[get_index(item)] += 1
    # Compare to items in second compartment
    while i < len(sack):
        item = sack[i]
        index = get_index(item)
        if hash_map[index] > 0:
            # Calculate priority
            priority_sum += index + 1
            hash_map[index] = -1
        i += 1

    return priority_sum


def get_index(item):
    if 'a' <= item <= 'z':
        return ord(item)-97
    elif 'A' <= item <= 'Z':
        return ord(item) - 39


if __name__ == "__main__":
    with open("input/day3_test", "r") as file:
        #reorganize_rucksacks(file)
        match_groups(file)
    with open("input/day3_input", "r") as file:
        #reorganize_rucksacks(file)
        match_groups(file)
        pass