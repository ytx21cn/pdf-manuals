import sys

from utils import Wget


def main():
    if len(sys.argv) < 2:
        print('ERROR: no sources csv specified', file=sys.stderr)
        print(f'Usage: {__file__} <sources.csv>', file=sys.stderr)
        exit(1)

    sources = sys.argv[1]
    Wget.download_all_if_newer(sources)


if __name__ == '__main__':
    main()