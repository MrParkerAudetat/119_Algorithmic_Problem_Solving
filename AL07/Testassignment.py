"""Optional AL07 test starting point; expand it with your own expectations."""

from AL07.main import greedy_change, calculate_cached
from AL07.investigation_support import exhaustive_change, cached_fibonacci, uncached_fibonacci


def test_tuesday():
    """Check greedy choices, edge cases, and input validation."""
    assert greedy_change([1, 4, 6], 8) == [6, 1, 1]
    assert exhaustive_change([1, 4, 6], 8) == [4, 4]
    assert greedy_change([4, 6], 8) is None
    assert exhaustive_change([4, 6], 8) == [4, 4]
    assert greedy_change([4, 6], 7) is None
    assert exhaustive_change([4, 6], 7) is None
    assert greedy_change([1, 5, 10], 12) == [10, 1, 1]
    assert greedy_change([1, 4, 6], 0) == []
    assert greedy_change([6, 1, 4, 1], 8) == [6, 1, 1]

    for denominations, target in [([1, 4], -1), ([1, 4], 13), ([1, 0], 5), ([], 5)]:
        try:
            greedy_change(denominations, target)
        except ValueError:
            pass
        else:
            assert False, f"Expected ValueError for {denominations=}, {target=}"


def test_thursday():
    """Check saved answers and bounded counts against a hand-checkable input."""
    # result, calls, hits, cache = cached_fibonacci(5, calculate_cached)
    # assert result == 5
    # assert calls == 9
    # assert hits == 3
    # assert len(cache) == 6
    # assert cache == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
    #
    # for n, expected in [(0, 0), (1, 1), (8, 21)]:
    #     result, calls, hits, cache = cached_fibonacci(n, calculate_cached)
    #     assert result == expected
    #     assert set(cache) == set(range(n + 1))
    #     assert cache[n] == expected
    #
    # first_run = cached_fibonacci(5, calculate_cached)
    # second_run = cached_fibonacci(5, calculate_cached)
    # assert first_run == second_run
    #
    # for n in (-1, 21):
    #     try:
    #         cached_fibonacci(n, calculate_cached)
    #     except ValueError:
    #         pass
    #     else:
    #         assert False, f"Expected ValueError for n={n}"


if __name__ == "__main__":
    test_tuesday()
    # THURSDAY: uncomment the following call when implementing the cache.
    # test_thursday()
    print("Tuesday starting check passed; expand the tests before submitting.")