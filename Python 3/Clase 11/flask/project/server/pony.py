from pony.orm import *

db = Database()

class Restautants(db.Entity):
    name = Required(str, unique=True)
    owner = Required(str)
    folk = Optional(bool)

    def __str__(self):
        return str(self.name)

POSTGRES_URL = 'salt.db.elephantsql.com'
POSTGRES_USER = 'qhpmvcxf'
POSTGRES_PW = 'KVyxuSnUjHqmS8cv87HmKljukR7IKAXA'
POSTGRES_DB = 'qhpmvcxf'

db.bind(
    'postgres',
    user=POSTGRES_USER,
    password=POSTGRES_PW,
    host=POSTGRES_URL,
    database=POSTGRES_DB,
    port='5432'
)

db.generate_mapping(create_tables=True)