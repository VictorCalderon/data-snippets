"""Module provides context manager functions
"""
import contextlib
import time

# Simple function based context manager
@contextlib.contextmanager
def timer():
    """Time execution of a content block

    Yields:
        None
    """

    # Open error handling block
    try:

        # Get starting time
        start = time.time()

        # Run code in context
        yield

    finally:

        # End time
        end = time.time()

        # Display elapsed time
        print(end - start)


if __name__ == "__main__":

    # Example of timer working
    with timer():
        s = 1
        time.sleep(s)
        print(f'This should take {s} seconds.')
