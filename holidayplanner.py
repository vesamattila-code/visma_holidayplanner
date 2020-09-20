import pandas as pd
from datetime import date, timedelta, datetime
import os.path
from os import path


class HolidayRangeTooWide(Exception):
    pass
    
class HolidayStartLaterThanEnd(Exception):
    pass

HOLIDAY_MAX_RANGE = 50

class HolidayAccess():

    def __init__(self,access = 0):
        self.access = access
        
    def get_access(self):
        return self.access
        
    def holidays_in_range(self, start, end):
        raise NotImplementedError
        
    def set_access(self, access):
        self.access = access

class HolidayCVSHandler(HolidayAccess):

    def __init__(self, access):
        HolidayAccess.__init__(self,access)
             
    def holidays_in_range(self, start, end):
        if not path.exists(self.access):
            raise FileNotFoundError
        count = 0
        date_to_check = start
        official_holidays=pd.read_csv(
            self.access, names=['date'])
        for i in official_holidays['date']:
            holiday = datetime.strptime(i, "%d.%m.%Y").date()
            d = date_to_check
            while d <= end:
                if holiday == d:
                    #skip if day is sunday
                    if holiday.weekday() != 6:  
                        count+=1
                d+=timedelta(days=1)
        return count


class HolidayPlanner():

    def __init__(self, holiday_access):
        self.holiday_handler = holiday_access
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
                                self.holiday_handler.holidays_in_range(
                                    start,end))
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
        
        