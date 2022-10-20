from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents"""
    with open(path) as file:
        reader_file = csv.DictReader(file)
        list = [row for row in reader_file]
        return list
