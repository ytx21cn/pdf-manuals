from typing import Dict, List
import csv


from utils.sources_data_struct import SourceKeys


class CSVReader:

    field_names = [v.value for v in SourceKeys.__members__.values()]

    @staticmethod
    def read_csv(csv_file: str):
        with open(csv_file) as csv_obj:
            reader = csv.DictReader(csv_obj, fieldnames=CSVReader.field_names)
            data: List[Dict] = list(reader)
        return data
