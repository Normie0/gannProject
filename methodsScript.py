import streamlit as st
from datetime import datetime, timedelta, date
import math
from countWeekends import prefix_weekend_counts
from countHolidays import count_holidays


HOLIDAYS_2025 = [
    "26 February 2025",  # Mahashivratri
    "14 March 2025",     # Holi
    "31 March 2025",     # Id-Ul-Fitr (Ramzan Id)
    "10 April 2025",     # Shri Mahavir Jayanti
    "14 April 2025",     # Dr. Baba Saheb Ambedkar Jayanti
    "18 April 2025",     # Good Friday
    "01 May 2025",       # Maharashtra Day
    "15 August 2025",    # Independence Day
    "27 August 2025",    # Ganesh Chaturthi
    "02 October 2025",   # Mahatma Gandhi Jayanti/Dussehra
    "21 October 2025",   # Diwali * Laxmi Pujan
    "22 October 2025",   # Diwali Balipratipada
    "05 November 2025",  # Prakash Gurpurb Sri Guru Nanak Dev
    "25 December 2025"   # Christmas
]

HOLIDAYS_2024 = [
    "26 January 2024",   # Republic Day
    "08 March 2024",     # Mahashivratri
    "25 March 2024",     # Holi
    "29 March 2024",     # Good Friday
    "11 April 2024",     # Id-Ul-Fitr (Ramzan Id)
    "17 April 2024",     # Ram Navami
    "01 May 2024",       # Maharashtra Day
    "20 May 2024",       # General Elections (Lok Sabha)
    "17 June 2024",      # Bakri Id
    "17 July 2024",      # Muharram
    "15 August 2024",    # Independence Day
    "02 October 2024",   # Mahatma Gandhi Jayanti
    "01 November 2024",  # Diwali * Laxmi Pujan
    "15 November 2024",  # Guru Nanak Jayanti
    "20 November 2024",  # Assembly General Elections
    "25 December 2024"   # Christmas
]

HOLIDAYS_2023 = [
    "26 January 2023",   # Republic Day
    "07 March 2023",     # Holi
    "30 March 2023",     # Ram Navami
    "04 April 2023",     # Mahavir Jayanti
    "07 April 2023",     # Good Friday
    "14 April 2023",     # Dr. Baba Saheb Ambedkar Jayanti
    "01 May 2023",       # Maharashtra Day
    "28 June 2023",      # Bakri Eid
    "15 August 2023",    # Independence Day
    "19 September 2023", # Ganesh Chaturthi
    "02 October 2023",   # Mahatma Gandhi Jayanti
    "24 October 2023",   # Dussehra
    "14 November 2023",  # Diwali-Balipratipada
    "27 November 2023",  # Guru Nanak Jayanti
    "25 December 2023"   # Christmas
]


def get_less_val(value):
    while value / 10 > 10:
        value /= 10
    return value


holidays = set(HOLIDAYS_2023 + HOLIDAYS_2024 + HOLIDAYS_2025)

def topSquaring(stock_price):
    price_greater_than_ten = get_less_val(stock_price)
    count = 2

    temp = price_greater_than_ten
    start_date = datetime.strptime("15:9:2023", "%d:%m:%Y")

    calendar_dates = [start_date.strftime("%d %B %Y")]  

    for _ in range(8):  
        temp = price_greater_than_ten * count
        temp = math.ceil(temp) if math.ceil(temp) - temp < 0.5 else math.floor(temp)

        count += 1
        
        last_date = datetime.strptime(calendar_dates[-1], "%d %B %Y")
        new_date = last_date + timedelta(days=temp)
        
        # Prevent overflow
        if new_date.year > 2100:
            print("Stopping early to prevent overflow.")
            break
        
        calendar_dates.append(new_date.strftime("%d %B %Y"))  

    return calendar_dates



