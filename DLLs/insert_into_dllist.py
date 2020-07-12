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


#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sorted_insert(head, data):
    node = head
    insert_node = DoublyLinkedListNode(data)
    while node is not None:
        if node.next is None or data < node.data or node.data <= data <= node.next.data:
            break
        node = node.next

    if node is None:
        return insert_node

    if node.next is None:
        node.next = insert_node
        insert_node.prev = node

    elif data < node.data:
        insert_node.next = node
        node.prev = insert_node
        head = insert_node

    else:
        next_node = node.next
        node.next = insert_node
        insert_node.prev = node

        insert_node.next = next_node
        next_node.prev = insert_node

    return head


if __name__ == '__main__':

    test_data = [
        ([1, 3, 4, 10], 5),
        ([1, 3, 4, 10], 0),
        ([1, 3, 4, 10], 20),
        ([1, 3, 4, 10], 3),
        ([], 3),
        ([3, 3, 3], 3),
        ([1, 3, 3, 4, 10], 3),
    ]

    for test_case in test_data:
        llist = DoublyLinkedList()
        for llist_item in test_case[0]:
            llist.insert_node(llist_item)

        llist1_head = sorted_insert(llist.head, test_case[1])

        print_doubly_linked_list(llist1_head, ' ')
