"""CSV invoice import."""
import csv

def read_lines(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))
