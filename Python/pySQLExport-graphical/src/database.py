def get_database(db_type, host, user, pw, database, port):
    if db_type == 'MySQL':
        from database_mysql import MySQLDatabase
        return MySQLDatabase(host, user, pw, database, port)
    elif db_type == 'PostgreSQL':
        from database_pgsql import PgSQLDatabase
        return PgSQLDatabase(host, user, pw, database, port)
