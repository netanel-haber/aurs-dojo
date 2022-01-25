from heapq import heapify, heappop, heappush
from collections import Counter
from os import path
from .get_file import get_file, location
from .node import Node

def heap_from_counter(counter:Counter):
    leaves = [Node(weight, char) for (char, weight) in counter.items()]
    heapify(leaves)
    return leaves

def tree_from_heap(heap):
    while(len(heap)>1):
        smallest = heappop(heap)
        bigger = heappop(heap)
        internal_node = Node(smallest.weight+bigger.weight, left=smallest, right=bigger)
        heappush(heap, internal_node)
    return heappop(heap)

def code_from_tree(tree):
    char_to_str_repr = {}
    def crutch(node, rep):
        if node.is_leaf():
            char_to_str_repr[node.char] = rep
            return
        crutch(node.left, rep + "0")
        crutch(node.right, rep + "1")
    crutch(tree, "")
    return char_to_str_repr

def encode(text, code):
    joined = "".join([code[c] for c in text])
    padding_length = len(joined)%8
    joined += "0"*(padding_length)
    barr = bytearray()
    window = 0
    paddedLength = len(joined)
    while window<paddedLength:
        barr.append(int(joined[window:window+8],base=2))
        window+=8
    barr.append(padding_length)
    return barr

if __name__ == '__main__':
    text = get_file()
    counter: Counter = Counter(text)
    heap = heap_from_counter(counter)
    tree = tree_from_heap(heap)
    code = code_from_tree(tree)
    encoded = encode(text, code)
    with open(path.join(location,'out.bin'), 'wb') as f:
        f.write(encoded)
    
















