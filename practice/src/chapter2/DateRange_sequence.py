from datetime import timedelta, date
from datetime import date

class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._date_range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day <= self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days
    
    def __getitem__(self, index):
        return self._date_range[index]

    def __len__(self):
        return len(self._date_range)
    
if __name__ == "__main__":
    temp_days = DateRangeSequence(date(2023, 1, 1), date(2023, 1, 10))

    for day in temp_days:
        print(day)
    ## becuase we wrapped object with a list,
    ## we don`t have to implement about sequence magic method!
    temp_days[10]