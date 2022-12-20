class Knot:
    def __init__(self):
        self.pos = [0, 0]
        self.prev = None
        self.next = None


def move_rope(moves):
    head = Knot()
    cur_knot = head
    for i in range(9):
        new_knot = Knot()
        cur_knot.next = new_knot
        new_knot.prev = cur_knot
        cur_knot = new_knot

    cur_knot = head

    visited = {}

    cur_head = [0, 0]
    cur_tail = [0, 0]
    for move in moves:
        # move_the_rope(move, cur_head, cur_tail, visited)
        move_the_long_rope(move, head, visited)
    print(len(visited.keys()))


def move_the_long_rope(cur_move, head, visited):
    print(cur_move)
    dir = cur_move[0]
    steps = int(cur_move[1])
    steps_dict = {"L": -1, "R": 1, "U": 1, "D": -1}
    cur_knot = head
    next_knot = cur_knot.next
    tail_spots = {tuple([0, 0])}

    while next_knot:
        move_the_rope(cur_move, cur_knot.pos, next_knot.pos, visited)
        cur_knot = next_knot
        next_knot = cur_knot.next
    if tuple(cur_knot.pos) not in tail_spots:
        tail_spots.add(tuple(cur_knot.pos))
    print(tail_spots, len(tail_spots))


def move_the_rope(cur_move, cur_head, cur_tail, visited):
    print(cur_move)
    dir = cur_move[0]
    steps = int(cur_move[1])
    steps_dict = {"L": -1, "R": 1, "U": 1, "D": -1}

    while steps != 0:
        # Move the head
        if dir == "L" or dir == "R":
            cur_head[0] += steps_dict[dir]
        elif dir == "U" or dir == "D":
            cur_head[1] += steps_dict[dir]

        x_dist = abs(cur_head[0] - cur_tail[0])
        y_dist = abs(cur_head[1] - cur_tail[1])

        # Overlap
        if (x_dist == 0 and y_dist == 0) or (x_dist == 1 and y_dist == 0) or \
                (x_dist == 0 and y_dist == 1):
            # Okay to continue
            pass
        elif (x_dist == 2 and y_dist == 0) or (x_dist == 0 and y_dist == 2):
            # move one step in the proper direction
            if dir == "L" or dir == "R":
                cur_tail[0] += steps_dict[dir]
            elif dir == "U" or dir == "D":
                cur_tail[1] += steps_dict[dir]
        elif (x_dist > 1 and y_dist == 1) or x_dist == 1 and y_dist > 1:
            # Move one step diagonally
            if dir == "L" or dir == "R":
                cur_tail[0] += steps_dict[dir]
                cur_tail[1] = cur_head[1]
            elif dir == "U" or dir == "D":
                cur_tail[1] += steps_dict[dir]
                cur_tail[0] = cur_head[0]
        print(cur_head, cur_tail)
        steps -= 1

        if tuple(cur_tail) not in visited:
            visited[tuple(cur_tail)] = True


def get_moves(file):
    moves = file.readlines()
    for i in range(len(moves)):
        moves[i] = tuple(moves[i].strip('\n').split())
    return moves


if __name__ == "__main__":
    with open("input/day9_input", "r") as file:
        moves = get_moves(file)

    move_rope(moves)
