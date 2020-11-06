from .database import SessionLocal, engine
from database import models
from .elements import periodic_table

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

try:
    for i in periodic_table:
        db_record = models.Element(
            ele = i['element'],
            weight = float(i['atomic weight']),
            grouping = i['class'],
            phase = i['phase'],
            period = int(i['period']),
            config = i['electron config'],
            melting = float(i['melting point']),
            boiling = float(i['boiling point']),
            symbol = i['symbol']
        )
        db.add(db_record)
        db.commit()
    print('all set!')
except Exception as e:
    print(e)
finally:
    db.close()
    print('DONE SEEDING')