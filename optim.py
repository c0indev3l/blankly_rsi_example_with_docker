import numpy as np
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
        self._parameters.default[name] = default
        self._parameters.values[name] = values
        self._parameters.types[name] = typ

    def parameters(self):
        Param = namedtuple("Param", self._parameters.names)
        for parameter in itertools.product(*self._parameters.values.values()):
            yield (Param(*parameter))

    def parameters(self):
        Param = namedtuple("Param", self._parameters.names)
        for parameter in itertools.product(*self._parameters.values.values()):
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


def main():
    explorer = ParamaterExplorer()
    explorer.add_parameter("rsi_period", 14, np.arange(start=10, stop=20, step=1), int)
    explorer.add_parameter("rsi_min", 30, np.linspace(start=0, stop=100, num=11), float)
    explorer.add_parameter("rsi_max", 70, np.linspace(start=0, stop=100, num=11), float)
    explorer.add_constraint(lambda p: p.rsi_min < p.rsi_max)

    print(explorer)
    print()
    count = explorer.count_runs
    print(f"\tCount: {count}")
    print()
    print(f"\tDefault: {explorer.default_parameter}")
    print()
    for i, param in enumerate(explorer.parameters()):
        print(i, param)


if __name__ == "__main__":
    main()
