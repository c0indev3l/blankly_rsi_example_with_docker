import os
from munch import Munch

PARAMS = os.getenv("PARAMS", default=None)
D_PARAMS = {}
print(f"PARAMS ENV2 VAR {PARAMS}")
if PARAMS is not None:
    PARAMS = PARAMS.split(",")

    def gettype(name):
        know_types = {
            "int": int,
            "float": float,
            "str": str
        }
        return know_types[name]
        """
        t = getattr(__builtins__, name)
        if isinstance(t, type):
            return t
        raise ValueError(name)
        """

    for param in PARAMS:
        name_typ, value = param.split("=")
        name, typ = name_typ.split("::")
        typ = gettype(typ)
        D_PARAMS[name] = typ(value)
    print(D_PARAMS)


def get_variable(name):
    return D_PARAMS[name]


def init_symbol_variables(state_variables, symbol):
    # d = {}
    d = Munch()  # a dictionary that supports attribute-style access, a la JavaScript
    setattr(state_variables, symbol, d)
