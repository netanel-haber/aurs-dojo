import dis
from msilib.schema import Error
from random import random
from types import CodeType, FunctionType
from bytes_utils import op_to_jrel, op_to_jabs
from print_bytes import get_print_bytes


def func_edges(func:FunctionType):
    first, *_, last = func.__code__.co_lines()
    return (first, last)


def func():
    if random() > 0.5:
        res = "bigger"
    else:
        res = "smaller"
    return res

code = func.__code__

fconsts = code.co_consts
fnames = code.co_names

print_bytes= get_print_bytes(names_idx=len(fnames),consts_idx=len(fconsts))

def inject_print_after(func:FunctionType, line:int):
    (first,last) = func_edges(func)
    (,,first_line) = first
    (,,last_line) = last
    if(line > (last-first)):
        raise Error("line not in function")


def collect_jumps_after_line(code: CodeType, inject_after: int):
    filter((_,__,line)=>line>,code.co_lines)
    for (s,e,line) in code.co_lines:
        if(line>inject_after)
    for (a, b) in dis.findlinestarts(code):
        print((b, a))






print(func_edges(func))

# for line in func.__code__.co_lines():
#     print(line)
dis.dis(func)
