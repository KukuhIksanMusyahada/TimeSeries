from datetime import date, timedelta

TODAY= date.today()
END_DATE= TODAY.strftime('%Y-%m-%d')
num_day = 5500
choosen_date= TODAY - timedelta(days= num_day)
START_DATE= choosen_date.strftime('%Y-%m-%d')