from types import CodeType


def clone_code_object(
    initial: CodeType, co_code: bytes, co_consts: tuple, co_names: tuple
) -> CodeType:
    return CodeType(
        initial.co_argcount,
        initial.co_posonlyargcount,
        initial.co_kwonlyargcount,
        initial.co_nlocals,
        initial.co_stacksize,
        initial.co_flags,
        co_code or initial.co_code,
        co_consts or initial.co_consts,
        co_names or initial.co_names,
        initial.co_varnames,
        initial.co_filename,
        initial.co_name,
        initial.co_firstlineno,
        initial.co_lnotab,
        initial.co_freevars,
        initial.co_cellvars,
    )
