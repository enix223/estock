from mysql import Mysql

class db(object):

    def __init__(self):
        self.db = Mysql(host='172.29.138.91', db='stock', user='istock', password='enixyuabc')
        self.db.connect()


    def insertSQL(self, table, columnValueDict):
        sql = 'INSERT INTO %s(%s) VALUES(%s)' % (table, ",".join(columnValueDict.keys()), ",".join(self.to_str(columnValueDict.values())))
        return self.db.execute(sql)
    
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
    
    
