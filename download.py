
import os
import datetime
from Drive import Drive


def main():
    if 'download_history.csv' not in os.listdir():
        open('download_history.csv', 'a').close()
        with open('download_history.csv', 'a') as f:
            f.write('DateTime,SuccessfulDownload\n')

    x = Drive()
    download_status = x.download('journal.jl')

    with open('download_history.csv', 'a') as f:
        f.write(f'{datetime.datetime.now()},{download_status}\n')


if __name__ == '__main__':
    main()

