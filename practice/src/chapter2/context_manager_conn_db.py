import pymysql
from pymysql.connections import Connection


class MySQLManager:
    def __init__(self, config):
        self._config = config
        self.connection = None

    def __enter__(self):
        try:
            self.connection = pymysql.connect(**self._config)
            return self.connection
        except pymysql.DatabaseError as e:
            raise Exception('Unable to connect to MySQL server...') from e
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.connection.rollback()
            print(f"Error is occured by this => {exc_type} - {exc_value}")
        self.connection.close()

if __name__ == '__main__':
    config = {
        'host': 'localhost',
        'user': 'root',
        'database': 'employees',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
        'unix_socket': '/tmp/mysql.sock'
    }    
    
    with MySQLManager(config) as conn:
        try:
            # Execute a SELECT query
            with conn.cursor() as cursor:
                query = 'SELECT * FROM employees LIMIT 10;'
                cursor.execute(query)
                results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)
        except pymysql.DatabaseError as e:
            print(f'Error occurred: {e}')


