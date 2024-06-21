#!/usr/bin/python3
"""task 5 orm"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong Usage")

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           password=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON states.id = cities.state_id WHERE state.name = %s\
            ORDER BY cities.id ASC"
    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    conn.close()
