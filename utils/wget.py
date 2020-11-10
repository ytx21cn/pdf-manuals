import subprocess as sp
import os
from os.path import join

from utils.CSVReader import CSVReader
from utils.sources_data_struct import pdf_base_dir, SourceKeys


class Wget:

    wget = 'wget'

    @staticmethod
    def download_newer_only(url: str):
        sp.run([Wget.wget, '-N', url])

    @staticmethod
    def download_all_if_newer(sources_csv: str):

        start_dir = os.getcwd()

        try:
            data = CSVReader.read_csv(sources_csv)
            for row in data:
                # get information for download
                category: str = row[SourceKeys.CATEGORY.value]
                filename: str = row[SourceKeys.FILENAME.value]
                url: str = row[SourceKeys.URL.value]
                assert url.endswith(filename)

                # make category directory
                target_dir = join(pdf_base_dir, category)
                os.makedirs(target_dir, exist_ok=True)

                # download pdf manual
                os.chdir(target_dir)
                Wget.download_newer_only(url)
        finally:
            os.chdir(start_dir)
