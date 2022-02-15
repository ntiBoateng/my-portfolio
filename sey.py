import datetime

time = datetime.datetime.now().time()
morning = time.replace(hour=7, minute=45, second=0, microsecond=0)
if time >= morning:
    print("turn on {} >= {}".format(time,morning))
else:
    print("turn off {} <= {}".format(time,morning))