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


def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data), end='')
        node = node.next
        if node:
            print(sep, end='')
    print()


def update_reference(current_node, tail=None):
    tail = None
    if current_node is None:
        return current_node, current_node

    next_node = current_node.next
    current_node.next = None
    if next_node is None:
        tail = current_node
        return current_node, tail
    else:
        next_node, tail = update_reference(next_node, tail)
        next_node.next = current_node
        return current_node, tail


def reverse(head):
    head, tail = update_reference(head)
    return tail


if __name__ == '__main__':

    data = [[0, 2, 4, 6, 8], [8, 6, 4, 2, 0], 2]

    tests = data[-1]

    for tests_itr in range(tests):
        llist = SinglyLinkedList()

        for val in data[tests_itr]:
            llist.insert_node(val)

        llist1 = reverse(llist.head)
        print_singly_linked_list(llist1, " ")
