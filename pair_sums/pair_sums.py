#!/bin/python3

from collections import namedtuple
from itertools import islice, combinations
import pprint
from random import randint
import sys
from time import perf_counter

MaxSubstring = namedtuple("max_substring", ["value", "substring"])


class LargestSubString:
    def __init__(self, list_size, simple_case=False):
        self.list_size = list_size
        self.elements = self._generate_data(simple_case)
        self.max_substring = MaxSubstring(None, [])

    def get_max_value(self):
        return self.max_substring.value

    def get_max_substring(self):
        return self.max_substring.substring

    def _generate_data(self, simple_case=True):
        # default_list = [5, 7, -5, 6, 3, 9, -8, 2, -1, 10]
        default_list = [-3, 7, -2, 3, 5, -2]
        start = perf_counter()
        data = [randint(-1000, 1000) for _ in range(self.list_size)] if not simple_case else default_list
        print(f"DATA GEN {len(data)} Elements --> {perf_counter() - start:0.6f} sec")
        return data

    @staticmethod
    def _calculate_sum_of_product_sums(sub_array):
        value = 0
        if sub_array:
            elem_sum = sub_array[-1]
            for index in range(len(sub_array) - 2, -1, -1):
                value += elem_sum * sub_array[index]
                elem_sum += sub_array[index]
        return value

    @staticmethod
    def _brute_force_calc(sub_array):
        combos = combinations(list(sub_array), 2)
        return sum([x[0] * x[1] for x in combos])

    def largest_value(self, cache_length=4):
        storage = {}
        cumulative_time = 0
        precalcs = 0
        full_calcs = 0
        duplicates = 0

        t_start = perf_counter()
        for sub_array_size in range(1, len(self.elements) + 1):
            sub_array_start_time = perf_counter()
            calcs = 0
            # print(f"Subarray_size: {sub_array_size}   Checks: {len(self.elements) - sub_array_size + 1}"
            #       f" for list len: {len(self.elements)}")
            for start in range(len(self.elements) - sub_array_size + 1):
                calcs += 1
                sub_array = tuple(islice(self.elements, start, sub_array_size, 1))
                length = len(sub_array)
                if length >= cache_length:
                    if sub_array in storage:
                        duplicates += 1
                        continue

                    if sub_array[:-1] in storage:
                        precalcs += 1
                        storage[sub_array] = storage[sub_array[:-1]] + sum(sub_array[:-1]) * sub_array[-1]

                    elif sub_array[1:] in storage:
                        precalcs += 1
                        storage[sub_array] = storage[sub_array[1:]] + sum(sub_array[1:]) * sub_array[0]

                    else:
                        full_calcs += 1
                        storage[sub_array] = self._calculate_sum_of_product_sums(sub_array)
                else:
                    full_calcs += 1
                    storage[sub_array] = self._calculate_sum_of_product_sums(sub_array)

                # noinspection PyTypeChecker
                if self.max_substring.value is None or storage[sub_array] > self.max_substring.value:
                    self.max_substring = MaxSubstring(storage[sub_array], sub_array)

            sub_array_loop_time = perf_counter() - sub_array_start_time
            cumulative_time += sub_array_loop_time
            if sub_array_size % 200 == 0:
                print(f"LENGTH {sub_array_size} of {self.list_size} COMPLETE: {sub_array_loop_time:0.4f} sec "
                      f"-> {cumulative_time:0.4f} sec  -> {calcs} calcs")

        t_total = perf_counter() - t_start
        print(f"\n"
              f"Elements:    {self.list_size:>,}\n"
              f"Took:        {t_total:>0.6f} sec\n"
              f"Cache Start: {cache_length}\n"
              f"Calcs:       {full_calcs:>,}\n"
              f"Precalcs:    {precalcs:>,}\n"
              f"Duplicates:  {duplicates:>,}\n"
              f"Total:       {full_calcs + precalcs + duplicates:>,}\n")
        return self.max_substring

# Need to reduce the data set, and prevent recalculating known entities... progressive caching or windowing.


if __name__ == '__main__':
    l_size = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    simple = l_size < 0

    lss = LargestSubString(list_size=l_size, simple_case=simple)
    result = lss.largest_value(cache_length=25)
    if len(lss.elements) < 100:
        print(f"DATA: {pprint.pformat(lss.elements)}")
    print(f"Result: {result.value:,} --> {result.substring}")
