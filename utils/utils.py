import csv
import json
from typing import List, Dict, Any


def save_to_json(data: Any, filename: str = "output.json") -> None:
    """
    Save data to a JSON file.

    Args:
        data (Any): The data to be saved in JSON format.
        filename (str, optional): The name of the output file. Defaults to "output.json".

    Returns:
        None
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def save_to_csv(data: List[Dict[str, Any]], filename: str = "output.csv") -> None:
    """
    Save data to a CSV file.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries containing the data to be saved.
        filename (str, optional): The name of the output file. Defaults to "output.csv".

    Returns:
        None
    """
    if not data:
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
