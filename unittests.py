import unittest
from holidayplanner import HolidayPlanner


class TestHolidayPlanner(unittest.TestCase):

    def test_planner_default_init(self):
        p = HolidayPlanner()
        assert(p)
        
    def test_planner_with_file_param(self):
        with self.assertRaises(FileNotFoundError):    
            HolidayPlanner('non_existing_file.cvs')
        
    def test_planner_with_empty_param(self):
        with self.assertRaises(FileNotFoundError):    
            HolidayPlanner('non_existing_file')
        pass
        
    def test_planner_with_non_string(self):
        with self.assertRaises(ValueError):    
            HolidayPlanner(123)
        pass
    
        

if __name__ == '__main__':
    unittest.main()