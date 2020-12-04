class FuncAdd:
    all_funcs = {}
    # Good Luck!
    def __init__(self, func, *args, **kwargs):
        self.func = func
        if func.__name__ not in FuncAdd.all_funcs.keys():
            FuncAdd.all_funcs[func.__name__] = (func(*args, **kwargs),)
        else:
            FuncAdd.all_funcs[func.__name__] += (func(*args, **kwargs),)
        
    def __call__(self, *args, **kwargs):
        results = tuple(FuncAdd.all_funcs[funcname] for funcname in FuncAdd.all_funcs.keys() if self.func.__name__ == funcname)
        return results[0]
            
    @staticmethod
    def delete(func):
        del FuncAdd.all_funcs[func.__name__]


@FuncAdd
def foo():
    return 'Hello'

@FuncAdd
def foo():
    return 'World'

print(foo())