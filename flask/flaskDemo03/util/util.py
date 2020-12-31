import datetime


def file_strtype(filename):
    return filename.filename.split('.')[-1]


def generate_time():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')