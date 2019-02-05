import psycopg2


class DatabaseConnection:
    '''
     A class which manages database interactions
    '''

    def __init__(self, db_user, db_password, dbname, db_host='localhost', db_port=5432):

        try:
            self.connection = psycopg2.connect(
                host=db_host, post=db_port, dbname=dbname, user=db_user, password=db_password)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except Exception as ex:
            print(f"Unable to connect to the database! Error {ex}")

    def create_table(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as ex:
            print(f"Could not create table. Error: {ex}")

if __name__ == "__main__":
    database_conn = DatabaseConnection('test', 'test', 'test')