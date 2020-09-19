import pandas as pd
import datetime
from datetime import date, timedelta, datetime

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
        #holidays_count=official_holidays_in_range(start,end)
        holidays_count=0
        holidays_needed = self.calculate_holidays_needed(delta.days,self.sundays_in_range(start,end), holidays_count)
        return holidays_needed
        
    def sundays_in_range(self,start,end):
        d0 = start
        d1 = end
        d0 += timedelta(days=6 - d0.weekday())  # First Sunday
        day_count = 0
        while d0 <= d1:
            # check yield usage in this function?
            d0 += timedelta(days=7)
            day_count += 1
        return day_count
        
    def calculate_holidays_needed(self,days, sundays,holidays):
        return days-sundays-holidays
        
    def official_holidays_in_range(self, start, end):
        pass
        