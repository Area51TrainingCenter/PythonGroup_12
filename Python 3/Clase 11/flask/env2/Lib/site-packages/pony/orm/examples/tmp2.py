from pony import orm
from pony.orm import db_session

orm.sql_debug(True)

db = orm.Database()

class A(db.Entity):
    friends = orm.Set("B", reverse="friends") #, index="foo", reverse_index="bar")

class B(db.Entity):
    friends = orm.Set("A", reverse="friends")

db.bind(provider='sqlite', filename=":memory:", create_db=True)
db.generate_mapping(check_tables=False)
db.drop_all_tables(with_all_data=True)
db.create_tables()

if __name__ == "__main__":
    with db_session:
        c1 = A()
        c2 = B(friends=c1)

    with db_session:
        print(A.select()[:])
        A.select().delete(bulk=True)
