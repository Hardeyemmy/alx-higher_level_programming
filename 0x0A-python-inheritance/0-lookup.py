#!/usr/bin/python3
"""
0-lookup: lookup()

"""

def lookup(obj):
    """
    Returns the list of the available attributes and methods.
    Args:
        obj (object): object.

    """
    return (dir(obj))
