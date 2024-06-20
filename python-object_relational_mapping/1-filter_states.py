#!/usr/bin/python3
"""Lists all states in a database"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """List states with letter N"""

    try:
        conn = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=username,
                               password=password,
                               db=database_name)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connectig to MySQL or execuiting query: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 0-selsct_states.py username password database")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)
