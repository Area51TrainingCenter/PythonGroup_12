from collections import namedtuple
from pony.orm import *


class DataAccess:
    """
    API implementation for a relation database access.
    """

    @db_session
    def select(self, query, query_args=None, classname=None, output_as_dict=False):
        """
        select() method uses the query string provided for retrieving information
        :param query: Query to be executed.  Parameter to be passed had to be prefixed with $ sign.
                      e.g: "select id, name from Person where name = $x"

        :param classname:
        :param query_args: Arguments that need to be passed to the query. e.g: {"x" : "Susan"}
        :param output_as_dict: When true, output will be returned as list of dict objects :e.g: [{"x" : "Susan"}],
                                if below condition is satisfied, classname is None and "*" is not provided in select
                                query for columns

        :return:
        """
        data = self.db.select(query, query_args)
        # if classname or output as dict is true
        # creation of key values is done
        # else list of tuples is returned
        if classname or output_as_dict:
            column_names = query.split('select ', 1)[1].split('from')[0].strip()

            # if * is provided in the column names list
            # return the tuple list
            if column_names.find("*") == -1:
                return data

            column_names_list = column_names.split(',')
            data_as_dict_list = []

            # loop over list of tuples
            # create a dict item
            # with column names from select list by index and
            # value as tuple element by index
            for item in data:
                dict_item = {}
                for idx, elem in enumerate(item):
                    dict_item.update({column_names_list[idx].strip(): elem})
                data_as_dict_list.append(dict_item)

            if classname:
                data_class_list = []
                for idx, dict_item in enumerate(data_as_dict_list):
                    data_as_dict_list.append(namedtuple(classname, dict_item.keys())(*dict_item.values()))
                return data_class_list
            else:
                return data_as_dict_list
        else:
            return data

    @db_session
    def create(self, query, callback=None, query_args=None):
        """
        create() method takes the query string for creating table
        :param query:
        :param callback:
        :param query_args: Arguments that need to be passed to the query. e.g: {"x" : "Susan"}
        :return:
        """
        data = self.db.execute(query, query_args)
        return data

    @db_session
    def insert(self, query, callback=None, query_args=None):
        """
        insert() method for inserting an item
        :param query:
        :param callback:
        :param query_args:
        :return:
        """
        data = self.db.execute(query, query_args)
        return data

    @db_session
    def update(self, query, callback=None, query_args=None):
        """
        update() method for updating information of a given item
        :param query:
        :param callback:
        :param query_args:
        :return:
        """
        data = self.db.execute(query, query_args)
        return data

    @db_session
    def delete(self, query, callback=None, query_args=None):
        """
        delete() method for deleting an item
        :param query:
        :param callback:
        :param query_args:
        :return:
        """
        data = self.db.execute(query, query_args)
        return data

    @db_session
    def execute(self, query, classname=None, query_args=None):
        """
        execute() method for executing a procedure/function
        :param query:
        :param classname:
        :param query_args:
        :return:
        """
        data = self.db.execute(query, query_args)
        return data

    @db_session
    def execute_procedure(self, procedure_name_params, procedure_args=None):
        """
        execute_procedure() method for executing a procedure
        :param
        procedure_name_params: name of a procedure and if any IN params e.g: myprocedure($x, $y).
                                              ALL IN parameters had to be prefixed with $ symbol
                :param procedure_args: any parameters that had to be passed to procedure {'x': 10, 'y': 20}
                :return:
                """
        data = self.db.execute("call " + procedure_name_params, procedure_args)
        return data

    @db_session
    def execute_function(self, function_name_params, function_args=None):
        """
        execute_function() method for executing a function
        :param function_name_params: name of a function and if any IN params e.g: myfunction($x, $y).
                                      ALL IN parameters had to be prefixed with $ symbol
        :param function_args: any parameters that had to be passed to function {'x': 10, 'y': 20}
        :return:
        """
        data = self.db.execute("select " + function_name_params, function_args)
        return data

    @db_session
    def begin_transaction(self):
        """
        begin_transaction() method for initiating transaction
        :return:
        """
        self.db.commit(False)

    @db_session
    def end_transaction(self):
        """
        end_transaction() method for end a transaction
        :return:
        """
        self.db.commit(True)

    @db_session
    def rollback(self):
        """
        rollback() rollback a transaction
        :return:
        """
        self.db.rollback()

    def __init__(self, provider, hostname, **kwargs):
        """
        Initializes FTP, SFTP setup
        :param provider: [MySQL, Oracle, PostgreSQL] only these providers are supported as of now
        :param hostname:
        :param kwargs:
            username - username to access database
            password -  password of the user
            db - database instance
        """
        self.provider = provider
        self.hostname = hostname
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.database = kwargs.get('database')

        if self.provider not in SupportedDatabase.__members__:
            db_list = ','.join(list(SupportedDatabase.__members__))
            raise Exception(
                provider + ', is not supported at this time.  Following databases are only supported : ' + db_list)

        self.db = Database()
        self.db.bind(provider=SupportedDatabase[self.provider].value, user=self.username, password=self.password,
                     host=self.hostname, database=self.database)
