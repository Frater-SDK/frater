import datetime


def now():
    return datetime.datetime.now().isoformat()


def utcnow():
    return datetime.datetime.utcnow().isoformat()
