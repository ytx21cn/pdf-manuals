import shutil
from utils import pdf_base_dir


def main():
    shutil.rmtree(pdf_base_dir)


if __name__ == '__main__':
    main()