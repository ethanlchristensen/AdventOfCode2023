
import re
import time
import pandas as pd

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
    
    start = time.time_ns()
    
    data = [line.split(' ') for line in data]
    data = [(list(line[0]), int(line[1])) for line in data]
    
    hand_assignments_value = {
        'five_of_a_kind': 7,
        'four_of_a_kind': 6,
        'full_house': 5,
        'three_of_a_kind': 4,
        'two_pair': 3,
        'one_pair': 2,
        'high_card': 1,
    }
    
    strength = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }
    
    hand_assignments = []
    
    for hand, bid in data:
        
        five_of_a_kind = 0
        four_of_a_kind = 0
        full_house = 0
        three_of_a_kind = 0
        two_pair = 0
        one_pair = 0
        high_card = 0
        
        unique_values = list(set(hand))
        
        unique_values_length = len(unique_values)
        
        if unique_values_length == len(hand):
            hand_assignments.append('high_card')
            continue
        if unique_values_length == 1:
            hand_assignments.append('five_of_a_kind')
            continue 
        if unique_values_length == 2:
            if hand.count(unique_values[0]) in [4, 1]:
                hand_assignments.append('four_of_a_kind')
                continue
            else:
                hand_assignments.append('full_house')
                continue
            break
            
        for unique_value in unique_values:
            
            count = hand.count(unique_value)
                    
            if count == 2:
                one_pair += 1
            elif count == 3:
                three_of_a_kind += 1
        
        if one_pair > 0:
            if one_pair == 1:
                hand_assignments.append('one_pair')
                continue
            elif one_pair == 2:
                hand_assignments.append('two_pair')
                continue
        
        if three_of_a_kind > 0:
            hand_assignments.append('three_of_a_kind')
            continue
        
        hand_assignments.append('not_sure')
    
    df = pd.DataFrame()
    df['hand'] = [''.join(line[0]) for line in data]
    df['card_1_val'] = [strength[line[0][0]] for line in data]
    df['card_2_val'] = [strength[line[0][1]] for line in data]
    df['card_3_val'] = [strength[line[0][2]] for line in data]
    df['card_4_val'] = [strength[line[0][3]] for line in data]
    df['card_5_val'] = [strength[line[0][4]] for line in data]
    df['hand_type']  = hand_assignments
    df['hand_type_val'] = [hand_assignments_value[hand_assignment] for hand_assignment in hand_assignments]
    df['bid'] = [line[1] for line in data]
    df = df.sort_values(by=['hand_type_val', 'card_1_val', 'card_2_val', 'card_3_val', 'card_4_val', 'card_5_val']).reset_index()
    df['idx'] = list(range(1, len(df) + 1))
    
    result = sum([a * b for a, b in zip(df['bid'].to_list(), df['idx'].to_list())])
    
    time_to_get = time.time_ns() - start
    
    return result, time_to_get

def part_two():
    """
    code to solve part two
    """
    return None, None
    
def solve():
    """
    code to run part one and part two
    """
    part_one_answer, time_to_get = part_one()
    part_two_answer, time_to_get = part_two()
    
    if part_one_answer:
        print(f"part one: {part_one_answer}")
    if part_two_answer:
        print(f"part two: {part_two_answer}")
    
if __name__ == '__main__':
    """
    code to run solve
    """
    solve()
