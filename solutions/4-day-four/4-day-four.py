import time

def load_data(name='data'):
    file = open(name, 'r')
    data = [line.strip() for line in file.readlines()]
    file.close()
    return data


def part_one():
    data = load_data()
    
    day_4_sum = 0
    
    for card in data:
        card_data = card.split(': ')[1].split(' | ')
        winning_numbers = [num for num in card_data[0].split(' ') if num != '']
        card_numbers = [num for num in card_data[1].split(' ') if num != '']
        
        card_score = 0
        
        for card_number in card_numbers:            
            if card_number in winning_numbers:
                if card_score > 0:
                    card_score *= 2
                else:
                    card_score += 1

        day_4_sum += card_score

    return day_4_sum


def part_two():
    
    data = load_data()
    
    mapping = [1 for _ in range(len(data))]
    
    for idx, card in enumerate(data):   
        card_data = card.split(': ')[1].split(' | ')
        winning_numbers = [num for num in card_data[0].split(' ') if num != '']
        card_numbers = [num for num in card_data[1].split(' ') if num != '']
        
        matching_numbers = len([val for val in card_numbers if val in winning_numbers])
        
        for copy in range(idx + 1, idx + matching_numbers + 1):
            mapping[copy] += mapping[idx]
    
    return sum(mapping)
        

def solve():
    part_one_answer = part_one()
    part_two_answer = part_two()

    print(f'part one: {part_one_answer}')
    print(f'part two: {part_two_answer}')


if __name__ == '__main__':
    '''
    code to run solve
    '''
    solve()
