def count_calories(fp):
    cal_count = [0]
    cur_elf = 0
    for line in fp:
        if line == '\n':
            cur_elf += 1
            cal_count.append(0)
        else:
            cur_cal = line.strip('\n')
            cal_count[cur_elf] += int(cur_cal)
    sort_list(cal_count)
    print(sum(cal_count[-3:]))


def sort_list(list):
    for i in range(0, len(list)-1):
        cur_pos = i
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]



if __name__ == "__main__":
    # Get input file
    with open("input/day1_test.txt", "r") as file:
        count_calories(file)
    with open("input/day1_input", "r") as file:
        count_calories(file)



