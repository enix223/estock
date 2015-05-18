from mysql import Mysql

class MySQLDB(object):

    def __init__(self, host, db, user, password):
        self.connection = None
        self.host, self.db, self.user, self.password = host, db, user, password
        self.connect()

    def connect(self):
        if not self.connection:            
            self.connection = Mysql(host=self.host, db=self.db, user=self.user, password=self.password)
            self.connection.connect()
        return self.connection

    def insertSQL(self, table, columnValueDict):
        sql = 'INSERT INTO %s(%s) VALUES(%s)' % (table, ",".join(columnValueDict.keys()), ",".join(self.to_str(columnValueDict.values())))
        return self.connection.execute(sql)
    
    def insert(self, table, columns, data):        
        sql = 'INSERT INTO %s(%s) VALUES(%s)' % (table, ",".join(columns), ",".join(self.to_str(data)))
        return self.connection.execute(sql)

    def insertSQLIgnore(self, table, columnValueDict):
        sql = 'INSERT IGNORE INTO %s(%s) VALUES(%s)' % (table, ",".join(columnValueDict.keys()), ",".join(self.to_str(columnValueDict.values())))
        return self.connection.execute(sql)

    def execute(self, sql):
        return self.connection.execute(sql)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.commit()
        self.connection.close()
        self.connection = None

    def to_str(self, arr):
        a = arr[:]
        for i in range(len(arr)):
            a[i] = "'%s'" % arr[i]
        return a
    
    
