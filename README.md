# visma_holidayplanner
Programming task

Initial thoughts on task:

-do unitests

-need function that returns number of holiday days needed in time range
   -checks dates are in scope
   -check given params are dates
   -check start < end
   -max range 50 days
   -take count sundays and official holidays
       -count number of sundays in range (separate function?)
       -count number of official holidays in range(function)   
-need function that returns delta of given dates
-list of official holiday dates
   -this version will have dates 2020-2021
   -list can/will change in future version, no hardcoding.
   -put list in file that can be updated with more dates, logic in class will remain same.
      - curreent file as default param for the class init?
      
   
