""" Huffman algorithm """
from utils import utils

with open(f"/home/rached/Bureau/huffman-algorithm/test", "r") as file_:
    CHARS = file_.read()

OCCURENCES_WITH_LETTERS = sorted(utils.get_occurences(CHARS))
TREES = utils.into_tree(OCCURENCES_WITH_LETTERS, method=lambda elem: elem[1], rec=False)
FINAL = utils.into_tree(TREES, rec=False)

TREE = FINAL[0]
print(TREE.find_binary("r"))
