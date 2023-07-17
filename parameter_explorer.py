import itertools
from collections import namedtuple


class Parameters:
    def __init__(self):
        self.names = []
        self.values = dict()
        self.default = dict()
        self.types = dict()


class ParamaterExplorer:
    def __init__(self):
        self._parameters = Parameters()
        self._constraints = []

    def __str__(self):
        s = "ParameterExplorer"
        if len(self._parameters.names) > 0:
            s += "\n\tParameters"
            for name in self._parameters.names:
                values = self._parameters.values[name]
                default = self._parameters.default[name]
                n = len(values)
                s += f"\n\t\t{name}: {default}\t{values} ({n} values)"
        if len(self._constraints) > 0:
            s += "\n\tConstraints"
            for constraint in self._constraints:
                s += "\n\t\t" + repr(constraint)
        return s

    def add_parameter(self, name, default, values, typ=float):
        assert name not in self._parameters.names, f"parameter '{name}' was ever set"
        self._parameters.names.append(name)
        self._parameters.default[name] = typ(default)
        self._parameters.values[name] = values
        self._parameters.types[name] = typ

    def parameters(self):
        Param = namedtuple("Param", self._parameters.names)
        for parameter in itertools.product(*self._parameters.values.values()):
            parameter = [self._parameters.types[self._parameters.names[i]](p) for i, p in enumerate(parameter)]
            parameter = Param(*parameter)
            allowed = True
            for constraint in self._constraints:
                if not constraint(parameter):
                    allowed = False
            if allowed:
                yield (parameter)

    def add_constraint(self, constraint):
        self._constraints.append(constraint)

    def default(self, name):
        return self._parameters.default[name]

    @property
    def count_runs(self):
        i = 0
        for parameter in self.parameters():
            i += 1
        return i

    @property
    def default_parameter(self):
        Param = namedtuple("Param", self._parameters.names)
        return Param(*self._parameters.default.values())


def to_param_string(param):
    s = ""
    def get_type_string(typ):
        know_typ = {
            int: "int",
            float: "float",
            str: "str"
        }
        return know_typ[typ]
    for i, (k, v) in enumerate(zip(param._fields, param)):
        if i != 0:
            s += ","
        s += f"{k}::{get_type_string(type(v))}={v}"
    return s