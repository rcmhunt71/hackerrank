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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def has_cycle(head):
    ptrs = {}
    node = head

    while node is not None:
        if node in ptrs:
            return True
        ptrs[node] = 1
        node = node.next

    return False


if __name__ == '__main__':
    tests = [
        [1, 3, 3, 5, 3]
    ]

    for test_case in tests:
        llist = SinglyLinkedList()
        index = 3
        llist_count = len(test_case)

        for llist_item in test_case:
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(len(test_case)):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        print(str(result) + '\n')
