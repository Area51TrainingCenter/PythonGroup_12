from peewee import *

POSTGRES_URL = 'salt.db.elephantsql.com'
POSTGRES_USER = 'qhpmvcxf'
POSTGRES_PW = 'KVyxuSnUjHqmS8cv87HmKljukR7IKAXA'
POSTGRES_DB = 'qhpmvcxf'


psql = PostgresqlDatabase(
    user=POSTGRES_USER,
    password=POSTGRES_PW,
    host=POSTGRES_URL,
    database=POSTGRES_DB,
)

class BaseModel(Model):
    class Meta:
        database = psql

class City(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(verbose_name=u'Nombre', max_length=100)
    countrycode = CharField(max_length=2)
    district = CharField(max_length=29)
    poblacion = BigIntegerField()

    @property
    def serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'countrycode': self.countrycode,
            'district': self.district,
            'poblacion': self.poblacion
        }

    def __str__(self):
        return f'{self.name} {self.district}'

    def __repr__(self):
        return {'name': self.name, 'district': self.district}


psql.create_tables([City])
