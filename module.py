import argparse
import json
import csv
import os
from exceptions_for_eos_app import (
    OutputFileExistsError,
    FileExtensionError,
    NotTwoDimensionalArrayError,
)


def save_to_json(path: str, data: any) -> None:
    """Context manager with arguments(path: str, data: any),
    create & save data to json file"""

    with open(path, "w") as json_file:
        json.dump(data, json_file)


def save_to_csv(path: str, data: any) -> None:
    """Context manager with arguments(path: str, data: any),
    create & save data to .csv file"""

    with open(path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)


def main() -> None:
    pass
    """Main function create cli interface witch transfer
     arguments(path & data) to save_to_json function."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        type=str,
        help="First argument - the path to the output file")
    parser.add_argument(
        "data",
        type=str,
        help="Second argument - the two-dimensional integer list as str")
    args = parser.parse_args()

    if os.path.exists(args.path):
        """Check validation for exists of file"""

        raise OutputFileExistsError("This file already exist")

    data = json.loads(args.data)

    if args.path.endswith(".csv"):
        """Check validation file is in `.csv` format"""
        save_to_csv(args.path, data)
    elif args.path.endswith(".json"):
        """Check validation file is in .json` format"""
        save_to_json(args.path, data)
    else:
        raise FileExtensionError("File must be only in `.JSON or .CSV` format")

    if not isinstance(data, list) or not all(
            isinstance(row, list) for row in data
    ):
        """Check validation for two-dimensional lists of integer"""

        raise NotTwoDimensionalArrayError(
            "The data should be a two-dimensional list of integers"
        )

    save_to_json(args.path, data)
    print(f"Create new file: {args.path}")


if __name__ == "__main__":
    main()
