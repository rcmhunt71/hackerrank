
def shift_list_left(element_list, num_shifts):
    for rotation in range(num_shifts):
        element_list.insert(len(element_list), element_list.pop(0))
        print(f"{rotation}: {element_list}")
    return element_list


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    result = shift_list_left(a, d)
    print(" ".join(result))
