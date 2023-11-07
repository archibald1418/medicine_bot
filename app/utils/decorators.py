from typing import Callable, Any, TypeAlias
from sqlalchemy.orm import Session

AnyFunction: TypeAlias = Callable[..., Any]


def call_counter(handler: AnyFunction) -> AnyFunction:
    """Decorator that tracks number of calls to the passed function"""

    def inner(*args, **kwargs):
        inner.calls += 1  # <- executes in runtime
        return handler(*args, **kwargs)

    inner.calls = 0  # type: ignore

    return inner


def session_is_active(func: AnyFunction):
    def assert_active(*args, session: Session):
        assert (session.is_active)
        return func(*args, session)
    return assert_active