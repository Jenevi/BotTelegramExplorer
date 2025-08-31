import csv
from typing import Iterable, Dict


def save_csv(groups: Iterable[Dict], path: str) -> None:
    """Save group information to a CSV file."""
    fieldnames = ["id", "title", "username", "participants", "description", "matched_keyword"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for g in groups:
            writer.writerow({key: g.get(key, "") for key in fieldnames})
