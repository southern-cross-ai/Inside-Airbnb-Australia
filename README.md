# Inside Airbnb Australia

## Overview
**Keywords**: Australia; Airbnb; Review

[Inside Airbnb](https://insideairbnb.com/) is a mission driven project that provides data and advocacy about Airbnb's impact on residential communities, aims to work towards a vision where communities are empowered with data and information to understand, decide and control the role of renting residential homes to tourists.


## Data Source
The original data is downloaded from [Inside Airbnb](https://insideairbnb.com/) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).  Please refer to [Data Policies - Inside Airbnb](https://insideairbnb.com/data-policies/) for more details.

This repo only stores `listings.csv[.gz]` and `reviews.csv[.gz]` data from Australia.
For data of other other locations, please visit [Get the data](https://insideairbnb.com/get-the-data/).



## Data Structure
The dataset under `InsideAirbnbAustralia` contains detailed listings and reviews data from the following 11 locations in Australia:
- Barossa Valley, South Australia
- Barwon South West, Vic, Victoria
- Brisbane, Queensland
- Melbourne, Victoria
- Mid North Coast, New South Wales
- Mornington Peninsula, Victoria
- Northern Rivers, New South Wales
- Sunshine Coast, Queensland
- Sydney, New South Wales
- Tasmania, Tasmania
- Western Australia, Western Australia

Each location has a separate directory with its name, e.g., `melbourne` and `sunshine-coast`.

Inside each location's directory, there are 2 subdirectories `gz` and `csv`, where `csv` contains the unzipped CSV files from their corresponding GZ files in `gz`.

Naming convention:
- `[location]_[date]_listings.csv[.gz]` contains detailed Airbnb listing data from `[location]` recorded every approximate 90 days;
- `[location]_[date]_reviews.csv[.gz]` contains detailed Airbnb review data from `[location]` recorded every approximate 90 days.

Notice that the `[date]` is used to build URLs to retrieve and download the data, doesn't necessarily represent the date of the data.

For more information about the data, please refer to [Get the data - Inside Airbnb](https://insideairbnb.com/get-the-data/).

## Download

We suggest you to walk through `utils/download.ipynb` notebook to explore how we build URLs to request and download the data.

You can also use `utils/download.py` to download the data directly in your terminal.
```bash
$ python utils/download.py --help  

usage: download.py [-h] [-s START_DATE] [-e END_DATE] -l LOCATIONS [LOCATIONS ...] [-r SAVE_ROOT]

Download Inside Airbnb data from Australia.

options:
  -h, --help            Show all help messages.
  -s START_DATE, --start_date START_DATE
                        Define the start date of the time range (YYY-MM-DD).
                        Default date is set to the date when Airbnb launched in Australia.
  -e END_DATE, --end_date END_DATE
                        Define the end date of the time range (YYYY-MM-DD).
                        Default date is set to the current date, i.e., today.
  -l LOCATIONS [LOCATIONS ...], --locations LOCATIONS [LOCATIONS ...]
                        Define the locations you want to download.
                        The possible locations are:
                        - 'sa/barossa-valley'
                        - 'vic/barwon-south-west-vic'
                        - 'qld/brisbane'
                        - 'vic/melbourne'
                        - 'nsw/mid-north-coast'
                        - 'vic/mornington-peninsula'
                        - 'nsw/northern-rivers'
                        - 'qld/sunshine-coast'
                        - 'nsw/sydney'
                        - 'tas/tasmania'
                        - 'wa/western-australia'
                        Use 'all' to download from all locations.
  -r SAVE_ROOT, --save_root SAVE_ROOT
                        The root path you want to save your data to.
                        Default root path is 'Inside-Airbnb-Australia'.

```


## License
This repository is licensed under [MIT](https://opensource.org/license/mit).