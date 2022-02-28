# Date and time
from datetime import date
from datetime import timedelta
import json_extract, text_parser

# Get the current date
today = date.today()
print("Today is:", today)

"""
    Yesterday's date = 1
    2 days ago = 2
    3 days ago = 3
    ...
    30 days ago = 30
"""

# How many days ago?
days_ago = int(input("-> How many days ago? "))
json_extract.extract_json(days_ago)
text_parser.relocate()