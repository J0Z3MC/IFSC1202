seconds_in_a_minute = 60
seconds_in_an_hour = seconds_in_a_minute * 60
seconds_in_a_day = seconds_in_an_hour * 24
seconds_in_a_year = seconds_in_a_day * 365

total_seconds = int(input("Enter the length of time in seconds: "))

years = total_seconds // seconds_in_a_year
remaining_seconds = total_seconds % seconds_in_a_year

days = remaining_seconds // seconds_in_a_day
remaining_seconds %= seconds_in_a_day

hours = remaining_seconds // seconds_in_an_hour
remaining_seconds %= seconds_in_an_hour

minutes = remaining_seconds // seconds_in_a_minute
remaining_seconds %= seconds_in_a_minute

seconds = remaining_seconds

print(f"Years: {years}")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")