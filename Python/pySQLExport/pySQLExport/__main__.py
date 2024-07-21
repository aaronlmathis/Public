import sys
import getpass
from pySQLExport.cli import parse_args
from pySQLExport.config import load_config
from pySQLExport.database import Database
from pySQLExport.query import Query
from pySQLExport.export import export_to_csv

def main():
    args = parse_args(sys.argv[1:])
    config = load_config(args.config_file)
    
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