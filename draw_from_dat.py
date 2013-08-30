from struct import *
from utils.db_import import db
from datetime import datetime

class Stock:
    kv = {}

    def __str__(self):
        return self.kv.__str__()

def draw(filePath):

    t1 = datetime.now()
    s = Stock()
    f = open(filePath, 'rb')
    mdb = db()
    while True:
        data = f.read(32)
        if data:
            s.kv['date'] = unpack('L', data[0:4])[0]
            s.kv['open'] = unpack('L', data[4:8])[0]/100.0
            s.kv['high'] = unpack('L', data[8:12])[0]/100.0
            s.kv['low'] = unpack('L', data[12:16])[0]/100.0
            s.kv['close'] = unpack('L', data[16:20])[0]/100.0
            s.kv['deal'] = unpack('f', data[20:24])[0]
            s.kv['vol'] = unpack('L', data[24:28])[0]
            #s.kv['reverse'] = unpack('L', data[28:32])[0]
            mdb.insertSQL('stock_002402', s.kv)
            #print(s)
        else:
            break

    mdb.close()
    f.close()
    t2 = datetime.now()
    print("Elapse time: %f" % (t2 - t1).total_seconds())

if __name__ == '__main__':
    p = "data/sz002402.day"
    draw(p)

