"""Focused checks for AL05 sorting, views, and searches."""

from copy import deepcopy

from main import insertion_sort, build_views
from pipeline_support import select_open_tickets
from search_algorithms import linear_search, binary_search
from search_support import days_key
from ticket_data import TICKETS


def assignment_checks():
    """Check sorting contracts, pipeline views, and search results."""
    original_tickets = deepcopy(TICKETS)

    # The required small example: stable order, counts, and per-insertion trace.
    sample = [
        {"id": "T403", "days_open": 7},
        {"id": "T405", "days_open": 7},
        {"id": "T402", "days_open": 5},
        {"id": "T406", "days_open": 4},
    ]
    original = deepcopy(sample)

    ordered, comparisons, moves, trace = insertion_sort(sample, days_key)

    assert [record["id"] for record in ordered] == [
        "T406", "T402", "T403", "T405"
    ]
    assert comparisons == 6
    assert moves == 5
    assert trace == [
        ["T403", "T405", "T402", "T406"],
        ["T402", "T403", "T405", "T406"],
        ["T406", "T402", "T403", "T405"],
    ]
    assert sample == original
    assert ordered is not sample
    assert all(any(item is source for source in sample) for item in ordered)

    # Cover empty, singleton, ordered, reverse, and shuffled inputs with ties.
    cases = [
        [],
        [{"id": "T401", "days_open": 2}],
        [
            {"id": "T406", "days_open": 4},
            {"id": "T402", "days_open": 5},
            {"id": "T403", "days_open": 7},
            {"id": "T405", "days_open": 7},
        ],
        [
            {"id": "T405", "days_open": 7},
            {"id": "T403", "days_open": 7},
            {"id": "T402", "days_open": 5},
            {"id": "T406", "days_open": 4},
        ],
        [
            {"id": "T402", "days_open": 5},
            {"id": "T405", "days_open": 7},
            {"id": "T406", "days_open": 4},
            {"id": "T403", "days_open": 7},
        ],
    ]
    for records in cases:
        original_records = deepcopy(records)
        result, _, _, _ = insertion_sort(records, days_key)

        assert records == original_records
        assert result is not records
        assert [record["id"] for record in result] == [
            record["id"] for record in sorted(records, key=days_key)
        ]

    # Check eligibility boundaries and completed-ticket exclusion.
    selected_at_4 = select_open_tickets(TICKETS, minimum_days=4)
    assert [record["id"] for record in selected_at_4] == [
        "T403", "T405", "T402", "T406"
    ]
    assert "T406" in [record["id"] for record in selected_at_4]
    assert "T404" not in [record["id"] for record in selected_at_4]

    selected, display_view, search_view = build_views(TICKETS, minimum_days=4)
    assert [record["id"] for record in display_view] == [
        "T406", "T402", "T403", "T405"
    ]
    assert [record["id"] for record in search_view] == [
        "T402", "T403", "T405", "T406"
    ]
    assert selected is not TICKETS
    assert display_view is not selected
    assert search_view is not selected
    assert display_view is not search_view
    assert all(
        any(item is record for record in selected)
        for item in display_view + search_view
    )

    # Resolve each search position in the same list that was searched.
    linear_position, _ = linear_search(selected, "T403")
    binary_position, _ = binary_search(search_view, "T403")
    assert selected[linear_position]["id"] == "T403"
    assert search_view[binary_position]["id"] == "T403"

    assert linear_search(selected, "T499")[0] is None
    assert binary_search(search_view, "T499")[0] is None

    # Deliberately invalid use: display_view is not ID-ordered.
    assert binary_search(display_view, "T406")[0] is None

    selected_at_7, display_at_7, search_at_7 = build_views(
        TICKETS, minimum_days=7
    )
    assert [record["id"] for record in selected_at_7] == ["T403", "T405"]
    assert [record["id"] for record in display_at_7] == ["T403", "T405"]
    assert [record["id"] for record in search_at_7] == ["T403", "T405"]

    linear_position_7, _ = linear_search(selected_at_7, "T403")
    binary_position_7, _ = binary_search(search_at_7, "T403")
    assert selected_at_7[linear_position_7]["id"] == "T403"
    assert search_at_7[binary_position_7]["id"] == "T403"
    assert linear_search(selected_at_7, "T406")[0] is None
    assert binary_search(search_at_7, "T406")[0] is None
    assert binary_search(search_at_7, "T499")[0] is None

    selected_at_8, display_at_8, search_at_8 = build_views(
        TICKETS, minimum_days=8
    )
    assert selected_at_8 == []
    assert display_at_8 == []
    assert search_at_8 == []
    assert TICKETS == original_tickets


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL05 checks passed.")