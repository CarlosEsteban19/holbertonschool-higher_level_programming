#!/usr/bin/python3
"""some imports to help"""
import sys
import MySQLdb


def list_states(username, password, db_name):
    """list all states from database table"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=db_name
        )  # Connection

        cursor = db.cursor()  # Object that interacts with database
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(username, password, db_name)
