import sys
import getpass
import os
from pySQLExport.cli import CLI
from pySQLExport.config import load_config
from pySQLExport.database import Database
from pySQLExport.query import Query
from pySQLExport.export import export_to_csv
from pySQLExport.utils import get_db_info_from_user

def main():

    cli = CLI()
    args = cli.parse_args(sys.argv[1:])

    
    config = None
    if args.config_file and os.path.isfile(args.config_file):
        config = load_config(args.config_file)
    else:
        print("Config file not found. Please provide the database information.")
        config = get_db_info_from_user()
        
    # Prompt for the password
    password = getpass.getpass(prompt='Enter database password: ')

    db = Database(config['host'], config['user'], password, config['database'], config['port'])
    
    query = Query(db)
    results = query.execute(args.query)
    
    if args.output:
        export_to_csv(results, args.output)
    else:
        for row in results:
            print(row)

if __name__ == "__main__":
    main()