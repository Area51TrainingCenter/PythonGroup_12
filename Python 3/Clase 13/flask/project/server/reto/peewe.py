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


class Category(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)
    uuid = UUIDField

    @property
    def serializer(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Movie(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)
    category = ForeignKeyField(Category)

    @property
    def serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category.name
        }

psql.create_tables([Category, Movie])

