from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            if self.current is None:
                self.current = self.storage.head
            self.current.value = item
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.index = 0

    def append(self, item):
        if self.index == len(self.storage):
            self.index = 0
        self.storage[self.index] = item
        self.index += 1

    def get(self):
        return [item for item in self.storage if item]
