import datetime
def time_minutes_before(minutes):
    return datetime.datetime.now() - datetime.timedelta(minutes= minutes)

def get_curr_time():
    return datetime.datetime.now()