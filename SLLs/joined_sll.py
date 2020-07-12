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


def find_merge_node(head1, head2):
    nodes = {}

    node = head1
    while node is not None:
        nodes[node] = 1
        node = node.next

    node = head2
    while node is not None:
        if node in nodes:
            return node.test_data
        node = node.next
    return None


if __name__ == '__main__':

    data = [
        ([1, 2, 3],  [1, 2, 3], 1),
        ([1, 2, 3], [1, 3], 2),
        ([3], [4], 4),
    ]

    for test_case in data:
        index = test_case[-1]
        llist1 = SinglyLinkedList()
        llist2 = SinglyLinkedList()

        for llist1_item in test_case[0]:
            llist1.insert_node(llist1_item)

        for llist2_item in test_case[1]:
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(len(test_case[0])):
            if i < index:
                ptr1 = ptr1.next

        for i in range(len(test_case[1])):
            if i != len(test_case[1]) - 1:
                ptr2 = ptr2.next

        ptr2.next = ptr1
        result = find_merge_node(llist1.head, llist2.head)

        print(f"Result: {str(result)}")
