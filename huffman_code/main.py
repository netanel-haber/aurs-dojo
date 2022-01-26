from bisect import bisect
from collections import Counter
from heapq import heapify, heappop, heappush
from time import time
from typing import Generator

from .files import get_file, read_bin_from_file, write_bin_to_file
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
        if node.char:
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


def decode(byte_arr: bytes, tree: Node) -> str:
    text = ""
    bin_text = hydrate_text(byte_arr)
    node = tree
    for bit in bin_text:
        node = node.left if bit == "0" else node.right
        if node.char:
            text += node.char
            node = tree
    return text


def decode_yoav(byte_arr: bytes, code: dict) -> Generator[str, None, None]:
    str_rep_chars = sorted((v, k) for k, v in code.items())
    sorted_str_reps = [pair[0] for pair in str_rep_chars]
    rep_lengths = [len(rep) for rep in sorted_str_reps]
    chars = [pair[1] for pair in str_rep_chars]
    buffer_length = (len(max(sorted_str_reps, key=len)) // 8) + 1
    sorted_int_reps = [
        int(rep, 2) << (8 * buffer_length - len(rep)) for rep in sorted_str_reps
    ]
    assert sorted(sorted_int_reps) == sorted_int_reps
    mask = (1 << (buffer_length * 8)) - 1
    buffer = 0
    used_bits = (buffer_length + 1) * 8
    for next_byte in byte_arr[:-1]:
        used_bits -= 8
        buffer &= mask
        buffer <<= 8
        buffer |= next_byte
        while used_bits <= 8:
            i = bisect(sorted_int_reps, (buffer >> (8 - used_bits)) & mask) - 1
            used_bits += rep_lengths[i]
            yield chars[i]
    while (buffer_length + 1) * 8 - used_bits != byte_arr[-1]:
        i = bisect(sorted_int_reps, (buffer << (used_bits - 8)) & mask) - 1
        used_bits += rep_lengths[i]
        yield chars[i]


if __name__ == "__main__":
    text = get_file()
    counter: Counter = Counter(text)
    heap = heap_from_counter(counter)
    tree = tree_from_heap(heap)
    code = code_from_tree(tree)
    encoded = encode(text, code)
    write_bin_to_file(encoded)
    bin_text = read_bin_from_file()
    a = time()
    decoded = "".join(decode_yoav(bin_text, code))
    assert decoded == text
    b = time()
    print(f"decode yoav: {b - a}")
    a = time()
    decoded = decode(bin_text, tree)
    assert decoded == text
    b = time()
    print(f"decode: {b - a}")
