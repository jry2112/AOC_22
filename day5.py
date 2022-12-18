import string
import re


def get_crates(fp):
    result = {}
    line = fp.readline()
    while line != '\n':
        regex = '[A-Z]| {4}'
        values = re.findall(regex, line)
        for col in range(len(values)):
            if values[col] != '    ':
                if col in result:
                    result[col].append(values[col])
                else:
                    result[col] = [values[col]]
        line = fp.readline()
    return result


def get_moves(fp):
    moves = []
    for line in file:
        line = line.split()
        result = []
        for i in range(len(line)):
            if i % 2 != 0:
                result.append(line[i])
        moves.append(result)

    return moves


def move_crates(crates_list, moves_list):
    for move in moves_list:
        count = int(move[0])
        target = int(move[1]) - 1
        dest = int(move[2]) - 1
        crates = []
        for i in range(count):
            crates_list[dest].insert(0, crates_list[target].pop(0))


def move_crates9001(crates_list, moves_list):
    for move in moves_list:
        count = int(move[0])
        target = int(move[1]) - 1
        dest = int(move[2]) - 1
        crates = []
        for i in range(count):
            crates.append(crates_list[target].pop(0))
        for j in range(count):
            crates_list[dest].insert(0, crates.pop(-1))


def get_tops(crates):
    tops = ''
    col = 0

    while col in crates:
        tops += crates[col][0]
        col += 1
    return tops


if __name__ =="__main__":
    with open("input/day5_input", "r") as file:
        crates = get_crates(file)
        print(crates)
        moves = get_moves(file)
        move_crates9001(crates, moves)
        print(get_tops(crates))

