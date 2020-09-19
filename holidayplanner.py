import pandas as pd

class HolidayPlanner():
    
    def __init__(self,holiday_file='holiday_dates.csv'):
        self.official_holidays=pd.read_csv(holiday_file, names=['date'])
        
