# coding: utf-8

import sqlite3
import os
import sys
import shutil
db_file = 'database.db'
db_sql = 'dbschema.sql'

def main():
    if os.path.exists(db_file):
        os.remove(db_file)
    conn = sqlite3.connect(db_file)
    with open(db_sql) as fp:
        conn.executescript(fp.read())
    conn.commit()
    conn.close()

    target_db = os.path.join('api', 'swagger_server', 'database.db')
    if os.path.exists(target_db):
        os.remove(target_db)
    shutil.copy(db_file, target_db)

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
