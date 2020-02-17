from pony.orm import *

db = Database()
POSTGRES_URL = 'salt.db.elephantsql.com'
POSTGRES_USER = 'qhpmvcxf'
POSTGRES_PW = 'KVyxuSnUjHqmS8cv87HmKljukR7IKAXA'
POSTGRES_DB = 'qhpmvcxf'


class Country(db.Entity):
    name = Required(str)
    user = Set('UserOscar')

    @property
    def serializer(self):
        return {
            'id': self.id,
            'name': self.name
        }


class UserOscar(db.Entity):
    name = Required(str)
    last_name = Required(str)
    country = Required(Country)

    @property
    def serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'country': self.country.name
        }


db.bind(
    'postgres',
    user=POSTGRES_USER,
    password=POSTGRES_PW,
    host=POSTGRES_URL,
    database=POSTGRES_DB,
    port='5432'
)

db.generate_mapping(create_tables=True)
