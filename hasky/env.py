from .errors import NotFunctionError, RedefinitionError, UndefinedNameError
from .func import Func
from .future import Future

class Env:
    def __init__(self):
        self.funcs = {}
        self.memos = {}

    def __setattr__(self, name, value):
        if name in ("funcs", "memos"):
            return super().__setattr__(name, value)

        if type(value) != type(lambda: 0):
            raise NotFunctionError("non-function defined")
        elif name in self.funcs:
            raise RedefinitionError("attempting to define an already-defined name")

        self.funcs[name] = Func(self, name, value)
        self.memos[name] = {}

    def __getattr__(self, name):
        if name not in self.funcs:
            raise UndefinedNameError("attempting to get an undefined name")

        func = self.funcs[name]
        if not func.needed_args:
            return func()
        return func
