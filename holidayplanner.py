import pandas as pd
class HolidayRangeTooWide(Exception):
    pass
    
class HolidayStartLaterThanEnd(Exception):
    pass

HOLIDAY_MAX_RANGE = 50

class HolidayPlanner():

    
    def __init__(self,holiday_file='holiday_dates.csv',max_range=HOLIDAY_MAX_RANGE):
        self.official_holidays=pd.read_csv(holiday_file, names=['date'])
        self.holiday_max_range = HOLIDAY_MAX_RANGE
        
    def days_needed(self, start, end):
        if start > end:
            raise HolidayStartLaterThanEnd
        delta = end - start
        if delta.days > self.holiday_max_range:
            raise HolidayRangeTooWide
        day_count = 0
        #official_holidays_in_range(start,end)
        #sundays_in_range(start,end)
        #calculate_holidays_needed()
        return day_count