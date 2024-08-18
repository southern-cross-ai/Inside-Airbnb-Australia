import argparse
import gzip
import os
import shutil
from datetime import datetime

import requests
from dateutil.relativedelta import relativedelta

# DO NOT CHANGE
prefix = 'https://data.insideairbnb.com/australia'
locations = ['sa/barossa-valley',
             'vic/barwon-south-west',
             'qld/brisbane',
             'vic/melbourne',
             'nsw/mid-north-coast',
             'vic/mornington-peninsula',
             'nsw/northern-rivers',
             'qld/sunshine-coast',
             'nsw/sydney',
             'tas/tasmania',
             'wa/western-australia']
affix_listings = 'data/listings.csv.gz'
affix_reviews = 'data/reviews.csv.gz'
format = '.csv.gz'


def time_range(start='2012-08-01', end='2024-08-17', day_interval=1):
    # set the start_date to the day when Airbnb launched in Australia
    y, m, d = start.split('-')
    start_date = datetime(int(y), int(m), int(d))
    if end == 'today':
        end_date = datetime.today()
    else:
        y, m, d = end.split('-')
        # last time updated on 2024-08-17
        end_date = datetime(int(y), int(m), int(d))
    # calculate all the dates between start_date and end_date
    dates = []
    while start_date <= end_date:
        dates.append(start_date.strftime('%Y-%m-%d'))
        start_date += relativedelta(days=day_interval)  # set interval to 1 day
    return dates


def download(locations, dates, save_root):
    # create the directory if it doesn't exist
    if not os.path.exists(save_root):
        os.makedirs(save_root, exist_ok=True)
    # start to retrieve the data in the time range from all locations
    for location in locations:
        for date in dates:
            for affix in [affix_listings, affix_reviews]:
                url = f'{prefix}/{location}/{date}/{affix}'
                print(url)
                res = requests.get(url)
                # download .csv.gz files
                name = f'{location.split(
                    '/')[-1]}_{date}_{affix.split('/')[-1]}'
                with open(os.path.join(save_root, name), 'wb') as f:
                    f.write(res.content)
                print(f"Downloaded {name}")
                # try to unzip, delete invalid file if failed
                try:
                    with gzip.open(os.path.join(save_root, name), 'rb') as f_in, \
                            open(os.path.join(save_root, name[:-3]), 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    print(f"Unzipped to {name[:-3]}")
                except gzip.BadGzipFile:
                    print(f"Removed invalid {name} and {name[:-3]}")
                    os.remove(os.path.join(save_root, name))
                    os.remove(os.path.join(save_root, name[:-3]))


def define_parser():
    parser = argparse.ArgumentParser(description="Download Inside Airbnb data from Australia.",
                                     formatter_class=argparse.RawTextHelpFormatter, add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help="Show all help messages.")
    parser.add_argument('-s', '--start_date', type=str, default='2012-08-01',
                        help="Define the start date of the time range (YYY-MM-DD).\n"
                        "Default date is set to the date when Airbnb launched in Australia.")
    parser.add_argument('-e', '--end_date', type=str, default='today',
                        help="Define the end date of the time range (YYYY-MM-DD).\n"
                        "Default date is set to the current date, i.e., today.")
    parser.add_argument('-l', '--locations', nargs='+', type=str, required=True,
                        help="Define the locations you want to download.\n"
                        "The possible locations are:\n"
                        "- 'sa/barossa-valley'\n"
                        "- 'vic/barwon-south-west-vic'\n"
                        "- 'qld/brisbane'\n"
                        "- 'vic/melbourne'\n"
                        "- 'nsw/mid-north-coast'\n"
                        "- 'vic/mornington-peninsula'\n"
                        "- 'nsw/northern-rivers'\n"
                        "- 'qld/sunshine-coast'\n"
                        "- 'nsw/sydney'\n"
                        "- 'tas/tasmania'\n"
                        "- 'wa/western-australia'\n"
                        "Use 'all' to download from all locations.")
    parser.add_argument('-r', '--save_root', type=str, default='Inside-Airbnb-Australia',
                        help="The root path you want to save your data to.\n"
                        "Default root path is 'Inside-Airbnb-Australia'.")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = define_parser()
    dates = time_range(start=args.start_date, end=args.end_date)
    download(args.locations, dates, args.save_root)
