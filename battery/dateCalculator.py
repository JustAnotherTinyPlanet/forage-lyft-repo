from datetime import datetime

def dateCalculator(date1, date2):
        # Convert the date strings to datetime objects
        dt1 = datetime.strptime(date1, '%Y-%m-%d')
        dt2 = datetime.strptime(date2, '%Y-%m-%d')

        # Calculate the difference between the two dates
        time_delta = dt2 - dt1

        # Extract the number of years from the time delta
        years_between = time_delta.days / 365.25  # Using 365.25 to account for leap years

        return int(years_between)