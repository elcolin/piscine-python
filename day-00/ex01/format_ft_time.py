import datetime
import time

current_datetime = datetime.datetime.now()
print("Seconds since January 1, 1970: ", "{:,.4f}".format(time.time()), " or ", "{:.2e}".format(time.time()))
print(current_datetime.strftime("%b %d %Y"))