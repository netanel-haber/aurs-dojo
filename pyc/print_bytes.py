from typing import List
from bytes_utils import to_byte, op_byte


def get_print_bytes(*, names_idx: int, consts_idx: int) -> List[bytes]:
    return [
        op_byte("LOAD_GLOBAL"),
        to_byte(names_idx),
        op_byte("LOAD_CONST"),
        to_byte(consts_idx),
        op_byte("CALL_FUNCTION"),
        to_byte(1),
        op_byte("POP_TOP", num_bytes=2),
    ]
