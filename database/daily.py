from database.models import db, Daily
from .elements import periodic_table

def query_daily_element():
    d_previous = Daily.query.all()
    if d_previous != []:
        d_ind = d_previous[0]
        d_info = vars(d_ind)
        d_list = list(d_info.items())
        d_el = d_list[1:]
        d_filter = [item for item in d_el if 'symbol' in item]
        d = d_filter[0][1]
        return d
    else:
        return None

el = query_daily_element()


for i in periodic_table:
    if i['symbol'] == el:
        return i