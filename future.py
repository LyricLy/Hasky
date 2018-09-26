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

    def __getattribute__(self, name):
        if name in ("func", "args", "kwargs", "result", "eval"):
            return super().__getattribute__(name)

        if not self.result:
            self.eval()
        return getattr(self.result, name)

    def __setattr__(self, name, value):
        if name in ("func", "args", "kwargs", "result"):
            return super().__setattr__(name, value)

        if not self.result:
            self.eval()
        setattr(self.result, name, value)

    def __add__(self, other):
        if not self.result:
            self.eval()
        if type(other) == Future:
            other = other.eval()
        return self.result.__add__(other)
