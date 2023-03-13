from datetime import timedelta, date

class DateRangeIterable:
    """
    An iterable class that generates a range of dates from a start date to an end date, inclusive.
    """
    def __init__(self, start_date: date, end_date: date):
        """
        Initializes the DateRangeIterable object with a start date and an end date.

        Parameters:
            start_date (date): The start date of the range.
            end_date (date): The end date of the range.
        """
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)
    
            

if __name__ == '__main__':
    print(DateRangeIterable(date(2023, 1, 1), date(2023, 1, 10)))

    for i in DateRangeIterable(date(2023, 1, 1), date(2023, 1, 10)):
        print(i)
    
        
    print(max(DateRangeIterable(date(2023, 1, 1), date(2023, 1, 10))))
    