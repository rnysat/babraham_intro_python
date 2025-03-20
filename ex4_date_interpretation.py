""" Assumptions about the date format:
- I have assumed that the first date is in the format year-month-date, because there is not a 16th month. 
- I have assumed the at the second date shared this format, because the exercise instructions state: "there are two different date formats", 
and the second date resembles the structure of the first rather than the final two dates.
- I have assumed that the second two dates follow the standard british date format of date-month-year. 
This assumption may not be correct, as both values in the first and second fields for both of the last two dates are
within a range (<= 12) that could relate to date or month.
"""

from datetime import datetime

date_set = """2018-04-16 10:25:29 AM MDT 
2018-01-05 12:05:00 PM CST 
01/01/2018 
12/02/2018 """

for line in date_set.split("\n"):
    try:
        dt = datetime.strptime(" ".join(line.strip().split()[0:-1]), "%Y-%m-%d %I:%M:%S %p")
    except:
        dt = datetime.strptime(line.strip(), "%d/%m/%Y")
    output = (dt.year, dt.month, dt.day)
    print(f"({output[0]}, {str(output[1]).zfill(2)}, {str(output[-1]).zfill(2)})")



