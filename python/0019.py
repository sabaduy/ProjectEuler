def get_days_in_month(month, year):
	if month in [4,6,9,11]:
		return 30
	elif month == 2:
		if year % 4 == 0:
			if year % 100 == 0 and year % 400 != 0:
				return 28
			return 29
		else:
			return 28
	else:
		return 31

# Week starts on sunday = 0
month_start_day = (1 + 365) % 7 # Initialize by knowing: 1 Jan 1900 was a Monday
month           = 1
year            = 1901

count = 0
days_in_month = 0
while year < 2001:
	month = 1
	while month < 13:
		# Check this month start day
		if month_start_day == 0:
			count += 1

		# Set up next month
		month_start_day = (month_start_day + get_days_in_month(month, year)) % 7
		month += 1

	year += 1

print(count)