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


def removeDuplicates(head):
    node = head
    while node is not None:
        if node.next is not None and node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head


if __name__ == '__main__':
    data = [
        [1, 2, 3, 4, 4, 5],
        [],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1],
        [8, 5, 3, 3, 1, 5, 7, 5],
        [1]
    ]

    for test_case in data:
        llist = SinglyLinkedList()

        for llist_item in test_case:
            llist.insert_node(llist_item)

        print("\nORIG: ", end='')
        print_singly_linked_list(llist.head, ' ')
        llist1 = removeDuplicates(llist.head)
        print("UPDATE: ", end='')
        print_singly_linked_list(llist1, ' ')
