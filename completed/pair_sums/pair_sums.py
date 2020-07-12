#!/bin/python3

from collections import namedtuple
from random import randint
from itertools import islice, combinations
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
        default_list = [5, 7, -5, 6, 3, 9, -8, 2, -1, 10]
        start = perf_counter()
        data = [randint(-1000, 1000) for _ in range(self.list_size)] if not simple_case else default_list
        print(f"DATA GEN {l_size}: {perf_counter() - start:0.4f} sec")
        return data

    @staticmethod
    def _calculate_sum_of_product_sums(sub_array):
        value = 0
        if sub_array:
            elem_sum = sub_array.pop()
            for index in range(len(sub_array) - 1, -1, -1):
                value += elem_sum * sub_array[index]
                elem_sum += sub_array[index]
        return value

    @staticmethod
    def _brute_force_calc(sub_array):
        combos = combinations(list(sub_array), 2)
        return sum([x[0] * x[1] for x in combos])

    def largest_value(self, optimized=True):
        storage = {}
        cumulative_time = 0

        t_start = perf_counter()
        for sub_array_size in range(1, len(self.elements) + 1):
            sub_array_start_time = perf_counter()

            for start in range(len(self.elements)):
                sub_array = list(islice(self.elements, start, sub_array_size, 1))
                value = (self._calculate_sum_of_product_sums(sub_array) if optimized else
                         self._brute_force_calc(sub_array))

                # noinspection PyTypeChecker
                if self.max_substring.value is None or value > self.max_substring.value:
                    self.max_substring = MaxSubstring(value, sub_array)

            sub_array_loop_time = perf_counter() - sub_array_start_time
            cumulative_time += sub_array_loop_time
            if sub_array_size % 10 == 0:
                print(f"LENGTH {sub_array_size} of {self.list_size} COMPLETE: {sub_array_loop_time:0.4f} sec "
                      f"-> {cumulative_time:0.4f} sec")

        t_total = perf_counter() - t_start
        print(f"Took: {t_total:0.4f} sec")
        return self.max_substring

# Need to reduce the data set, and prevent recalculating known entities... progressive caching or windowing.


if __name__ == '__main__':
    (simple, optimize) = (False, True)
    l_size = 1000

    result = LargestSubString(list_size=l_size).largest_value()
    print(f"Result: {result.value:,} --> {result.substring}")
