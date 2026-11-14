"""Optional English-first starter for stable sorting and a key-correct pipeline."""
from search_algorithms import linear_search, binary_search
from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets
from ticket_display import show_ticket, show_tickets


# TUESDAY - Stable ordering, with counts for one tiny example.

def insertion_sort(records, key):
    """Return a stable shallow ordered list, comparison/shift counts, and ID trace."""
    ordered = list(records)
    comparisons = 0
    moves = 0
    trace = []

    for i in range(1, len(ordered)):
        item = ordered[i]
        item_key = key(item)
        j = i - 1

        while j >= 0:
            comparisons += 1
            if key(ordered[j]) > item_key:
                ordered[j + 1] = ordered[j]
                moves += 1
                j -= 1
            else:
                break

        ordered[j + 1] = item
        trace.append([record["id"] for record in ordered])

    return ordered, comparisons, moves, trace

# THURSDAY - Compose existing interfaces; rebuild after the eligibility change.

def build_views(records, minimum_days=4):
    """Return selected, age-display, and ID-search lists sharing eligible records."""
    selected = select_open_tickets(records, minimum_days)

    display_view, _, _, _ = insertion_sort(selected, days_key)
    search_view = sorted(selected, key=id_key)

    return selected, display_view, search_view


def main():
    """Demonstrate the sort, pipeline views, searches, and threshold change."""
    selected = select_open_tickets(TICKETS, minimum_days=4)
    display_view, comparisons, moves, trace = insertion_sort(selected, days_key)

    show_tickets("Selected tickets at minimum_days=4", selected)
    show_tickets("Display view: days open ascending", display_view)

    print("\nTeaching evidence (not timings):")
    print(f"Key comparisons: {comparisons}; right-shifts: {moves}")
    for step, ids in enumerate(trace, start=1):
        print(f"After insertion {step}: {ids}")

    python_sorted = sorted(selected, key=days_key)
    print(
        "\nMatches Python sorted:",
        [record["id"] for record in display_view]
        == [record["id"] for record in python_sorted],
    )

    selected, display_view, search_view = build_views(TICKETS, minimum_days=4)
    show_tickets("ID-ordered search view", search_view)

    linear_position, _ = linear_search(selected, "T403")
    binary_position, _ = binary_search(search_view, "T403")
    print("\nT403 found by linear search:")
    show_ticket(selected[linear_position] if linear_position is not None else None)
    print("T403 found by binary search:")
    show_ticket(search_view[binary_position] if binary_position is not None else None)

    print("\nSearch for absent T499:")
    missing_position, _ = binary_search(search_view, "T499")
    show_ticket(
        search_view[missing_position]
        if missing_position is not None
        else None
    )

    print("\nDeliberately invalid: binary search on the age-ordered view:")
    wrong_position, _ = binary_search(display_view, "T406")
    show_ticket(
        display_view[wrong_position]
        if wrong_position is not None
        else None
    )
    print("This lookup used the wrong ordering; ID binary search requires ID order.")

    selected_7, display_7, search_7 = build_views(TICKETS, minimum_days=7)
    show_tickets("Selection after raising the threshold to 7", selected_7)
    print("Display IDs:", [record["id"] for record in display_7])
    print("Search IDs:", [record["id"] for record in search_7])

    linear_position_7, _ = linear_search(selected_7, "T403")
    binary_position_7, _ = binary_search(search_7, "T403")
    print("\nAfter the change, T403 is still found:")
    show_ticket(
        selected_7[linear_position_7]
        if linear_position_7 is not None
        else None
    )
    show_ticket(
        search_7[binary_position_7]
        if binary_position_7 is not None
        else None
    )

    print("T406 no longer qualifies at minimum_days=7:")
    excluded_position, _ = binary_search(search_7, "T406")
    show_ticket(
        search_7[excluded_position]
        if excluded_position is not None
        else None
    )
    print("Absent T499 remains missing:")
    missing_position_7, _ = binary_search(search_7, "T499")
    show_ticket(
        search_7[missing_position_7]
        if missing_position_7 is not None
        else None
    )

    selected_8, display_8, search_8 = build_views(TICKETS, minimum_days=8)
    show_tickets("Selection at minimum_days=8", selected_8)
    print("Display IDs:", [record["id"] for record in display_8])
    print("Search IDs:", [record["id"] for record in search_8])


if __name__ == "__main__":
    main()
