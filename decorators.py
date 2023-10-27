from typing import Callable, Any, TypeAlias

AnyFunction: TypeAlias = Callable[..., Any]


def call_counter(handler: AnyFunction) -> AnyFunction:
    """Decorator that tracks number of calls to the passed function"""

    def inner(*args, **kwargs):
        inner.calls += 1  # <- executes in runtime
        return handler(*args, **kwargs)

    inner.calls = 0  # type: ignore

    return inner


"""

@decorator
def func():
    return None

func = decorator()
    
"""