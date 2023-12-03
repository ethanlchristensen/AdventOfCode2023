def part_one():
    return sum(list(map(lambda yup: 0 if not yup[1] else yup[0], [[(val := line.strip().split(': '))[1], int(val[0].split(' ')[1]), all([[(erm := single.split(' ')), int(erm[0]) <= {'red': 12, 'green': 13, 'blue': 14}[erm[1]]][1] for single in [j for sub in [block.split(', ') for block in val[1].split('; ')] for j in sub]])][1:] for line in open('data', 'r')])))


def part_two():
    return sum([(yeet := [(val := line.strip().split(': '))[1], [single.split(' ') for single in [j for sub in [block.split(', ') for block in val[1].split('; ')] for j in sub]]][1], [max([int(holy[0]) if holy[1] == 'red' else 0 for holy in yeet]) * max([int(holy[0]) if holy[1] == 'green' else 0 for holy in yeet]) * max([int(holy[0]) if holy[1] == 'blue' else 0 for holy in yeet])][0])[1] for line in open('data', 'r')])


def solve():
    part_one_answer = part_one()
    part_two_answer = part_two()

    print(f"part one: {part_one_answer}")
    print(f"part two: {part_two_answer}")


if __name__ == "__main__":
    """
    code to run solve
    """
    solve()
