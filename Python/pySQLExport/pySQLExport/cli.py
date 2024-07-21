import argparse

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="pySQLExport CLI Tool")
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument('--config-file', type=str, required=False, help='Path to the database config file')
        self.parser.add_argument('--query', type=str, required=True, help='SQL query to execute')
        self.parser.add_argument('--output', type=str, help='Output CSV file to save the results')

    def parse_args(self, args):
        return self.parser.parse_args(args)