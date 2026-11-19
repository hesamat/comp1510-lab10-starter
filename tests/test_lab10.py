"""Tests for Lab 10 (loans.py).

One example test ships with the boundary part below: it shows the
with-block shape for a rejected row. The rest of the suite is yours.
Before you implement each function in loans.py, work here first. For
every function below: list its ordinary cases, the boundaries where
its answer changes, and the cases where two rules act at once as
comments, write one test per case (one logical assertion where the
case compares values), run the tests in PyCharm to watch them fail,
and only then implement or repair until your tests pass.
"""

import pytest

from loans import (
    longest_loan,
    shelves_by_course,
    longest_first,
    parse_row,
    numbered_listing,
    load_loans,
)


# ----------------------------------------------------------------------------
# The broken call: longest_loan(records)
# Returns the record with the largest days field. On a tie, the record
# that came first. While the call is broken, the tests cannot even run:
# write the ordinary-case test first, run it, and read the TypeError.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# The shelf map: shelves_by_course(courses, shelves)
# Returns the dictionary built by pairing the two lists position by
# position. The silent stop is behavior worth a test: when the shelf
# list is shorter, only the rows that have partners come back.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Longest first: longest_first(records)
# Returns the records with the most days first, and the list you handed
# over must still be in its original order when the call returns. Ties
# keep their original order.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# At the boundary: parse_row(row)
# Returns the record with real types: days and renewals as ints, the
# three text fields untouched. A row whose number is empty or is not a
# number raises ValueError. An example test follows. Write your tests
# below it.
# ----------------------------------------------------------------------------


def test_parse_row_rejects_an_empty_days_field():
    # Example test: the call must raise, so it goes inside a with
    # block. The message comes from int() itself, so there is no
    # match= wording to check here.
    row = {"date": "Nov 22", "title": "Ways of Seeing",
           "borrower": "Osei, Ama", "days": "", "renewals": "0"}
    with pytest.raises(ValueError):
        parse_row(row)


# ----------------------------------------------------------------------------
# The morning listing: numbered_listing(records)
# Takes the records longest_first ranked and returns one line per
# record, numbered from 1, such as "1. The Overstory: 27 days". An
# empty ranked list gives an empty listing.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Loading the file: load_loans(path)
# Reads a CSV of loans and returns the records that parsed, skipping a
# row whose number fails to convert. Point it at loans_messy.csv,
# which ships beside loans.py, and count what comes back.
# Write your tests below.
# ----------------------------------------------------------------------------
