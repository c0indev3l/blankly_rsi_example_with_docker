import numpy as np
import itertools
from collections import namedtuple


class Parameters:
    def __init__(self):
        self.names = []
        self.values = dict()
        self.default = dict()


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
                s += f"\n\t\t{name}: {default}\t{values}"
        if len(self._constraints) > 0:
            s += "\n\tConstraints"
            for constraint in self._constraints:
                s += "\n\t\t" + repr(constraint)
        return s

    def add_parameter(self, name, default, values):
        self._parameters.names.append(name)
        self._parameters.default[name] = default
        self._parameters.values[name] = values

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


explorer = ParamaterExplorer()
explorer.add_parameter("rsi_period", 14, np.linspace(start=5, stop=20, num=11))
explorer.add_parameter("rsi_min", 30, np.linspace(start=0, stop=100, num=11))
explorer.add_parameter("rsi_max", 70, np.linspace(start=0, stop=100, num=11))
explorer.add_constraint(lambda p: p.rsi_min < p.rsi_max)

print(explorer)
for i, param in enumerate(explorer.parameters()):
    print(i, param)
