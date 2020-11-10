from typing import Dict, List

import csv


class CSVReader:

    CATEGORY = 'Category'
    FILENAME = 'Filename'
    URL = 'URL'
    field_names = [CATEGORY, FILENAME, URL]

    @staticmethod
    def read_csv(csv_file: str):
        with open(csv_file) as csv_obj:
            reader = csv.DictReader(csv_obj, fieldnames=CSVReader.field_names)
            data: List[Dict] = list(reader)[1:]
        return data
