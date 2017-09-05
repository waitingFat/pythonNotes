import datetime


def getDate():
    today = datetime.date.today()
    print today
    isoformat = today.isoformat()
    print isoformat
    zfill = isoformat.zfill(11)
    print zfill

if __name__ == '__main__':
    getDate()