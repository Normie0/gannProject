from datetime import date, timedelta, datetime

# List of holidays from 2024 and 2025
HOLIDAYS = [
    "26 February 2025", "14 March 2025", "31 March 2025", "10 April 2025",
    "14 April 2025", "18 April 2025", "01 May 2025", "15 August 2025",
    "27 August 2025", "02 October 2025", "21 October 2025", "22 October 2025",
    "05 November 2025", "25 December 2025",
    "26 January 2024", "08 March 2024", "25 March 2024", "29 March 2024",
    "11 April 2024", "17 April 2024", "01 May 2024", "20 May 2024",
    "17 June 2024", "17 July 2024", "15 August 2024", "02 October 2024",
    "01 November 2024", "15 November 2024", "20 November 2024", "25 December 2024",
    "26 January 2023", "07 March 2023", "30 March 2023", "04 April 2023",
    "07 April 2023", "14 April 2023", "01 May 2023", "28 June 2023",
    "15 August 2023", "19 September 2023", "02 October 2023", "24 October 2023",
    "14 November 2023", "27 November 2023", "25 December 2023"
]

# Convert holiday strings into date objects
holiday_dates = {datetime.strptime(h, "%d %B %Y").date() for h in HOLIDAYS if datetime.strptime(h, "%d %B %Y").date().weekday() not in {5, 6}}

def count_holidays(start_date, end_date):
    """Counts the number of holidays between start_date and end_date."""
    return sum(1 for holiday in holiday_dates if start_date <= holiday <= end_date)

