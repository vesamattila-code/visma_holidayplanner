import pandas as pd
#import datetime
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
        holidays_needed=1
        if start > end:
            raise HolidayStartLaterThanEnd
        if(start != end):
            delta = end - start

            if delta.days > self.holiday_max_range:
                raise HolidayRangeTooWide
            holidays_needed = self.calculate_holidays_needed(
                                delta.days+1, # count of days is delta +1
                                self.sundays_in_range(start,end), 
                                self.official_holidays_in_range(start,end))
        return holidays_needed
        
    def sundays_in_range(self, d0, d1):
        d0 += timedelta(days=6 - d0.weekday())
        day_count = 0
        while d0 <= d1:
            d0 += timedelta(days=7)
            day_count += 1
        return day_count
        
    def calculate_holidays_needed(self,days, sundays,holidays):
        return days-sundays-holidays
        
    def official_holidays_in_range(self, start, end):
        count = 0
        date_to_check = start
        for i in self.official_holidays['date']:
            holiday = datetime.strptime(i, "%d.%m.%Y").date()
            d = date_to_check
            while d <= end:
                if holiday == d:
                    if holiday.weekday() != 6:  #skip if day is sunday
                        count+=1
                d+=timedelta(days=1)
        return count
        