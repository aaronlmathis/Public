def get_db_info_from_user():
    host = input("Enter database host: ")
    user = input("Enter database user: ")
    database = input("Enter database name: ")
    port = input("Enter database port (default 3306): ")
    port = int(port) if port else 3306
    return {
        'host': host,
        'user': user,
        'database': database,
        'port': port
    }
