#! /bin/python3
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


def print_singly_linked_list(node, sep=" "):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end="")


# Complete the insertNodeAtPosition function below.
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node

    parent = head
    for _ in range(position - 1):
        if parent.next is not None:
            parent = parent.next
        else:
            break

    child = parent.next
    parent.next = new_node
    new_node.next = child
    return head


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head, ' ')
