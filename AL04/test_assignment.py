from copy import deepcopy

from main import linear_search, binary_search
from ticket_data import TICKETS
from search_support import id_key, category_key


def assignment_checks():
    original = deepcopy(TICKETS)
    id_ordered = sorted(TICKETS, key=id_key)

    # Found result and trace: position 0 is a valid result.
    position, trace = linear_search(TICKETS, "T403")
    assert position == 0
    assert trace == [(0, "T403")]

    position, trace = binary_search(id_ordered, "T403")
    assert position == 2
    assert trace == [(0, 5, 2, "T403")]

    # Empty and singleton lists.
    for search in (linear_search, binary_search):
        assert search([], "T403") == (None, [])
        assert search([TICKETS[0]], "T403")[0] == 0
        assert search([TICKETS[0]], "T499")[0] is None

    # First and last IDs, and missing IDs below, between, and above.
    for search in (linear_search, binary_search):
        assert search(id_ordered, "T401")[0] == 0
        assert search(id_ordered, "T406")[0] == 5
        for missing in ("T400", "T4015", "T499"):
            assert search(id_ordered, missing)[0] is None

    # Repeated categories: either matching ticket is acceptable.
    category_ordered = sorted(TICKETS, key=category_key)
    for search in (linear_search, binary_search):
        position, _ = search(category_ordered, "account", key=category_key)
        assert position is not None
        assert category_ordered[position]["category"] == "account"

    # Deliberately invalid binary search on unsorted data.
    assert linear_search(TICKETS, "T401")[0] == 1
    assert binary_search(TICKETS, "T401")[0] is None

    # Searches must not change the original tickets.
    assert TICKETS == original


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL04 checks passed.")
