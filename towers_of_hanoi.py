# Simulate towers of hanoi problem


import sys


class Tower:
    # Each tower can be represented as a stack.
    # Count the number of push and pops during actual run.
    def __init__(self):
        self.lst = []
        self.ops = 0

    def push(self, i):
        self.ops += 1
        self.lst.append(i)

    def pop(self):
        self.ops += 1
        return self.lst.pop()

    def clear_moves(self):
        self.ops = 0

    def __repr__(self):
        return repr(self.lst)


def tower_of_hanoi(num_discs, from_tower, to_tower, temp_tower):
    if num_discs == 1:
        to_tower.push(from_tower.pop())
    else:
        tower_of_hanoi(num_discs - 1, from_tower, temp_tower, to_tower)
        tower_of_hanoi(1, from_tower, to_tower, temp_tower)
        tower_of_hanoi(num_discs - 1, temp_tower, to_tower, from_tower)


def main(num_discs):

    towers = []
    for i in range(3):
        towers.append(Tower())

    for i in range(num_discs):
        towers[0].push(i)
    towers[0].clear_moves()

    for i in range(len(towers)):
        print("Initial state of tower[", i, "] =", towers[i])

    print("\n>>Running towers of hanoi with num_discs = ", num_discs, "\n")

    tower_of_hanoi(num_discs, towers[0], towers[2], towers[1])

    for i in range(len(towers)):
        print("Final state of tower[", i, "] =", towers[i])

    total_ops = sum([t.ops for t in towers])
    return total_ops // 2


if __name__ == "__main__":
    num_discs = 3
    if len(sys.argv) > 2:
        print("Invalid arguments. Need only the number of discs")
        exit(-1)
    elif len(sys.argv) == 2:
        num_discs = int(sys.argv[1])

    nmoves = main(num_discs)
    print("Total Moves = ", nmoves)
