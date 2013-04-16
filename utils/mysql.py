'''
Created on May 17, 2012

@author: anduril
'''
import sys
import MySQLdb as mysql
import logging
logging.basicConfig(filename='mysql.log',level=logging.ERROR)

class Mysql():
    
    conn = None
    
    def __init__(self, host, db, user, password):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        logging.info("Initialization Completed.")
        
    def connect(self):
        try :             
            self.conn = mysql.connect(self.host, self.user, self.password, self.db)
            self.cur = self.conn.cursor(mysql.cursors.DictCursor)
            logging.info("Created a new connection to the database.")
        except mysql.Error, e:
            logging.exception("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)  
        
    def executeQuery(self, query):
        logging.info("Executing query -- %s ", query)
        try :
            self.cur.execute(query)
            numrows = int(self.cur.rowcount)
            return numrows
        except mysql.Error, e:
            logging.exception("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
    
    def fetchOne(self):
        return self.cur.fetchone()
    
    def fetchAll(self):
        logging.info("Fetching All rows")
        return self.cur.fetchall()
    
    def fetchColumnHeaders(self):
        logging.info("Fetching Column Descriptor")
        return self.cur.description
    
    def commit(self):
        logging.info("Committing to database.")
        self.conn.commit()
        return
    
    def rollback(self):
        logging.info("Rolling back")
        self.conn.rollback()
        return
    
    def close(self):
        logging.info("Closing connection")
        self.cur.close()
        self.conn.close()   

    def execute(self, sql):
        logging.info("Executing sql -- %s ", sql)
        try :
            self.cur.execute(sql)
            numrows = int(self.cur.rowcount)
            return numrows
        except mysql.Error, e:
            logging.exception("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
