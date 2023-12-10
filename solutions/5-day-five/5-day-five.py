
import re
import time
import numpy as np
from tqdm import tqdm


def load_data(name='data'):
    file = open(name, 'r')
    data = [line.strip() for line in file.readlines() if line.strip() != '']
    file.close()
    return data


def part_one():
    """
    code to solve part one
    """

    data = load_data()
    
    start = time.time_ns()

    seeds = [int(x) for x in data.pop(0).split(': ')[1].split(' ')]

    seed_locations = []

    stages = [line[:-1] for line in data if not line[0].isdigit()]

    stages_map = {stage: {} for stage in stages}

    current_stage = None

    stages_poppable = stages[:]
    
    source_ranges = []
    
    destination_ranges = []
    
    for line in data:
        if not line[0].isdigit():
            if current_stage is not None:
                stages_map[current_stage] = {
                    'source': source_ranges,
                    'destination': destination_ranges
                }
                source_ranges, destination_ranges = [], []
            current_stage = stages_poppable.pop(0)
        else:
            destination_start, source_start, range_length = (int(val) for val in line.split())
            source_ranges.append((source_start, source_start + range_length))
            destination_ranges.append((destination_start, destination_start + range_length))
            
    stages_map[current_stage] = {
        'source': source_ranges,
        'destination': destination_ranges
    }
    
    min_seed_location = float('inf')
    
    for seed in seeds:
        current_val = seed
        for stage in stages:
            current_map = stages_map[stage]
            source_ranges = current_map['source']
            destination_ranges = current_map['destination']
            for idx, source_range in enumerate(source_ranges):
                start, end = source_range
                if current_val >= start and current_val < end:
                    current_val = destination_ranges[idx][0] + (current_val - start)
                    break
        if current_val < min_seed_location:
            min_seed_location = current_val
    
    total_time = time.time_ns() - start
    
    return min_seed_location, total_time


def part_two():
    """
    code to solve part two
    """
    return None, None
    data = load_data()
    
    start = time.time_ns()
    
    seed_ranges = []

    intial_seeds = [int(x) for x in data.pop(0).split(': ')[1].split(' ')]
    
    for idx in range(0, len(intial_seeds), 2):
        start, range_length = intial_seeds[idx], intial_seeds[idx + 1]
        seed_ranges.append((start, start + range_length))

    stages = [line[:-1] for line in data if not line[0].isdigit()]

    stages_map = {stage: {} for stage in stages}

    current_stage = None

    stages_poppable = stages[:]
    
    source_ranges = []
    
    destination_ranges = []
    
    for line in data:
        if not line[0].isdigit():
            if current_stage is not None:
                stages_map[current_stage] = {
                    'source': source_ranges,
                    'destination': destination_ranges
                }
                source_ranges, destination_ranges = [], []
            current_stage = stages_poppable.pop(0)
        else:
            destination_start, source_start, range_length = (int(val) for val in line.split())
            source_ranges.append((source_start, source_start + range_length))
            destination_ranges.append((destination_start, destination_start + range_length))
            
    stages_map[current_stage] = {
        'source': source_ranges,
        'destination': destination_ranges
    }
    
    min_seed_location = float('inf')
    for seed_range in seed_ranges:
        for seed in range(seed_range[0], seed_range[1]):
            current_val = seed
            need_to_break = False
            for stage in stages:
                if need_to_break:
                    print("break")
                    break
                current_map = stages_map[stage]
                source_ranges = current_map['source']
                destination_ranges = current_map['destination']
                for idx, source_range in enumerate(source_ranges):
                    start, end = source_range
                    
                    if current_val >= start and current_val < end:
                        current_val = destination_ranges[idx][0] + (current_val - start)
                        break
                    
            if current_val < min_seed_location:
                min_seed_location = current_val
    
    total_time = time.time_ns() - start
    
    return min_seed_location, total_time


def solve():
    """
    code to run part one and part two
    """

    part_one_answer, time_to_run = part_one()
    part_two_answer, time_to_run = part_two()

    if part_one_answer:
        print(f"part one: {part_one_answer}")
    if part_two_answer:
        print(f"part two: {part_two_answer[0]}")


if __name__ == '__main__':
    """
    code to run solve
    """
    solve()
