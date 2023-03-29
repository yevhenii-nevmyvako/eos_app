import json
import csv


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


if __name__ == "__main__":
    save_to_csv()
    save_to_json()
