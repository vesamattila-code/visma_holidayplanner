import unittest
from holidayplanner import HolidayPlanner, HolidayCVSHandler,HolidayStartLaterThanEnd,HolidayAccess,HolidayRangeTooWide
import datetime
from datetime import date, timedelta, datetime
import pandas as pd


class TestHolidayPlanner(unittest.TestCase):

    def test_holiday_access(self):
        acc=HolidayAccess()
        acc.get_access()
        acc.set_access(0)
        with self.assertRaises(NotImplementedError):
            acc.holidays_in_range(date(2020,12,31),date(2020,10,1))

    def test_planner_default_init(self):
        p = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        self.assertTrue(p)
            
    def test_days_needed_start_later_than_end(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        with self.assertRaises(HolidayStartLaterThanEnd):
            planner.days_needed(date(2020,12,31),date(2020,10,1))
            
    def test_days_needed_range_over_max_range(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        with self.assertRaises(HolidayRangeTooWide):
            planner.days_needed(date(2020,10,1),date(2020,12,1))
            
    def test_planner_with_empty_param(self):
        with self.assertRaises(FileNotFoundError):    
            planner = HolidayPlanner(HolidayCVSHandler(''))     
            result = planner.days_needed(date(2020,10,1),date(2020,10,12))
            
    def test_planner_with_non_string(self):   
        planner=HolidayPlanner(HolidayCVSHandler(123))
        
    def test_sundays_in_range(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        self.assertEqual(planner.sundays_in_range(
            date(2020,10,1),date(2020,10,31)),4)
        
    def test_days_needed_valid_month_25_days(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        self.assertEqual(planner.days_needed(date(2020,1,1),
            date(2020,1,31)),25)
        
    def test_days_needed_valid_month_15_days(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        self.assertEqual(planner.days_needed(
            date(2020,4,10), date(2020,5,1)),16)
        
    def test_days_needed_valid_month_year_changing(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        self.assertEqual(planner.days_needed(date(2020,12,25),
            date(2021,1,7)),9)
        
    def test_days_needed_one_day_scope(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        self.assertEqual(planner.days_needed(
            date(2021,12,25),date(2021,12,25)),1)
        
    def test_days_needed_without_fake_sunday_added(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates.csv'))
        self.assertEqual(planner.days_needed(
            date(2020,10,1),date(2020,10,30)),26)
        
    def test_days_needed_with_fake_sunday_added(self):
        planner = HolidayPlanner(HolidayCVSHandler('holiday_dates_with_fake_sunday_11102020.csv'))
        self.assertEqual(planner.days_needed(
            date(2020,10,1),date(2020,10,30)),26)
    
        

    
        

if __name__ == '__main__':
    unittest.main()