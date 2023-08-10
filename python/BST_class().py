class BSTNode(object):
    def __init__(self, key, value=None, right=None, left=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left

    def add(self, key):
        side = 'left' if key < self.key else 'right'
        node = getattr(self,side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)

    def search(self, key):
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.search(key)
