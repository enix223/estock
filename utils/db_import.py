from mysql import Mysql

class db(object):

    def __init__(self):
        self.db = Mysql(host='172.29.138.91', db='stock', user='root', password='enixyuabc@123')
        self.db.connect()

    def insert(self, table, columns, data):        
        sql = 'INSERT INTO %s(%s) VALUES(%s)' % (table, ",".join(columns), ",".join(self.to_str(data)))
        return self.db.execute(sql)

    def close(self):
        self.db.commit()
        self.db.close()

    def to_str(self, arr):
        a = arr[:]
        for i in range(len(arr)):
            a[i] = "'%s'" % arr[i]
        return a
    
    
