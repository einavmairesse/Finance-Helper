from datetime import datetime


def str_to_date(date_as_string):
    try:
        date = datetime.strptime(date_as_string, '%m/%Y')
    except ValueError:
        raise ValueError(f'Could not parse date from string: {date_as_string}')

    return date
