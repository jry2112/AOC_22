class Node():
    def __init__(self):
        self.parent = None
        self.children = []
        self.name = None
        self.size = 0
        self.type = None

    def print_node(self, action):
        print(f"{self.type} {self.name} - {self.size}")


def find_directories(fp):
    cmd = fp.readline().strip('\n').split()
    head = None
    cur_node = None

    while cmd:
        print(cmd)
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                dir_name = cmd[2]
                if dir_name == '/':
                    head = Node()
                    head.name = dir_name
                    head.type = 'dir'
                    cur_node = head

                elif dir_name == '..':
                    cur_node = cur_node.parent

                else:
                    # find the new dir
                    for child_dir in cur_node.children:
                        if child_dir.type == 'dir':
                            if child_dir.name == dir_name:
                                cur_node = child_dir

                cmd = fp.readline().strip('\n').split()

            elif cmd[1] == 'ls':
                # make the children
                cmd = fp.readline().strip('\n').split()
                while cmd and cmd[0] != '$':
                    name = cmd[1]
                    if cmd[0] == 'dir':
                        child_dir = Node()
                        child_dir.name = name
                        child_dir.type = 'dir'
                        child_dir.parent = cur_node
                        cur_node.children.append(child_dir)
                    else:
                        # normal file
                        size = int(cmd[0])
                        child_file = Node()
                        child_file.name = name
                        child_file.type = 'file'
                        child_file.parent = cur_node
                        child_file.size = size
                        cur_node.children.append(child_file)
                        prev_node = cur_node
                        if prev_node:
                            while prev_node != head:
                                prev_node.size += size
                                prev_node = prev_node.parent
                        head.size += size
                    cmd = fp.readline().strip('\n').split()
    file_sizes = []
    get_size(head, file_sizes)

    total_size = 0
    small_sum_size = 0
    for file in file_sizes:
        if file[1] <= 100000:
            small_sum_size += file[1]
        if file[0] == '/':
            total_size = file[1]
    print(small_sum_size)
    print(total_size)

    total_space = 70000000
    desired_space = 30000000
    unused_space = total_space - total_size
    print(unused_space)
    target = ('', None)
    for directory in file_sizes:
        if target[1] is None:
            target = directory
        elif directory[1] + unused_space >= desired_space:
            if target[1] > directory[1]:
                target = directory

    print(target)


def get_size(par_node, file_sizes):
    if par_node.type == 'dir':
        file_sizes.append((par_node.name, par_node.size))
        for child_node in par_node.children:
            get_size(child_node, file_sizes)



if __name__ == "__main__":
    with open("input/day7_input", "r") as file:
        find_directories(file)
