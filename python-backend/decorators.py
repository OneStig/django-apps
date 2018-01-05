def test_decorator(func):

    def wrap_func():
        print("before call")
        func()
        print("after func call")

    return wrap_func

def requires_decorator():
    print("requires decorator")

@test_decorator
def real_decorator():
    print("requires decorator")

if __name__ == '__main__':
    requires_decorator = test_decorator(requires_decorator)

    requires_decorator()

    real_decorator()
