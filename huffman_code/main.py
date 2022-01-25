from heapq import heapify, heappop, heappush
from collections import Counter
from .files import get_file, write_bin_to_file, read_bin_from_file
from .node import Node


def heap_from_counter(counter: Counter):
    leaves = [Node(weight, char) for (char, weight) in counter.items()]
    heapify(leaves)
    return leaves


def tree_from_heap(heap):
    while len(heap) > 1:
        smallest = heappop(heap)
        bigger = heappop(heap)
        internal_node = Node(
            smallest.weight + bigger.weight, left=smallest, right=bigger
        )
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
    joined = "".join(code[c] for c in text)
    padding_length = 8 - (len(joined) % 8)
    joined += "0" * (padding_length)
    barr = bytearray()
    idx = 0
    padded_length = len(joined)
    while idx < padded_length:
        str_byte = joined[idx : idx + 8]
        barr.append(bin_str_to_int(str_byte))
        idx += 8
    barr.append(padding_length)
    return barr


def bin_str_to_int(str):
    return int(str, base=2)


def raw_bin(b):
    return bin(b)[2:].rjust(8, "0")


def hydrate_text(byte_arr):
    string = "".join(raw_bin(b) for b in byte_arr[:-2])
    last_padding = bin_str_to_int(raw_bin(byte_arr[-1]))
    last = raw_bin(byte_arr[-2])[:-last_padding]
    return string + last


def decode(byte_arr: bytes, tree: Node):
    text = ""
    bin_text = hydrate_text(byte_arr)
    node = tree
    for bit in bin_text:
        node = node.left if bit == "0" else node.right
        if node.is_leaf():
            text += node.char
            node = tree
    return text


if __name__ == "__main__":
    text = get_file()
    counter: Counter = Counter(text)
    heap = heap_from_counter(counter)
    tree = tree_from_heap(heap)
    code = code_from_tree(tree)
    encoded = encode(text, code)
    write_bin_to_file(encoded)
    bin_text = read_bin_from_file()
    decoded = decode(bin_text, tree)
    assert decoded == text
