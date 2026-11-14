"""AL04 search functions copied locally for AL05."""

from search_support import id_key, matches, compare_values


def linear_search(records, target, key=id_key):
    """Return the first matching position and visits, or None and visits."""
    trace = []
    for position, record in enumerate(records):
        value = key(record)
        trace.append((position, value))
        if matches(value, target):
            return position, trace
    return None, trace


def binary_search(records, target, key=id_key):
    """Return any matching position and interval visits on key-ordered input."""
    trace = []
    low = 0
    high = len(records) - 1

    while low <= high:
        mid = (low + high) // 2
        value = key(records[mid])
        trace.append((low, high, mid, value))

        comparison = compare_values(value, target)
        if matches(value, target):
            return mid, trace
        if comparison < 0:
            low = mid + 1
        else:
            high = mid - 1

    return None, trace