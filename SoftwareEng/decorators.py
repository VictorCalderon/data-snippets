"""Basic decorator implementations
"""
import time
import signal
from functools import wraps


# Real-life timeout decorator
def raise_timeout(*args, **kwargs):
    """Timeout signal handler
    """
    raise TimeoutError()


# Set signal timeout handler setup
signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)


def timeout(s: int):
    """[summary]

    Args:
        s (int): Seconds before timeout

    Returns:
        decorator: Timeout decorator
    """

    # Define decorator
    def decorator(func):

        # Define wrapper
        @wraps(func)
        def wrapper(*args, **kwargs):

            # Set alarm signal in s seconds
            signal.alarm(s)

            try:
                # Call decorated function
                return func(*args, **kwargs)

            finally:

                # Cancel alarm
                signal.alarm(0)

        # Return wrapper
        return wrapper

    # Return decorator
    return decorator


# Simple decorator that doubles parameters values
def double_args(func):
    """Double each parameters value

    Args:
        func (function): A function that takes numerical values as parameters.
    """

    # Define wrapper
    @wraps(func)
    def wrapper(a, b):

        # Return multiplied variables
        return func(a * 2, b * 2)

    # Return wrapper
    return wrapper


# A decorated multiplication function
@double_args
def multiply(a: float, b: float) -> float:
    """Multiply two values

    Args:
        a (float): a float
        b (float): a float

    Returns:
        float: Product of A and B.

    Raises:
        ValueError: a or b are not numerical values
    """

    try:

        # Check if variables can be transformed to floats
        float(a)
        float(b)

    except:
        ValueError('Parameters a and b must be numerical.')

    return a * b


def timer(func):
    """A decorator that prints how long a function call took"""

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Start timer
        t_start = time.time()

        try:
            # Call decorated function
            return func(*args, **kwargs)

        finally:
            # Print to screen total run time of the function
            print(f'{func.__name__} took: {time.time() - t_start}')

    return wrapper


def memoize(func):
    """Save function results in memory"""

    # Cache
    cache = {}

    # Wrapper function
    def wrapper(*args, **kwargs):

        # Check if args and kwargs are new
        if (args, kwargs) not in cache:

            # Add result to cache
            cache[(args, kwargs)] = func(*args, **kwargs)

        # Return value
        return cache[(args, kwargs)]

    # Return wrapper
    return wrapper


def run_n_times(n: int) -> None:
    """Sleep N Seconds decorator

    Args:
        n (int): Seconds to sleep

    Returns:
        None
    """

    # Define decorator
    def decorator(func):

        # Define wrapper
        def wrapper(*args, **kwargs):

            # Run function n times
            for i in range(n):
                func(*args, **kwargs)

        # Return wrapper function
        return wrapper

    # Return built decorator
    return decorator


@timer
def sleep_n_seconds(n: int):
    """Sleep for n seconds

    Args:
        n (int): Number of seconds to sleep

    Returns:
        None
    """

    # Sleep
    time.sleep(n)


@memoize
def slow_product(a: float, b: float) -> float:

    # Sleep
    sleep_n_seconds(5)

    # Multiply
    return multiply(a, b)


@timeout(2)
def print_hello():
    time.sleep(1)
    print('Hello')


if __name__ == "__main__":
    print('timeout function')
    print_hello()
