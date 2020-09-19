import unittest
from holidayplanner import HolidayPlanner,HolidayStartLaterThanEnd,HolidayRangeTooWide
from datetime import date, timedelta, datetime


class TestHolidayPlanner(unittest.TestCase):

    def test_planner_default_init(self):
        p = HolidayPlanner()
        self.assertTrue(p)
        
    def test_planner_with_file_param(self):
        with self.assertRaises(FileNotFoundError):    
            HolidayPlanner('non_existing_file.cvs')
        
    def test_planner_with_empty_param(self):
        with self.assertRaises(FileNotFoundError):    
            HolidayPlanner('non_existing_file')
        
    def test_planner_with_non_string(self):
        with self.assertRaises(ValueError):    
            HolidayPlanner(123)
            
    def test_days_needed_start_later_than_end(self):
        planner = HolidayPlanner()
        with self.assertRaises(HolidayStartLaterThanEnd):
            planner.days_needed(date(2020,12,31),date(2020,10,1))
            
    def test_days_needed_range_over_max_range(self):
        planner = HolidayPlanner()
        with self.assertRaises(HolidayRangeTooWide):
            planner.days_needed(date(2020,10,1),date(2020,12,1))
    
    def test_days_needed_valid_month(self):
        planner = HolidayPlanner()
        planner.days_needed(date(2020,10,1),date(2020,10,31))
        self.assertEqual(planner.days_needed(date(2020,10,1),date(2020,10,31)),26)

    
        

if __name__ == '__main__':
    unittest.main()