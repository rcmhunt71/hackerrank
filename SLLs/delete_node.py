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


def delete_node(head, position):
    if head is not None and position >= 0:
        if position == 0:
            return head.next

        parent_node = head
        for index in range(position - 1):
            if parent_node.next is not None:
                parent_node = parent_node.next
            else:
                return head

        if parent_node is not None:
            parent_node.next = parent_node.next.next if parent_node.next is not None else None

    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()

    for _ in range(int(input())):
        llist.insert_node(int(input()))

    input_position = int(input())
    llist1 = delete_node(llist.head, input_position)

    print_singly_linked_list(llist1, ' ')
