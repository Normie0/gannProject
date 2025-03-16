import streamlit as st
import pandas as pd
from datetime import datetime, timedelta, date
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import altair as alt

# Use your existing imports - these would come from your original files
from countWeekends import prefix_weekend_counts
from countHolidays import count_holidays

# Define your holiday lists
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

holidays = set(HOLIDAYS_2023 + HOLIDAYS_2024 + HOLIDAYS_2025)

# Use your existing functions as they are
def get_less_val(value):
    while value / 10 > 10:
        value /= 10
    return value

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
        temp = math.ceil(temp) if math.ceil(temp) - temp < 0.5 else math.floor(temp)
        
        count += 1
        
        last_date = datetime.strptime(calendar_dates[-1], "%d %B %Y")
        new_date = last_date + timedelta(days=temp)
        
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
        temp = math.ceil(temp) if math.ceil(temp) - temp < 0.5 else math.floor(temp)
        
        count += 1
        
        last_date = datetime.strptime(calendar_dates[-1], "%d %B %Y")
        last_date_obj = last_date.date()
        new_date = last_date + timedelta(days=temp)
        new_date_obj = new_date.date()
        
        new_date_holidays = count_holidays(last_date_obj, new_date_obj) + sum(prefix_weekend_counts[new_date_obj]) - sum(prefix_weekend_counts[last_date_obj])
        
        while new_date_holidays > 0:
            new_date += timedelta(days=new_date_holidays)
            last_date_obj = new_date_obj
            new_date_obj = new_date.date()
            new_date_holidays = count_holidays(last_date_obj + timedelta(days=1), new_date_obj) + sum(prefix_weekend_counts[new_date_obj]) - sum(prefix_weekend_counts[last_date_obj])
        
        calendar_dates.append(new_date.strftime("%d %B %Y"))
    
    return calendar_dates

def thirty_sixty_ninety():
    start_date = datetime.strptime("20:3:2023", "%d:%m:%Y")
    
    calendar_dates = [start_date.strftime("%d %B %Y")]
    
    angles = [30, 60, 90, 120, 180, 240, 270, 360]
    
    for angle in angles:
        temp = angle
        
        last_date = datetime.strptime(calendar_dates[-1], "%d %B %Y")
        new_date = last_date + timedelta(days=temp)
        
        while new_date.weekday() in {5, 6} or new_date.strftime("%d %B %Y") in holidays:
            new_date += timedelta(days=1)
        
        if new_date.year > 2100:
            print("Stopping early to prevent overflow.")
            break
        
        calendar_dates.append(new_date.strftime("%d %B %Y"))
    
    return calendar_dates

def compareArr(arr1, arr2):
    arr1_dates = [datetime.strptime(d, "%d %B %Y").date() for d in arr1]
    arr2_dates = [datetime.strptime(d, "%d %B %Y").date() for d in arr2]
    
    close_dates = []
    for d1 in arr1_dates:
        for d2 in arr2_dates:
            if abs((d1 - d2).days) <= 7:
                close_dates.append((d1.strftime("%d %B %Y"), d2.strftime("%d %B %Y"), abs((d1 - d2).days)))
    
    return close_dates

# Streamlit app
st.set_page_config(page_title="Date Calculator", layout="wide")

st.title("Market Date Calculator")
st.markdown("### Calculate and visualize significant market dates using different methods")

# Input section
st.sidebar.header("Input Parameters")

top_price = st.sidebar.number_input("Top Squaring Price", value=20222.45, format="%.2f")
bottom_price = st.sidebar.number_input("Bottom Squaring Price", value=16828.35, format="%.2f")
range_price = st.sidebar.number_input("Range Squaring Value", value=9, format="%.2f")

top_start_date = st.sidebar.date_input("Top Squaring Start Date", date(2023, 9, 15))
bottom_start_date = st.sidebar.date_input("Bottom Squaring Start Date", date(2023, 3, 20))
range_start_date = st.sidebar.date_input("Range Squaring Start Date", date(2025, 3, 3))
degrees_start_date = st.sidebar.date_input("30-60-90 Start Date", date(2023, 3, 20))

# Calculate dates
top_dates = topSquaring(top_price)
bottom_dates = bottomSquaring(bottom_price)
range_dates = rangeSquaring(range_price)
degrees_dates = thirty_sixty_ninety()

