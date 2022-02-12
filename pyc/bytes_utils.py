from opcode import opmap, hasjabs, hasjrel, opname
from typing import List


def to_byte(num: int, num_bytes=1) -> bytes:
    return num.to_bytes(num_bytes, "little")


def op_byte(op, num_bytes=1) -> bytes:
    return to_byte(opmap[op], num_bytes)


def immutable_bytestring_splice(arr: bytes, index: int, items: List[bytes]) -> bytes:
    return b"".join([arr[:index], *items, arr[index:]])


op_to_jrel = {opname[i]: i for i in hasjrel}
op_to_jabs = {opname[i]: i for i in hasjabs}
