"""Optional English-first starter; one recognition-level app across three days."""

from Catalog_Data import BOOKS, validate_book_ids

# MONDAY - Implement equivalent lookups after Monday's instruction.


def find_Book(records, book_id):
    """Return the first matching book, or None when absent."""
    # Look at one record at a time, in its original order.
    # Compare its ID with the requested ID.
    # Return the record immediately when it matches.
    # Return None if you reach the end without a match.
    # Do not change the input records.
    for book in records:
        if book["id"] == book_id:
            return book
    return None


def build_index(records):
    """Map each previously validated catalog ID to its book record."""
    # Begin with an empty dictionary.
    # Visit each book once; use its ID as the key and its record as the value.
    # Return the completed index without changing the original records.
    # Use the supplied ID precheck before building; do not resolve duplicates.
    index = {}
    for book in records:
        index[book["id"]] = book
    return index


def indexed_lookup(index, book_id):
    """Return the indexed book or None when the catalog ID is absent."""
    # Check whether the requested ID is a dictionary key.
    # Return the associated book when present; otherwise return None.
    # Do not rebuild the dictionary here.
    if book_id in index:
        return index[book_id]
    return None


def record_builder(size):
    """Build a catalog with the requested number of records."""
    return [{"id": book_id} for book_id in range(size)]


def find_Book(records, book_id):
    """Return the scan result and the number of ID comparisons."""
    comparisons = 0
    for book in records:
        if book["id"] == book_id:
            return book
    return None


def main():
    """Show the examples for the lookup functions you have completed."""
    # Begin a fresh shared project; do not choose either partner's AL01 code.
    # Use the supplied BOOKS list and validate its catalog IDs.
    # Build an index once; look up every ID supplied by the catalog.
    # Compare both lookup answers and show ID, title, author, or a not-found message.
    # Replace this message when the Monday functions are ready.
    validate_book_ids(BOOKS)
    index = build_index(BOOKS)

    for book in BOOKS:
        book_id = book["id"]
        scan_result = find_Book(BOOKS, book_id)
        index_result = indexed_lookup(index, book_id)
        print("Looking up", book_id)
        print("  Same answer from both lookups:", scan_result == index_result)
        if scan_result is None:
            print("  Not found.")
        else:
            print("  ID:", scan_result["id"])
            print("  Title:", scan_result["title"])
            print("  Author:", scan_result["author"])

    print("\nWhen every query misses:")
    # Two fixed queries stay O(n); n queries become O(n^2).
    for size in (4, 8):
        scan_result = find_Book(record_builder(size), -1)
        print(
            f"n={size}: 2 fixed queries -> {2}; n queries -> {size * 1}"
        )
    print("Fixed q: O(n). If q grows with n: O(n^2).")

if __name__ == "__main__":
    main()
