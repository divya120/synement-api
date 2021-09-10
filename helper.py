import datetime
import pytz

data_keys = [
    'id',
    'subject',
    'type',
    'date_due'
]


def get_date_today():
    return datetime.datetime.now(
        pytz.timezone('Asia/Kolkata')).strftime('%d-%b-%G')


def get_date_tomorrow():
    tomorrow = datetime.datetime.now(
        pytz.timezone('Asia/Kolkata')) + datetime.timedelta(days=1)
    return tomorrow.strftime('%d-%b-%G')


def get_row_with_keys(row):
    return dict(zip(data_keys, row))
