""" Provide a tree according to the huffman algorithm """


class Node:
    """ Represent a node in the tree """

    def __init__(self, root, left=None, right=None):
        """ Represent a node in the tree """
        self.root = root
        self.left = left
        self.right = right

    def insert(self, value):
        """ Represent a new value into the tree """
        if value > self.root:
            if self.right is None:
                self.right = Node(value)

            self.right.insert(value)

        if value < self.root:
            if self.left is None:
                self.left = Node(value)

            else:
                self.left.insert(value)

    def find_binary(self, value, binary=""):
        """ Take a letter and return the associated 
            binary according to the huffman tree """
        if value > self.root:
            if self.right is tuple:
                if self.right[0] == value:
                    return binary + "0"

                else:
                    return self.right.find_binary(value, binary + "0")

            else:
                if self.left is tuple:
                    if self.left[0] == value:
                        return binary + "1"

                else:
                    return self.left.find_binary(value, binary + "0")

    def __add__(self, other_tree):
        """ Return the sum of two roots of nodes """
        return other_tree + self.root

    def __lt__(self, other_tree):
        """ Compare two roots of nodes """
        return self.root < other_tree.root

    def __str__(self):
        """ Display the representation of the tree """
        return f"NODE :  {self.root}---->LEFT : {self.right}||RIGHT : {self.left}"
