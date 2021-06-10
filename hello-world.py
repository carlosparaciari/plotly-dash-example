from datetime import datetime

time_today = datetime.now()

print("hello world on {}".format(datetime.strftime(time_today, "%d-%m-%Y")))
