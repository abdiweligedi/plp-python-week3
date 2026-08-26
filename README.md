# PLP Python Week 3 — Name Splitter, Bug Hunt & First Decisions

## Files

- `name_greeter.py` — Splits a user's full name and greets them using their first name.
- `bug_hunt.py` — Finds and fixes three bugs while practicing Python error messages and debugging.
- `ticket_checker.py` — Checks whether a user is an adult and displays the correct ticket price.
- `screenshots/` — Contains screenshots of the programs running.

## Bug Hunt Reflection

The bug that took longest to find was the age calculation bug because the age entered by the user was stored as a string. The error message helped me understand that Python could not add an integer to a string. I fixed the problem by converting the age to an integer using `int()`.