def bottomSquaring(stock_price):
    price_greater_than_ten = get_less_val(stock_price)
    count = 2

    temp = price_greater_than_ten
    start_date = datetime.strptime("20:3:2023", "%d:%m:%Y")

    calendar_dates = [start_date.strftime("%d %B %Y")]  

    for _ in range(8):  
        temp = price_greater_than_ten * count
        # Apply rounding rule
        temp = math.ceil(temp) if math.ceil(temp) - temp < 0.5 else math.floor(temp)

        count += 1
        
        last_date = datetime.strptime(calendar_dates[-1], "%d %B %Y")
        new_date = last_date + timedelta(days=temp)

        # Prevent overflow
        if new_date.year > 2100:
            print("Stopping early to prevent overflow.")
            break
        
        calendar_dates.append(new_date.strftime("%d %B %Y"))  

    return calendar_dates


def rangeSquaring(stock_price):
    range_price = math.sqrt(stock_price)
    count = 2
    temp = range_price
    start_date = datetime.strptime("3:3:2025", "%d:%m:%Y")

    calendar_dates = [start_date.strftime("%d %B %Y")]  

    for _ in range(8):  
        temp = range_price * count
        # Apply rounding rule
        temp = math.ceil(temp) if math.ceil(temp) - temp < 0.5 else math.floor(temp)

        count += 1

        last_date = start_date
        new_date = last_date + timedelta(days=temp)
        last_date_obj = last_date.date()
        new_date_obj = new_date.date()
        new_date_holidays = count_holidays(last_date_obj, new_date_obj) + sum(prefix_weekend_counts[new_date_obj]) - sum(prefix_weekend_counts[last_date_obj])
        while new_date_holidays > 0:
            new_date += timedelta(days=new_date_holidays)
            last_date_obj = new_date_obj
            new_date_obj = new_date.date()
            new_date_holidays = count_holidays(last_date_obj + timedelta(days=1), new_date_obj) + sum(prefix_weekend_counts[new_date_obj]) - sum(prefix_weekend_counts[last_date_obj])
        
        calendar_dates.append(new_date.strftime("%d %B %Y"))  

    return calendar_dates


def thirty_sixty_ninety(dates):

    start_date = datetime.strptime("20:3:2023", "%d:%m:%Y")

    calendar_dates = [start_date.strftime("%d %B %Y")]

    angles = [30, 60, 90, 120, 180, 240, 270, 360]  

    for angle in angles:  
        temp = angle

        last_date = start_date
        new_date = last_date + timedelta(days=temp)

        while new_date.weekday() in {5, 6} or new_date.strftime("%d %B %Y") in holidays:
            new_date += timedelta(days=1)
        
        # Prevent overflow
        if new_date.year > 2100:
            print("Stopping early to prevent overflow.")
            break
        
        calendar_dates.append(new_date.strftime("%d %B %Y"))  

    return calendar_dates


topSquaringdates = (topSquaring(20222.45))
bottomSquaringdates = (bottomSquaring(16828.35))
rangeSquaringdates = (rangeSquaring(9))
degreesDates = (thirty_sixty_ninety(100))

print(topSquaringdates)
print(bottomSquaringdates)
print(rangeSquaringdates)
print(degreesDates)

def compareArr(arr1, arr2):
    # Convert string dates to datetime.date objects before looping
    arr1_dates = [datetime.strptime(d, "%d %B %Y").date() for d in arr1]
    arr2_dates = [datetime.strptime(d, "%d %B %Y").date() for d in arr2]

    for d1 in arr1_dates:
        for d2 in arr2_dates:
            if abs((d1 - d2).days) <= 7:  # Check if within 7 days
                print(d1.strftime("%d %B %Y"), "and", d2.strftime("%d %B %Y"), "are within 7 days")

print("Top squaring vs Bottom squaring")
compareArr(topSquaringdates[1:], bottomSquaringdates[1:])
print("Top squaring vs Range squaring")
compareArr(topSquaringdates[1:], rangeSquaringdates[1:])
print("Top squaring vs degrees")
compareArr(topSquaringdates[1:], degreesDates[1:])
print("Bottom squaring vs Range squaring")
compareArr(bottomSquaringdates[1:], rangeSquaringdates[1:])
print("Bottom squaring vs degrees")
compareArr(bottomSquaringdates[1:], degreesDates[1:])
print("Range squaring vs degrees")
compareArr(rangeSquaringdates[1:], degreesDates[1:])


# practice()