from .tree import Node


def get_occurences(chars):
    occurences = {}

    for char in chars:
        if char in occurences:
            occurences[char] += 1

        else:
            occurences[char] = 1

    return occurences.items()


def get_binary(chars, tree=None):
    binary_according_to_char = {char: None for char in chars}
    print(binary_according_to_char)


def into_tree(elements, method=lambda x: x, rec=False):
    iterator = zip(elements[0::2], elements[1::2])
    tree = [
        Node(method(initial) + method(following), initial, following)
        for initial, following in iterator
    ]

    if rec is True and len(elements) != 1:
        return into_tree(tree, method, rec=True)

    else:
        return sorted(tree)
