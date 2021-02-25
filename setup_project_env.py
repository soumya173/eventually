# coding: utf-8

import sqlite3
import os
import sys
import shutil
import subprocess
import setup_db

def main():
    status = setup_db.main()
    if status != 0:
        print("Failed to setup database. Exiting")
        return 1
    python_bin = sys.executable
    out = subprocess.run([python_bin, 'api/setup.py', 'install'])
    print(out.stdout)
    print(out.stderr)
    if out.returncode != 0:
        print(out.stdout)
        print(out.stderr)
        print("Failed in installing dependancies")
        return 1
    print("Everything went well, your project is setup now")
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
