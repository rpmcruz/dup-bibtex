# dup-bibtex
Check for duplicates in your bibtex file. It extracts all entry/title pairs and uses [difflib.SequenceMatcher](https://docs.python.org/3/library/difflib.html) to compare them.

**Usage:** `python dups.py file.bib`

(No need to install anything. Only packages that come with Python are used by the script.)
