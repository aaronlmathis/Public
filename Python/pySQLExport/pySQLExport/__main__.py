import sys
import getpass
import os
from pySQLExport.cli import CLI
from pySQLExport.config import load_config
from pySQLExport.database import Database
from pySQLExport.query import Query
from pySQLExport.export import Export
from pySQLExport.utils import get_db_info_from_user, print_colored

def main():
    try:
        cli = CLI()
        args = cli.parse_args(sys.argv[1:])
        
        config = None
        if args.config_file and os.path.isfile(args.config_file):
            try:
                config = load_config(args.config_file)
            except Exception as e:
                print_colored(f"Failed to load config file: {e}", "red")
                sys.exit(1)
        else:
            print_colored("Config file not found. Please provide the database information.", "yellow")
            config = get_db_info_from_user()
            
        # Prompt for the password
        password = getpass.getpass(prompt='Enter database password: ')

        try:
            db = Database(config['host'], config['user'], password, config['database'], config['port'])
        except Exception as e:
            print_colored(f"Failed to connect to the database: {e}", "red")
            sys.exit(1)
        
        try:
            query = Query(db)
            results = query.execute(args.query)
        except Exception as e:
            print_colored(f"Failed to execute query: {e}", "red")
            sys.exit(1)
        
        if args.output:
            if args.output not in ['csv']:
                print_colored("Invalid output type. Current options are CSV.", "red")
                sys.exit(1)
            if not args.outfile:
                print_colored("Please provide an output file path: ", "yellow", end='')
                args.outfile = input()

            try:
                exporter = Export(results, args.outfile)
                exporter.export(args.output)
            except Exception as e:
                print_colored(f"Failed to export results: {e}", "red")
                sys.exit(1)
        else:
            for row in results:
                print(row)

    except Exception as e:
        print_colored(f"An unexpected error occurred: {e}", "red")
        sys.exit(1)

if __name__ == "__main__":
    main()
