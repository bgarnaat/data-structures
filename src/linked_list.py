# -*-utf-8-*-
class LinkedList(object):
    def __init__(self, iter=None):
        self.head = None
        if iter:
            for val in iter:
                self.insert(val)
    def insert(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
    def pop(self):
        try:
            rtn_value = self.head.val
            new_head = self.head.point_to
            self.head = new_head
            self.head.point_to = None
            return rtn_value
        except AttributeError:
            return None
    def size(self):
        count = 0
        step_head = self.head
        while step_head:
            count += 1
            step_head = step_head.point_to
        return count
    def search(self, val):
        step_head = self.head
        while step_head:
            if step_head.val == val:
                return step_head
            step_head = step_head.point_to
        else:
            return None
    def remove(self, node):
        step_head = self.head
        prev_node = None
        if self.search(node.val) is None:
            raise ValueError
        while step_head:
            if step_head.val == node.val:
                if prev_node is None:
                    self.head = step_head.point_to
                    step_head.point_to = None
                    step_head = self.head
                else:
                    prev_node.point_to = step_head.point_to
                    step_head.point_to = None
                    step_head = prev_node
            prev_node = step_head
            step_head = step_head.point_to

    def display(self):
        pass

class Node(object):
    def __init__(self, val, point_to=None):
        self.val = val
        self.point_to = point_to
