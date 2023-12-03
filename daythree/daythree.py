import re


def load_data(name='data'):
    file = open(name, 'r')
    data = [line.strip() for line in file.readlines()]
    file.close()
    return data


def part_one():

    data = load_data()

    width, height = len(data[0]), len(data)

    valid_numbers = []

    for idx, line in enumerate(data):
        numbers = [number for number in re.finditer("(\d+)", line)]
        for number_map in numbers:
            number_start = number_map.start()
            number_end = number_map.end()

            number_added = False

            # check diagonally to the left
            if number_start > 0:
                if data[idx][number_start-1] != '.':
                    valid_numbers.append(int(number_map.group()))
                    number_added = True
                if idx < height-1:
                    if data[idx + 1][number_start-1] != '.':
                        valid_numbers.append(int(number_map.group()))
                        continue
                    else:
                        for tmp_idx in range(number_start, number_end):
                            if number_added:
                                break
                            if data[idx+1][tmp_idx] != '.':
                                valid_numbers.append(int(number_map.group()))
                                number_added = True
                if idx > 0:
                    if data[idx - 1][number_start-1] != '.':
                        valid_numbers.append(int(number_map.group()))
                        number_added = True
                    else:
                        for tmp_idx in range(number_start, number_end):
                            if number_added:
                                break
                            if data[idx - 1][tmp_idx] != '.':
                                valid_numbers.append(int(number_map.group()))
                                number_added = True

            # check diagonally to the right
            if number_end < width - 1:
                if data[idx][number_end] != '.':
                    valid_numbers.append(int(number_map.group()))
                    number_added = True
                if idx < height-1:
                    if data[idx + 1][number_end] != '.':
                        valid_numbers.append(int(number_map.group()))
                        number_added = True
                    else:
                        for tmp_idx in range(number_start, number_end):
                            if number_added:
                                break
                            if data[idx+1][tmp_idx] != '.':
                                valid_numbers.append(int(number_map.group()))
                                number_added = True
                if idx > 0:
                    if data[idx - 1][number_end] != '.':
                        valid_numbers.append(int(number_map.group()))
                        number_added = True
                    else:
                        for tmp_idx in range(number_start, number_end):
                            if number_added:
                                break
                            if data[idx-1][tmp_idx] != '.':
                                valid_numbers.append(int(number_map.group()))
                                number_added = True

    return sum(valid_numbers)


def part_two():

    directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
    ]

    data = load_data('data')

    sum = 0

    gear_locations = set()
    number_locations = set()

    def get_gear_neighbors(gear, neighbors):

        output = []

        valid_gear_cords = [
            (gear[0] + direction[0], gear[1] + direction[1]) for direction in directions
        ]

        for neighbor in neighbors:
            valid_neighbor_cords = [(x, neighbor[2])
                                    for x in range(neighbor[0], neighbor[1])]
            for valid_neighbor_cord in valid_neighbor_cords:
                if valid_neighbor_cord in valid_gear_cords:
                    output.append(int(neighbor[3]))
                    break

        return output

    for idx, line in enumerate(data):
        for gear in re.finditer("\*", line):
            gear_locations.add((gear.start(), idx))
        for digit in re.finditer("\d+", line):
            number_locations.add(
                (digit.start(), digit.end(), idx, digit.group(0)))

    for gear in gear_locations:
        neighbors = get_gear_neighbors(gear, number_locations)
        if len(neighbors) == 2:
            sum += neighbors[0] * neighbors[1]

    return sum


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
