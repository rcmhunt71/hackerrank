

def max_of_array_manipulation_2(list_length, queries):
    result_list = [0 for _ in range(list_length + 1)]
    for (start, stop, incr) in queries:
        result_list[start] += incr
        if stop < list_length:
            result_list[stop + 1] -= incr

    maximum = result = 0
    for val in result_list:
        result += val
        if maximum < result:
            maximum = result
    return maximum


if __name__ == '__main__':
    num_ops = 5
    query_list = [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100]
    ]

    print(f"RESULT: {max_of_array_manipulation_2(num_ops, query_list)}")
