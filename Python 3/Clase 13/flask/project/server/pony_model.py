from pony.orm import *

db = Database()


class Restautants(db.Entity):
    name = Required(str, unique=True)
    owner = Required(str)
    folk = Optional(bool)
    folks = Set('Folks')

    @property
    def serializer(self):
        return {
            'name': self.name,
            'owner': self.owner,
            'folk': self.folk,
            'folks': self.folks.get()
        }

    def __str__(self):
        return str(self.name)


class Folks(db.Entity):
    restautants = Set('Restautants')
    quantity = Required(int)


class City(db.Entity):
    name = Required(str)
    query = Set('Location', revserse='location')
    weather = Set('WeatherDescription', reverse='city')

    @property
    def serializer(self):
        return {
            'name': self.name,
        }

    def __str__(self):
        return str(self.name)


class Localtion(db.Entity):
    name = Required(str)
    country = Required(str)
    lan = Required(str)
    long = Required(str)
    location = Set('City', reverse='query')

    @property
    def serializer(self):
        return {
            'name': self.name,
        }

    def __str__(self):
        return str(self.name)


class WeatherDescription(db.Entity):
    description = Required(str)
    city = Set('City', reverse='weather')

    @property
    def serializer(self):
        return {
            'name': self.description,
        }

    def __str__(self):
        return str(self.description)


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
