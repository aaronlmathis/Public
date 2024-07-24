from database import Database

class PySQLExport:
    def __init__(self):
        self.config = {}
        self.test = "foofoofoo"

    def connect_db(self, host, user, pw, database, port):
        self.config = {
            "host": host,
            "user": user,
            "pass": pw,
            "port": port,
            "database": database
        }
        try:
            self.db = Database(host, user, pw, database, port)
            return True
        except Exception as e:
            return False
        
    def execute_query(self, query):
        try:
            self.results,  self.columns = self.db.execute(query)
        except Exception as e:
            print(f"Failed to execute query: {e}")

        return self.results, self.columns
        