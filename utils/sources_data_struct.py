from enum import unique, Enum


@unique
class SourceKeys(Enum):
    CATEGORY = 'Category'
    FILENAME = 'Filename'
    URL = 'URL'
