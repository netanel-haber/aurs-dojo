from heapq import heapify, heappop, heappush
from collections import Counter
from .get_file import get_file
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
    code = {}
    def crutch(node, path):
        if node.is_leaf():
            code[node.char] = path
            return
        crutch(node.left, path + "0")
        crutch(node.right, path + "1")
    crutch(tree, "")
    return {k: int(v, 2) for k, v in code.items() }



if __name__ == '__main__':
    text = get_file()
    counter: Counter = Counter(text)
    heap = heap_from_counter(counter)
    tree = tree_from_heap(heap)
    code = code_from_tree(tree)
    
















