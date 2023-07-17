def to_param_string(param):
    s = ""

    def get_type_string(typ):
        know_typ = {int: "int", float: "float", str: "str"}
        return know_typ[typ]

    for i, (k, v) in enumerate(zip(param._fields, param)):
        if i != 0:
            s += ","
        s += f"{k}::{get_type_string(type(v))}={v}"
    return s
