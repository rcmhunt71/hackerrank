#!/bin/python3


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def get_node(head, position_from_tail):
    if head is None or position_from_tail < 0:
        return

    num_nodes = 0
    tail = head
    while tail.next is not None:
        tail = tail.next
        num_nodes += 1

    print(f"TAIL: {tail.test_data}")
    position_from_head = num_nodes - position_from_tail

    print(f"POS_T: {position_from_tail}")
    print(f"POS_H: {position_from_head}")

    if position_from_head < 0:
        return None
    node = head
    for _ in range(position_from_head):
        node = node.next

    return node.test_data


if __name__ == '__main__':
    tests = [([], 0), ([3, 2,  1, 0, -1], -1)]

    for tests_itr in tests:
        llist = SinglyLinkedList()

        print(f"DATA: {tests_itr[0]}")
        for elem in tests_itr[0]:
            llist.insert_node(elem)
        position = tests_itr[1]

        result = get_node(llist.head, position)
        print(f"RESULT: {result}\n\n")
