class Node():
    '''singly-linked-list'''
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        cnt = 0
        while current:
            cnt += 1
            current = current.get_next()
        return cnt

    def search(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in List")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in List")
        if previous is None:
            self.head = current.get_next()
        else:
            prevous.set_next(current.get_next())

