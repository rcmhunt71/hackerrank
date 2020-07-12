#!/bin/python3


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node


def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data), end='')
        node = node.next
        if node:
            print(sep, end='')
        print()


def print_node(node, preamble):
    if node is None:
        print(f"NONE node. PREAMBLE: {preamble}")
        return
    try:
        node_prev = node.prev.test_data
    except AttributeError:
        node_prev = None

    try:
        node_next = node.next.test_data
    except AttributeError:
        node_next = None
    print(f"{preamble}: {node_prev} --> {node.data} --> {node_next}")


def node_copy(node):
    """
    Copy is needed due the python assignment being a reference, not a copy,
    so any operation on the node is reflected in all subsequent calls
    """
    new_node = DoublyLinkedListNode(node.test_data)
    new_node.next = node.next
    new_node.prev = node.prev
    return new_node


def reverse(node):
    while True:
        temp = node_copy(node)
        node.prev = temp.next
        node.next = temp.prev

        if temp.next is None:
            break

        node = temp.next
    return node


if __name__ == '__main__':

    data = [[1, 2, 3, 4]]
    t = len(data)

    for test_case in data:
        llist = DoublyLinkedList()

        for elem in test_case:
            llist.insert_node(elem)

        print_doubly_linked_list(llist.head, ' ')
        llist1_node = reverse(llist.head)
        print_doubly_linked_list(llist1_node, ' ')
