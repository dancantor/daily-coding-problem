"""
Problem Statement:
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

from typing import List


def nr_of_possible_ways_to_climb(nr_of_steps: int, steps_at_a_time: List[int]) -> int:
    if nr_of_steps == 0:
        return 1
    
    possible_ways_dynamic = [0 for i in range(nr_of_steps + 1)]
    possible_ways_dynamic[0] = 1
    
    for i in range(1, nr_of_steps + 1):
        for step in steps_at_a_time:
            if step <= i:
                possible_ways_dynamic[i] += possible_ways_dynamic[i - step]
    
    return possible_ways_dynamic[nr_of_steps]


print(f"N=4, steps [1,2]: {nr_of_possible_ways_to_climb(4, [1,2])}")
print(f"N=5, steps [1,2]: {nr_of_possible_ways_to_climb(5, [1,2])}")
print(f"N=3, steps [1,3,5]: {nr_of_possible_ways_to_climb(3, [1,3,5])}")
print(f"N=0, steps [1,2]: {nr_of_possible_ways_to_climb(0, [1,2])}")
print(f"N=1, steps [1,2]: {nr_of_possible_ways_to_climb(1, [1,2])}")
print(f"N=2, steps [1,2]: {nr_of_possible_ways_to_climb(2, [1,2])}")

