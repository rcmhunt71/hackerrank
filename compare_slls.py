#!/bin/python3
import os


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


def print_singly_linked_list(node, sep=' '):
    while node:
        print(str(node.data), end='')
        node = node.next
        if node:
            print(sep, end='')
    print()


def compare_lists(llist1_head, llist2_head):
    if None in [llist1_head, llist2_head]:
        return llist1_head is None and llist2_head is None

    (node_1, node_2) = (llist1_head, llist2_head)
    while True:
        if None in [node_1, node_2]:
            return node_1 is None and node_2 is None

        if node_1.data != node_2.data:
            return False

        (node_1, node_2) = (node_1.next, node_2.next)


if __name__ == '__main__':
    data = [
        ([1, 1], [2, 2]),
        ([1, 2], [1, 2]),
        ([], []),
        ([1, 2], [1, 2, 3]),
        ([], [1, 2]),
        ([1, 2, 3], [])
    ]

    for test_num, test_case in enumerate(data):
        llist1 = SinglyLinkedList()
        llist2 = SinglyLinkedList()

        for llist1_item in test_case[0]:
            llist1.insert_node(llist1_item)

        for llist2_item in test_case[1]:
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        border = "*"
        print(f"{border * 40}\n{border} TEST CASE #:{test_num}\n{border * 40}")
        print("L1: ", end='')
        print_singly_linked_list(node=llist1.head)

        print("L2: ", end='')
        print_singly_linked_list(node=llist2.head)

        print(f"Lists Match: {str(result)}\n")

