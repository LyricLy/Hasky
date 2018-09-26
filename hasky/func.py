import copy
import inspect
from .future import Future
from .frozendict import FrozenDict
from .errors import TooManyArgumentsError

class Func:
    def __init__(self, env, name, func):
        self.name = name
        self.func = func
        self.env = env
        self.spec = inspect.getfullargspec(func)
        self.needed_args = len(self.spec.args)
        self.needed_kwargs = self.spec.kwonlyargs
        self.args = ()
        self.kwargs = FrozenDict()

    def __call__(self, *args, **kwargs):
        new_func = copy.copy(self)
        new_func.args += args
        for x in kwargs:
            self.kwargs[x] = kwargs[x]

        if len(new_func.args) > self.needed_args and self.spec.varargs is None:
            raise TooManyArgumentsError("too many arguments passed to function")
        if not all(x in self.needed_kwargs for x in new_func.kwargs) and self.spec.varkw is None:
            raise TooManyArgumentsError("unneeded kwarg passed to function")

        if len(new_func.args) >= self.needed_args and len(new_func.kwargs.keys()) >= len(self.needed_kwargs):
            if (new_func.args, new_func.kwargs) in self.env.memos[self.name]:
                return Future(self.env.memos[self.name][(new_func.args, new_func.kwargs)])
            return Future(self, new_func.args, new_func.kwargs)
        else:
            return new_func
