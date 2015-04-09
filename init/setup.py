import sqlite3
import os
import sys

_ESTOCK_DB = '../estock.s3db'

if os.path.isfile(_ESTOCK_DB):
    con = sqlite3.connect(_ESTOCK_DB)
    cur = con.cursor()

    # Create the tables
    cur.execute("""CREATE TABLE [new_stock_odd_success_rate] (
        [plate] varchar(3)  NULL,
        [stock_code] varchar(6)  NULL PRIMARY KEY,
        [apply_code] varchar(6)  NULL,
        [stock_name] nvarchar(20) null,
        [price] real  NULL,
        [apply_date] varchar(10)  NULL,
        [odd_success_rate] real  NULL
        )""")
    cur.commit()

    # config table
    cur.execute("""CREATE TABLE [config] (
        [key] VARCHAR(50)  UNIQUE NULL PRIMARY KEY,
        [value] varchar(100)  NULL
        )""")
    cur.commit()

