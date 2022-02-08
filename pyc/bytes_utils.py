from opcode import opmap


def to_byte(num: int, num_bytes=1) -> bytes:
    return num.to_bytes(num_bytes, "little")


def op_byte(op, num_bytes=1) -> bytes:
    return to_byte(opmap[op], num_bytes)


def immutable_bytestring_splice(arr: bytes, index: int, *items: bytes) -> bytes:
    return b"".join([arr[:index], *items, arr[index:]])