# Create tabs for different views
tab1, tab2, tab3 = st.tabs(["Date Tables", "Timeline Visualization", "Close Date Matches"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Squaring Dates")
        df_top = pd.DataFrame({
            "Index": range(len(top_dates)),
            "Date": top_dates
        })
        st.dataframe(df_top, hide_index=True)
        
        st.subheader("Range Squaring Dates")
        df_range = pd.DataFrame({
            "Index": range(len(range_dates)),
            "Date": range_dates
        })
        st.dataframe(df_range, hide_index=True)
    
    with col2:
        st.subheader("Bottom Squaring Dates")
        df_bottom = pd.DataFrame({
            "Index": range(len(bottom_dates)),
            "Date": bottom_dates
        })
        st.dataframe(df_bottom, hide_index=True)
        
        st.subheader("30-60-90 Degree Dates")
        df_degrees = pd.DataFrame({
            "Index": range(len(degrees_dates)),
            "Date": degrees_dates
        })
        st.dataframe(df_degrees, hide_index=True)

with tab2:
    st.subheader("Timeline Visualization")
    
    # Convert dates to datetime objects for visualization
    chart_data = []
    
    for i, date_str in enumerate(top_dates):
        dt = datetime.strptime(date_str, "%d %B %Y")
        chart_data.append({
            "Date": dt.strftime("%Y-%m-%d"),  # Format date as string for Altair
            "Method": "Top Squaring",
            "DisplayDate": date_str,
            "Index": i
        })
    
    for i, date_str in enumerate(bottom_dates):
        dt = datetime.strptime(date_str, "%d %B %Y")
        chart_data.append({
            "Date": dt.strftime("%Y-%m-%d"),
            "Method": "Bottom Squaring",
            "DisplayDate": date_str,
            "Index": i
        })
    
    for i, date_str in enumerate(range_dates):
        dt = datetime.strptime(date_str, "%d %B %Y")
        chart_data.append({
            "Date": dt.strftime("%Y-%m-%d"),
            "Method": "Range Squaring",
            "DisplayDate": date_str,
            "Index": i
        })
    
    for i, date_str in enumerate(degrees_dates):
        dt = datetime.strptime(date_str, "%d %B %Y")
        chart_data.append({
            "Date": dt.strftime("%Y-%m-%d"),
            "Method": "Degrees",
            "DisplayDate": date_str,
            "Index": i
        })
    
    # Create a DataFrame for the chart
    df_chart = pd.DataFrame(chart_data)
    
    # Create an Altair chart
    chart = alt.Chart(df_chart).mark_circle(size=100).encode(
        x='Date:T',
        y='Method:N',
        color='Method:N',
        tooltip=['Method', 'DisplayDate', 'Index']
    ).properties(
        width=800,
        height=300
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)
    
    # Create a Matplotlib figure for more detailed control
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = {
        "Top Squaring": "#1f77b4",
        "Bottom Squaring": "#ff7f0e",
        "Range Squaring": "#2ca02c", 
        "Degrees": "#d62728"
    }
    
    for i, method in enumerate(["Top Squaring", "Bottom Squaring", "Range Squaring", "Degrees"]):
        method_df = df_chart[df_chart['Method'] == method]
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in method_df['Date']]
        y_positions = [i] * len(dates)
        ax.scatter(dates, y_positions, label=method, color=colors[method], s=100)
    
    ax.set_yticks(range(4))
    ax.set_yticklabels(["Top Squaring", "Bottom Squaring", "Range Squaring", "Degrees"])
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.xticks(rotation=45)
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    st.pyplot(fig)


with tab3:
    st.subheader("Close Date Matches (Within 7 Days)")
    
    # Compare dates between different methods
    comparisons = [
        ("Top Squaring vs Bottom Squaring", compareArr(top_dates[1:], bottom_dates[1:])),
        ("Top Squaring vs Range Squaring", compareArr(top_dates[1:], range_dates[1:])),
        ("Top Squaring vs Degrees", compareArr(top_dates[1:], degrees_dates[1:])),
        ("Bottom Squaring vs Range Squaring", compareArr(bottom_dates[1:], range_dates[1:])),
        ("Bottom Squaring vs Degrees", compareArr(bottom_dates[1:], degrees_dates[1:])),
        ("Range Squaring vs Degrees", compareArr(range_dates[1:], degrees_dates[1:]))
    ]
    
    # Create a DataFrame for all close date matches
    close_matches_data = []
    for comparison_name, matches in comparisons:
        for date1, date2, days_apart in matches:
            close_matches_data.append({
                "Comparison": comparison_name,
                "Date 1": date1,
                "Date 2": date2,
                "Days Apart": days_apart
            })
    
    if close_matches_data:
        df_close_matches = pd.DataFrame(close_matches_data)
        st.dataframe(df_close_matches, hide_index=True, use_container_width=True)
        
        # Count of close matches by comparison
        st.subheader("Count of Close Date Matches by Comparison")
        comparison_counts = df_close_matches["Comparison"].value_counts().reset_index()
        comparison_counts.columns = ["Comparison", "Count"]
        
        # Create a bar chart of the counts
        chart = alt.Chart(comparison_counts).mark_bar().encode(
            x=alt.X('Comparison:N', title='Comparison', sort='-y'),
            y=alt.Y('Count:Q', title='Number of Close Matches'),
            color=alt.Color('Comparison:N', legend=None)
        ).properties(
            width=800,
            height=400
        )
        
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("No close date matches found within 7 days.")
    
    # Display the raw comparison results
    st.subheader("Detailed Comparison Results")
    
    for comparison_name, matches in comparisons:
        with st.expander(comparison_name):
            if matches:
                for date1, date2, days_apart in matches:
                    st.write(f"- {date1} and {date2} are {days_apart} days apart")
            else:
                st.write("No matches found within 7 days.")

# Add a summary dashboard
st.header("Summary Dashboard")

# Create a summary of all the dates
all_dates_summary = []
for date in top_dates:
    try:
        dt = datetime.strptime(date, "%d %B %Y")
        all_dates_summary.append({"Date": dt, "Method": "Top Squaring"})
    except ValueError:
        st.warning(f"Could not parse date: {date}")

for date in bottom_dates:
    try:
        dt = datetime.strptime(date, "%d %B %Y")
        all_dates_summary.append({"Date": dt, "Method": "Bottom Squaring"})
    except ValueError:
        st.warning(f"Could not parse date: {date}")

for date in range_dates:
    try:
        dt = datetime.strptime(date, "%d %B %Y")
        all_dates_summary.append({"Date": dt, "Method": "Range Squaring"})
    except ValueError:
        st.warning(f"Could not parse date: {date}")

for date in degrees_dates:
    try:
        dt = datetime.strptime(date, "%d %B %Y")
        all_dates_summary.append({"Date": dt, "Method": "Degrees"})
    except ValueError:
        st.warning(f"Could not parse date: {date}")

df_summary = pd.DataFrame(all_dates_summary)

# Make sure Date is datetime type
df_summary['Date'] = pd.to_datetime(df_summary['Date'])

# Sort by date
df_summary = df_summary.sort_values("Date")

# Count dates by month
df_summary['Month'] = df_summary['Date'].dt.strftime('%Y-%m')
date_counts = df_summary.groupby(['Month', 'Method']).size().reset_index(name='Count')

# Create a chart showing date counts by month and method
chart = alt.Chart(date_counts).mark_bar().encode(
    x=alt.X('Month:N', title='Month', sort=None),
    y=alt.Y('Count:Q', title='Number of Dates'),
    color=alt.Color('Method:N', title='Method'),
    tooltip=['Month', 'Method', 'Count']
).properties(
    width=800,
    height=400
).interactive()

st.altair_chart(chart, use_container_width=True)

# Display a calendar heatmap of all dates
st.subheader("Date Frequency Calendar")

# Create a calendar of all dates
df_summary['Day'] = df_summary['Date'].dt.day
df_summary['MonthName'] = df_summary['Date'].dt.strftime('%b')
df_summary['Year'] = df_summary['Date'].dt.year

# Count dates by day
date_counts_daily = df_summary.groupby(['Year', 'MonthName', 'Day']).size().reset_index(name='Count')

# Create a calendar heatmap
calendar_chart = alt.Chart(date_counts_daily).mark_rect().encode(
    x=alt.X('Day:O', title='Day of Month'),
    y=alt.Y('MonthName:O', title='Month', sort=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),
    color=alt.Color('Count:Q', scale=alt.Scale(scheme='blues')),
    tooltip=['Year', 'MonthName', 'Day', 'Count']
).properties(
    width=800,
    height=400
).interactive()

st.altair_chart(calendar_chart, use_container_width=True)