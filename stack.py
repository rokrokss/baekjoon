class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)	# add to back
    def pop(self):
        return self.items.pop()	# without index parameter, pops the last element
    def isEmpty(self):
        return not self.items

