from enum import unique, Enum
from os.path import abspath, dirname


pdf_base_dir = abspath(f'{dirname(__file__)}/../pdf')


@unique
class SourceKeys(Enum):
    CATEGORY = 'Category'
    FILENAME = 'Filename'
    URL = 'URL'
