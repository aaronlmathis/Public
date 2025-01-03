import argparse
import sys
import yaml
from deepdiff import DeepDiff
from pprint import pprint

def load_yaml(file_path):
    """
    Load a YAML file and return its contents as a Python dictionary.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            print(f"\nLoaded '{file_path}':")
            pprint(data)
            return data
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file {file_path}: {exc}")
        sys.exit(1)

def compare_yamls(yaml1, yaml2, ignore_order=True):
    """
    Compare two Python dictionaries and return the differences.
    """
    differences = DeepDiff(yaml1, yaml2, ignore_order=ignore_order)
    return differences

def main():
    parser = argparse.ArgumentParser(description="Compare two YAML files and report differences.")
    parser.add_argument("file1", help="Path to the first YAML file.")
    parser.add_argument("file2", help="Path to the second YAML file.")
    parser.add_argument(
        "-i",
        "--ignore-order",
        action="store_true",
        help="Ignore the order of list items."
    )
    args = parser.parse_args()

    yaml1 = load_yaml(args.file1)
    yaml2 = load_yaml(args.file2)

    differences = compare_yamls(yaml1, yaml2, args.ignore_order)

    if differences:
        print("\nDifferences found:")
        if 'values_changed' in differences:
            print("\nValues Changed:")
            pprint(differences['values_changed'])
        if 'dictionary_item_added' in differences:
            print("\nItems Added:")
            pprint(differences['dictionary_item_added'])
        if 'dictionary_item_removed' in differences:
            print("\nItems Removed:")
            pprint(differences['dictionary_item_removed'])
        # Add more categories as needed
    else:
        print("\nThe YAML files are identical.")

if __name__ == "__main__":
    main()
