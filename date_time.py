
from datetime import datetime, date, timedelta
date_now = date.today()
delta = timedelta(days=1)
date_before_today = date_now - delta
delta_month = timedelta(days=30)
date_before_month = date_now - delta_month
print(date_now.strftime('%d.%m.%Y'))
print(date_before_today.strftime('%d.%m.%Y'))
print(date_before_month.strftime('%d.%m.%Y'))


date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
