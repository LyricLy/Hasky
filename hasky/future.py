class Future:
    def __init__(self, func, args=None, kwargs=None):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def eval(self):
        if self.args is None:
            self.result = self.func
            return self.func
        result = self.func.func(*self.args, **self.kwargs)
        self.result = result
        self.func.env.memos[self.func.name][(self.args, self.kwargs)] = result
        return result

    def __getattr__(self, name):
        if not self.result:
            self.eval()
        return getattr(self.result, name)

    def __setattr__(self, name, value):
        if name in ("func", "args", "kwargs", "result"):
            return super().__setattr__(name, value)

        if not self.result:
            self.eval()
        setattr(self.result, name, value)

    def __repr__(self):
        if not self.result:
            self.eval()
        return self.result.__repr__()

    def __str__(self):
        if not self.result:
            self.eval()
        return self.result.__str__()

    def __bytes__(self):
        if not self.result:
            self.eval()
        return self.result.__bytes__()

    def __hash__(self):
        if not self.result:
            self.eval()
        return self.result.__hash__()

    def __bool__(self):
        if not self.result:
            self.eval()
        return self.result.__bool__()

    def __dir__(self):
        if not self.result:
            self.eval()
        return self.result.__dir__()

    def __len__(self):
        if not self.result:
            self.eval()
        return self.result.__len__()

    def __length_hit__(self):
        if not self.result:
            self.eval()
        return self.result.__length_hit__()

    def __iter__(self):
        if not self.result:
            self.eval()
        return self.result.__iter__()

    def __reversed__(self):
        if not self.result:
            self.eval()
        return self.result.__reversed__()

    def __neg__(self):
        if not self.result:
            self.eval()
        return self.result.__neg__()

    def __pos__(self):
        if not self.result:
            self.eval()
        return self.result.__pos__()

    def __abs__(self):
        if not self.result:
            self.eval()
        return self.result.__abs__()

    def __invert__(self):
        if not self.result:
            self.eval()
        return self.result.__invert__()

    def __complex__(self):
        if not self.result:
            self.eval()
        return self.result.__complex__()

    def __int__(self):
        if not self.result:
            self.eval()
        return self.result.__int__()

    def __float__(self):
        if not self.result:
            self.eval()
        return self.result.__float__()

    def __index__(self):
        if not self.result:
            self.eval()
        return self.result.__index__()

    def __round__(self):
        if not self.result:
            self.eval()
        return self.result.__round__()

    def __trunc__(self):
        if not self.result:
            self.eval()
        return self.result.__trunc__()

    def __floor__(self):
        if not self.result:
            self.eval()
        return self.result.__floor__()

    def __ceil__(self):
        if not self.result:
            self.eval()
        return self.result.__ceil__()

    def __await__(self):
        if not self.result:
            self.eval()
        return self.result.__await__()

    def __aiter__(self):
        if not self.result:
            self.eval()
        return self.result.__aiter__()

    def __anext__(self):
        if not self.result:
            self.eval()
        return self.result.__anext__()

    def __call__(self, *args, **kwargs):
        if not self.result:
            self.eval()
        return self.result(*args, **kwargs)

    def __format__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__format__(x)

    def __lt__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__lt__(x)

    def __le__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__le__(x)

    def __eq__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__eq__(x)

    def __ne__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ne__(x)

    def __gt__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__gt__(x)

    def __ge__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ge__(x)

    def __delattr__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__delattr__(x)

    def __instancecheck__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__instancecheck__(x)

    def __subclasscheck__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__subclasscheck__(x)

    def __getitem__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__getitem__(x)

    def __missing__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__missing__(x)

    def __delitem__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__delitem__(x)

    def __contains__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__contains__(x)

    def __add__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__add__(x)

    def __sub__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__sub__(x)

    def __mul__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__mul__(x)

    def __matmul__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__matmul__(x)

    def __truediv__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__truediv__(x)

    def __floordiv__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__floordiv__(x)

    def __mod__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__mod__(x)

    def __divmod__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__divmod__(x)

    def __pow__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__pow__(x)

    def __lshift__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__lshift__(x)

    def __rshift__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rshift__(x)

    def __and__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__and__(x)

    def __xor__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__xor__(x)

    def __or__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__or__(x)

    def __radd__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__radd__(x)

    def __rsub__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rsub__(x)

    def __rmul__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rmul__(x)

    def __rmatmul__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rmatmul__(x)

    def __rtruediv__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rtruediv__(x)

    def __rfloordiv__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rfloordiv__(x)

    def __rmod__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rmod__(x)

    def __rdivmod__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rdivmod__(x)

    def __rpow__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rpow__(x)

    def __rlshift__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rlshift__(x)

    def __rrshift__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rrshift__(x)

    def __rand__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rand__(x)

    def __rxor__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__rxor__(x)

    def __ror__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ror__(x)

    def __iadd__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__iadd__(x)

    def __isub__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__isub__(x)

    def __imul__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__imul__(x)

    def __imatmul__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__imatmul__(x)

    def __itruediv__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__itruediv__(x)

    def __ifloordiv__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ifloordiv__(x)

    def __imod__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__imod__(x)

    def __idivmod__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__idivmod__(x)

    def __ipow__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ipow__(x)

    def __ilshift__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ilshift__(x)

    def __irshift__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__irshift__(x)

    def __iand__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__iand__(x)

    def __ixor__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ixor__(x)

    def __ior__(self, x):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        return self.result.__ior__(x)

    def __setitem__(self, x, y):
        if not self.result:
            self.eval()
        if isinstance(x, Future) and not x.result:
            x = x.eval()
        if isinstance(y, Future) and not y.result:
            y = y.eval()
        return self.result.__setitem__(x, y)
