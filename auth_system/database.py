import mysql.connector
from config import DB_CONFIG

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        # Use buffered=True to automatically fetch all results
        self.cursor = self.connection.cursor(dictionary=True, buffered=True)


    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return None

    def close(self):
        self.cursor.close()
        self.connection.close()
