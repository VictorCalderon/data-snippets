"""Module containing data for docstring creation
"""


# Simple function with a docstring

def count_substring(context: str, substring: str) -> int:
    """Count the number of times a substring appears in context.

    Args:
        context (str): Context from which to grab information.
        substring (str): Substring to be counted.

    Returns:
        int

    Raises:
        ValueError: context and substring must both be of type <str>.
        IndexError: context must be greater than substring.
    """

    # Check both parameter's datatype
    if not (isinstance(context, str) and isinstance(substring, str)):
        raise ValueError('Both context and substring must be <str>')

    # Check if context has more characters than substring
    if (len(context) > len(substring)):
        raise IndexError(
            'The length of context must be greater than substring'
        )

    # Count
    return context.count(substring)
