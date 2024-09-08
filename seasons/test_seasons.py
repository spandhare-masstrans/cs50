import pytest
from datetime import date
from seasons import calculate_minutes

def test_calculate_minutes():
    ## assert calculate_minutes("1999-01-01", present_date) == 13466880
    ## assert calculate_minutes("2019-05-08", present_date) == 2679840
    assert calculate_minutes("2023-09-08") == 527040

# Add more tests for edge cases and invalid formats
