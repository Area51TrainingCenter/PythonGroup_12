import types

class OnConnectDecorator(object):
    def __init__(self, database, provider):
        self.provider = provider
    def __call__(self, func=None, provider=None):
        if isinstance(func, types.FunctionType):
            self.database._on_connect_funcs.append(func, provider or self.provider)
        if not provider and func is basestring:
            provider = func
        if not isinstance(provider, basestring):
            throw(TypeError)
        return OnConnectDecorator(self.database, provider)

class Database(object):
    def on_connect(database):
        return OnConnectDecorator(database, None)






@db.on_connect
def f1(conection):
    pass



def f1(connection):
    pass

f1 = db.on_connect(f1)



@db.on_connect(provider='sqlite')
def f1(conection):
    pass


def f1(connection):
    pass

real_decorator = db.on_connect(provider='sqlite')

f1 = real_decorator(f1)




