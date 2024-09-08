from datetime import datetime
from datetime import date
import time
import inflect
import sys

p = inflect.engine()

def convert_to_words(n):
    # Convert number to words without commas and 'and'
    words = p.number_to_words(n).replace(' and','').capitalize()
    words = words + " minutes"
    return words

def calculate_minutes(birthdate_str):
    present_date = date.today()
    #present_date = date(2000, 1, 1)

    try:
        year, month, day = map(int, birthdate_str.split("-"))
        birthdate = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    present_date_str = present_date.strftime('%Y-%m-%d')
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(birthdate_str, fmt)
    d2 = datetime.strptime(present_date_str, fmt)

    # Convert to Unix timestamp
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())

    if (d2_ts > d1_ts):
    	minutes = (d2_ts - d1_ts)/60
    else:
        minutes = (d1_ts - d2_ts)/60
    return int(minutes)

def main():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    minutes = calculate_minutes(birthdate_str)
    words = convert_to_words(minutes)
    print(words)


if __name__ == "__main__":
    main()
