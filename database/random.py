import random
from .database import SessionLocal, engine
from database import models
from .elements import periodic_table
from .models import Element, Daily

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

def find_random_element():
    e_num = random.randint(1,50)
    e_select = db.query(Element).filter(Element.id == e_num).first()
    e_info = vars(e_select)
    e_data = list(e_info.items())
    e_list = e_data[1:]
    e_filter = [item for item in e_list if 'symbol' in item]
    e = e_filter[0][1]
    return e



def query_daily_element():
    d_previous = db.query(Daily).all()
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

e_found = find_random_element()
d_found = query_daily_element()

if (e_found == d_found):
    while e_found == d_found:
        e_found = find_random_element()
        if (e_found != d_found):
            break


def updating_daily_element():
    if (e_found and d_found != None):
        retrieve = db.query(Daily).all()[0]
        db.delete(retrieve)
        db.commit()
        print('success')
        data = models.Daily(
            symbol = e_found
        )
        db.add(data)
        db.commit()
        db.close()
        print('#1')
    else:
        data = models.Daily(
            symbol = e_found
        )
        db.add(data)
        db.commit()
        db.close()
        print('#2')

updating_daily_element()