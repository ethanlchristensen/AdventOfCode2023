
import re


def load_data(name='data'):
    file = open(name, 'r')
    data = [line.strip() for line in file.readlines()]
    file.close()
    return data


def part_one():
    """
    code to solve part one
    """

    data = load_data()
    data = [list(map(int, re.sub(r' +', ' ', line.split(': ')[1].strip()).split(' '))) for line in data]
    
    result = 1
    
    time_record = zip(data[0], data[1])
    
    for time, record in time_record:
        ways_to_win_race = 0
        for idx in range(1, time):
            if (idx * (time - idx)) > record:
                ways_to_win_race += 1
        result *= ways_to_win_race
 
    return result


def part_two():
    """
    code to solve part two
    """
    
    data = load_data()
    data = [int(line.strip().split(': ')[1].replace(' ', '')) for line in data]
            
    ways_to_win_race = 0
    for idx in range(1, data[0]//2):
        if (idx * (data[0] - idx)) > data[1]:
            ways_to_win_race += 2
             
    return ways_to_win_race + 1


def solve():
    """
    code to run part one and part two
    """
    part_one_answer = part_one()
    part_two_answer = part_two()

    if part_one_answer:
        print(f"part one: {part_one_answer}")
    if part_two_answer:
        print(f"part two: {part_two_answer}")


if __name__ == '__main__':
    """
    code to run solve
    """
    solve()
