days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days, that takes as input a number representing a month
def how_many_days(month_number):


# , and returns
# the number of days in that month.
    return days_in_month[month_number -1]

print how_many_days(5)
