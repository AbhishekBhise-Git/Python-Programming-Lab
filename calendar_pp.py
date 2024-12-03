def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return the number of days in a given month."""
    if month == 2:  # February
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:
        return 31

def calculate_first_day_of_year(year):
    """Calculate the day of the week for January 1st of a given year."""
    base_year = 1900  # January 1, 1900, was a Monday
    total_days = 0
    
    for y in range(base_year, year):
        total_days += 366 if is_leap_year(y) else 365
    
    return (total_days % 7)  # 0 = Monday, ..., 6 = Sunday

def generate_month_grid(month, year, first_day):
    """Generate a grid for the month's calendar."""
    grid = [["   "] * 7 for _ in range(6)]
    days = days_in_month(month, year)
    day = 1
    row, col = 0, first_day
    
    while day <= days:
        grid[row][col] = f"{day:2} "
        day += 1
        col += 1
        if col == 7:
            col = 0
            row += 1
    return grid

def print_month_grid(grid, month_name):
    """Print the month's calendar in a formatted way."""
    header = f"{month_name}".center(20, " ")
    print(header)
    print("Su Mo Tu We Th Fr Sa")
    for row in grid:
        print(" ".join(row))
    print()

def print_year_calendar(year):
    """Print the calendar for the entire year."""
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    first_day = calculate_first_day_of_year(year)
    
    for month in range(1, 13):
        print_month_grid(generate_month_grid(month, year, first_day), month_names[month - 1])
        first_day = (first_day + days_in_month(month, year)) % 7

# Get input from the user and print the calendar
year = int(input("Enter the year: "))
print_year_calendar(year)
