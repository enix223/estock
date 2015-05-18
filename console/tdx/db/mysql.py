'''
Created on May 17, 2012

@author: anduril
'''
import sys
import MySQLdb as mysql
from base import Base

class Mysql(Base):
    
    conn = None
    
    def __init__(self, host, db, user, password):
        self.host = host
        self.db = db
        self.user = user
        self.password = password        
        super(Mysql, self).__init__()
        self.logger.info("Initialization Completed.")
        
    def connect(self):
        try :             
            self.conn = mysql.connect(self.host, self.user, self.password, self.db)
            self.cur = self.conn.cursor(mysql.cursors.DictCursor)
            self.logger.info("Created a new connection to the database.")
        except mysql.Error, e:
            self.logger.exception(e)
        
    def executeQuery(self, query):
        self.logger.info("Executing query -- %s ", query)
        try :
            self.cur.execute(query)
            numrows = int(self.cur.rowcount)
            return numrows
        except mysql.Error, e:
            self.logger.exception(e)
    
    def fetchOne(self):
        return self.cur.fetchone()
    
    def fetchAll(self):
        self.logger.info("Fetching All rows")
        return self.cur.fetchall()
    
    def fetchColumnHeaders(self):
        self.logger.info("Fetching Column Descriptor")
        return self.cur.description
    
    def commit(self):
        self.logger.info("Committing to database.")
        self.conn.commit()
        return
    
    def rollback(self):
        self.logger.info("Rolling back")
        self.conn.rollback()
        return
    
    def close(self):
        self.logger.info("Closing connection")
        self.cur.close()
        self.conn.close()   

    def execute(self, sql):
        self.logger.info("Executing sql -- %s ", sql)
        try :
            self.cur.execute(sql)
            numrows = int(self.cur.rowcount)
            return numrows
        except mysql.Error, e:
            self.logger.exception(e)
