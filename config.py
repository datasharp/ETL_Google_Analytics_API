from datetime import datetime, timedelta

start_date = datetime.strftime(datetime.now() - timedelta(days = 7),'%Y-%m-%d')
end_date = datetime.strftime(datetime.now(),'%Y-%m-%d')
date_range = "{}_{}".format(start_date, end_date)
rolling_window = 7


