#! python
# encoding:utf-8

def test_datetime():
    from datetime import timedelta
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print c.days
    print c.seconds
    print c.seconds / 3600.0
    print c.total_seconds() / 3600.0

    from datetime import datetime
    d = datetime(2016, 3, 23)
    print d + timedelta(days=10)
    e = datetime(2016, 4, 2)
    f = e - d
    print f
    print f.days
    now = datetime.today()
    print now
    print now + timedelta(minutes=60)

def test_dateutil():
    from dateutil.relativedelta import relativedelta
    from datetime import datetime
    a = datetime(2016, 3, 23)
    print a + relativedelta(months=+1)
    b = datetime(2016, 5, 24)
    c = relativedelta(b, a)
    print c
    print c.months
    print c.days

def get_previous_byday(dayname, start_date=None):
    from datetime import datetime, timedelta
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    print target_date
    return target_date

def iter_month_date(start_date=None):
    def get_month_range(start_date=None):
        from datetime import datetime, date, timedelta
        import calendar

        if start_date is None:
            start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
        return (start_date, end_date)
    def test():
        from datetime import timedelta
        a_day = timedelta(days=1)
        first_day, last_day = get_month_range()
        while first_day < last_day:
            print first_day
            first_day += a_day

    from datetime import datetime, date, timedelta
    def date_range(start, stop, step=timedelta(days=1)):
        while start < stop:
            yield start
            start += step
    for d in date_range(date(2016, 3, 23), date(2016, 4, 1)):
        print d
    for d in date_range(datetime(2016, 3, 23), datetime(2016, 4, 1)):
        print d

def main():
    #test_datetime()
    #test_dateutil()
    #get_previous_byday('Saturday')
    iter_month_date()

if __name__ == '__main__':
    main()