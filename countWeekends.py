from datetime import date, timedelta

def compute_prefix_weekend_counts(start_date, end_date):
    """Computes prefix sum of weekend counts up to each date."""
    current_date = start_date
    saturday_count, sunday_count = 0, 0
    prefix_weekend_counts = {}

    while current_date <= end_date:
        if current_date.weekday() == 5:  # Saturday
            saturday_count += 1
        elif current_date.weekday() == 6:  # Sunday
            sunday_count += 1
        
        # Store cumulative sum in the dictionary
        prefix_weekend_counts[current_date] = (saturday_count, sunday_count)
        
        # Move to the next day
        current_date += timedelta(days=1)

    return prefix_weekend_counts


# Example Usage
start_date = date(2024, 1, 1)  # Define a start date
end_date = date(2100, 1, 1)  # Define a long-range end date

# Precompute prefix weekend counts
prefix_weekend_counts = compute_prefix_weekend_counts(start_date, end_date)

