from dis import dis

from clone_code_object import clone_code_object
from bytes_utils import immutable_bytestring_splice
from print_bytes import get_print_bytes


def fact():
    a = 8
    a = 0


fn_code_obj = fact.__code__
fn_consts = fn_code_obj.co_consts
fn_names = fn_code_obj.co_names
fn_code = fn_code_obj.co_code


augemented = clone_code_object(
    fn_code_obj,
    immutable_bytestring_splice(
        fn_code,
        -2,
        get_print_bytes(names_idx=len(fn_names), consts_idx=len(fn_consts)),
    ),
    fn_consts + ("lol",),
    fn_names + ("print",),
)

dis(augemented)
eval(augemented)
