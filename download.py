from utils import CSVReader


def main():
    sources = 'sources.csv'

    data = CSVReader.read_csv(sources)
    print(data)


if __name__ == '__main__':
    main()