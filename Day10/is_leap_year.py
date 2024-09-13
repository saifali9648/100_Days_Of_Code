def is_leap_year(year):
    """Take input as year and return the ture or false: is leap year or not leap year"""
    if year%400==0:
        return True
    elif year%4==0 and year%100 !=0:
        return True
    else:
        return False
    
year=int(input("enter a year that you want to check is leap year or not:?"))
print(is_leap_year(year=year))