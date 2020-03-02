class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_value(self):
        return self.val

    def get_next_node(self):
        return self.next_node


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def has_space(self):
        if self.size < self.limit:
            return True
        else:
            return False

    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True

    def peek(self):
        if not self.is_empty():
            print(self.top_item.get_value())
        else:
            print("the stack is empty")

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("stack overflow")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = self.top_item.get_next_node()
            print(item_to_remove.val)
        else:
            print("the stack is empty")
