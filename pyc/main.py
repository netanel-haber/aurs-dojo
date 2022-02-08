from dis import dis

from augement_code_object import augment_code_object
from bytes_utils import immutable_bytestring_splice, to_byte, op_byte


def fact():
    a = 8
    a = 0


fn_code_obj = fact.__code__
fn_consts = fn_code_obj.co_consts
fn_names = fn_code_obj.co_names
fn_code = fn_code_obj.co_code

co_code = immutable_bytestring_splice(
    fn_code,
    -2,
    op_byte("LOAD_GLOBAL"),
    to_byte(len(fn_names)),
    op_byte("LOAD_CONST"),
    to_byte(len(fn_consts)),
    op_byte("CALL_FUNCTION"),
    to_byte(1),
    op_byte("POP_TOP", num_bytes=2),
)

augemented = augment_code_object(
    fn_code_obj, co_code, fn_consts + ("lol",), fn_names + ("print",)
)

dis(augemented)
print(co_code)
eval(augemented)
