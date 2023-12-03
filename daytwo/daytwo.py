def part_one():
    return sum(list(map(lambda yup: 0 if not yup[1] else yup[0], [[(val := line.strip().split(": "))[1], int(val[0].split(" ")[1]), all([[(erm:=single.split(" ")), int(erm[0]) <= {'red': 12,'green': 13,'blue': 14}[erm[1]]][1] for single in [j for sub in [block.split(", ") for block in val[1].split("; ")] for j in sub]])][1:] for line in open('data','r')])))


def part_two():
    file = open('data', 'r')
    data = [line.strip() for line in file]
    file.close()

    powers = []

    for line in data:
        game_data = line.split(": ")
        game_id = int(game_data[0].split(' ')[1])
        draws = game_data[1].split('; ')
        game_vals = {
            'red': [],
            'green': [],
            'blue': []
        }
        for draw in draws:
            cubes = draw.split(', ')
            for cube in cubes:
                cube_data = cube.split(' ')
                count, color = int(cube_data[0]), cube_data[1]
                game_vals[color].append(count)

        powers.append(
            max(game_vals['red']) * max(game_vals['green']) * max(game_vals['blue']))

    return sum(powers)


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
    
