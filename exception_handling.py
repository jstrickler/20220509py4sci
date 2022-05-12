import sqlite3
import logging

logging.basicConfig(filename="demo.log")

file_name = 'wombats.txt'

try:
    with open(file_name) as wombats_in:
        pass
except (FileNotFoundError, PermissionError) as err:
    print(err)  # ???
    logging.warning(err)  # ???


items = ['cat', 'bird', 'dog', 'cow', 'moose']
try:
    print(items[99])
except IndexError as err:
    logging.error(err)

values = 5, 8, 0.0, "8.6", None, 14, 'abc', 2, 6

for v in values:
    try:
        num = float(v)
        result = 27 / num
    except ZeroDivisionError as err:
        logging.warning(err)
    except (TypeError, ValueError) as err:
        print(err)
    except Exception as err:
        logging.error(err)
    else:  # there were no exceptions
        print(result)

conn = None
try:
    conn = sqlite3.connect('mydata.db')
except sqlite3.DatabaseError as err:
    logging.error(err)
    print("So long and thanks for all the fish")
    exit()
else:
    cursor = conn.cursor()
    cursor.execute("select * from animals")
finally:
    if conn is not None:
        cursor.close()
        conn.close()


print("ALL DONE")
