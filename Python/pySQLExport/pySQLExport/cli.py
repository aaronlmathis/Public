import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(description="MySQL CLI Tool")
    parser.add_argument('--config-file', type=str, required=True, help='Path to the database config file')
    parser.add_argument('--query', type=str, required=True, help='SQL query to execute')
    parser.add_argument('--output', type=str, help='Output CSV file to save the results')
    return parser.parse_args(args)