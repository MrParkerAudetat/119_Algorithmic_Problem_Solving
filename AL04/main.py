"""Optional English-first starter for individual search contracts and correctness."""

from ticket_data import TICKETS
from search_support import id_key, category_key, matches, compare_values
from ticket_display import show_ticket, show_tickets, show_trace


# MONDAY - Separate the requested value from the traversal.

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
    """Return any matching position and interval visits on a key-ordered input."""
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
        elif comparison < 0:
            low = mid + 1
        else:
            high = mid - 1
    return None, trace


# TUESDAY CHECKPOINT - Verify the contract and preserve an independent submission.

def main():
    """Show completed searches with readable results and two small teaching traces."""
    id_ordered = sorted(TICKETS, key=id_key)
    
    
    print("Linear search for T403:")
    position, trace = linear_search(TICKETS, "T403")
    show_trace("Linear search trace for T403", trace)
    show_ticket(TICKETS[position] if position is not None else None)
    
    
    print("\nLinear search for T499:")
    position, trace = linear_search(TICKETS, "T499")
    show_trace("Linear search trace for T499", trace)
    show_ticket(TICKETS[position] if position is not None else None)
    
    
    print("\nBinary search for T403:")
    position, trace = binary_search(id_ordered, "T403")
    show_trace("Binary search trace for T403", trace)
    show_ticket(id_ordered[position] if position is not None else None)
    
    
    print("\nBinary search for absent T499 in ID order:")
    position, trace = binary_search(id_ordered, "T499")
    show_trace("binary search for T499", trace)
    show_ticket(id_ordered[position] if position is not None else None)

    print("\nDeliberately invalid: binary search on the original unsorted list:")
    linear_position, _ = linear_search(TICKETS, "T401")
    binary_position, _ = binary_search(TICKETS, "T401")
    print("Linear search finds T401:")
    show_ticket(TICKETS[linear_position] if linear_position is not None else None)
    print("Binary search misses it because the list is not ID-ordered:")
    show_ticket(TICKETS[binary_position] if binary_position is not None else None)

    category_ordered = sorted(TICKETS, key=category_key)
    print("\nBinary search for the repeated category 'account':")
    position, trace = binary_search(
        category_ordered, "account", key=category_key
    )
    show_trace("binary search for category account", trace)
    show_ticket(category_ordered[position] if position is not None else None)
    
if __name__ == "__main__":
    main()