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


def mergeLists(head_1, head_2):

    merged = SinglyLinkedList()

    if head_1 is None or head_2 is None:
        if head_1 is None:
            append_linked_list(head_2, merged)
        elif head_2 is None:
            append_linked_list(head_1, merged)
        return merged

    node_1 = head_1
    node_2 = head_2
    while node_1 is not None and node_2 is not None:
        if node_2.data <= node_1.data:
            merged.insert_node(node_2.data)
            node_2 = node_2.next
        else:
            merged.insert_node(node_1.data)
            node_1 = node_1.next

    if node_1 is None:
        append_linked_list(node_2, merged)
    elif node_2 is None:
        append_linked_list(node_1, merged)
    return merged


def append_linked_list(head_node, dest_list):
    while head_node is not None:
        dest_list.insert_node(head_node.data)
        head_node = head_node.next


def get_tail(node):
    while node is not None:
        node = node.next
    return node


if __name__ == '__main__':

    data = [[[1,2,3], [1,2,3]]]
    tests = len(data)

    for tests_itr in data:
        print(tests_itr)
        llist1 = SinglyLinkedList()
        llist2 = SinglyLinkedList()

        for val in tests_itr[0]:
            llist1.insert_node(val)
        for val in tests_itr[1]:
            llist2.insert_node(val)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist1.head, '.')
        print_singly_linked_list(llist2.head, '.')
        print_singly_linked_list(llist3.head, ' ')
