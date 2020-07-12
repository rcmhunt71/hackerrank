from itertools import combinations
from random import randint
from time import perf_counter

num_elems = 1000
print(f"Number of Elems: {num_elems}")
#elements = [randint(-100, 100) for _ in range(num_elems - 1)]
elements = [5, 7, -5, 6, 3, 9, -8, 2, -1]
elem_sum = elements[-1]

simple_value = 0
start = perf_counter()
for index in range(len(elements) - 2, -1, -1):
    simple_value += elem_sum * elements[index]
    elem_sum += elements[index]

stop = perf_counter()
simple_time = stop - start
print(f"TOOK (SIMPLIFICATION): {simple_time}")
print(f"VALUE: {simple_value}\n")

start = perf_counter()
combo_value = sum([x[0] * x[1] for x in combinations(elements, 2)])
stop = perf_counter()
combo_time = stop - start
print(f"TOOK (COMBO SUM): {combo_time}")
print(f"VALUE: {combo_value}")

print(f"FACTOR IMPROVEMENT: {combo_time/simple_time:0.3f}")

def find_me(subarray):
    combos = combinations(list(subarray), 2)
    return sum([x[0] * x[1] for x in combos])
