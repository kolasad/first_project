import sqlite3

from lesson_8.queries import SQLITE_VERSION_QUERY, CREATE_WORKERS_TABLE, INSERT_WORKERS, SELECT_WORKERS, SELECT_NAMES, \
    COUNT_WORKERS, SALARY_AVG_PER_LEVEL, CREATE_EQUIPMENT_TABLE, SELECT_WORKERS_WITH_EQUIPMENT, \
    SELECT_USERS_WITH_EQUIPMENT_COUNT, SELECT_USER_EQUIPMENT, DROP_WORKERS, TRUNCATE_WORKERS

DATABASE_FILE = 'workers.db'


def execute_fetch_query(query):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        print('Connection made')
        cursor.execute(query)
        record = cursor.fetchall()
        print(f'Fetched all: {record}')
        cursor.close()
    except sqlite3.Error as e:
        print(f'Error while connecting to database: {e}')
    finally:
        if conn:
            conn.close()
            print('Connection closed')


execute_fetch_query(SQLITE_VERSION_QUERY)

execute_fetch_query(CREATE_WORKERS_TABLE)

# execute query creating new worker
conn = None
try:
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    print('Connection made')
    cursor.execute(INSERT_WORKERS.format(
        'Magda', 'Nowa', 5688, 2, 'female'
    ))
    conn.commit()
    cursor.close()
except sqlite3.Error as e:
    print(f'Error while connecting to database: {e}')
finally:
    if conn:
        conn.close()
        print('Connection closed')


execute_fetch_query(SELECT_WORKERS)
execute_fetch_query(SELECT_NAMES)
execute_fetch_query(COUNT_WORKERS)
execute_fetch_query(SALARY_AVG_PER_LEVEL)

conn = sqlite3.connect(DATABASE_FILE)
with conn:  # context manager
    cursor = conn.cursor()
    cursor.execute(SALARY_AVG_PER_LEVEL)
    record = cursor.fetchall()
    for row in record:
        print(row)


execute_fetch_query(CREATE_EQUIPMENT_TABLE)

conn = sqlite3.connect(DATABASE_FILE)
with conn:  # context manager
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO equipment(worker_id, name) VALUES(2, 'monitor');"
    )
    conn.commit()
    cursor.execute('SELECT * FROM equipment;')
    print(cursor.fetchall())


conn = sqlite3.connect(DATABASE_FILE)
with conn:  # context manager
    cursor = conn.cursor()
    cursor.execute(SELECT_WORKERS_WITH_EQUIPMENT)
    print(cursor.fetchall())
    cursor.execute(SELECT_USERS_WITH_EQUIPMENT_COUNT)
    print(cursor.fetchall())


def get_user_equipment(user_id):
    with conn:
        cursor = conn.cursor()
        # cursor.execute(SELECT_USER_EQUIPMENT.format(user_id))
        cursor.execute(f"SELECT * FROM equipment WHERE worker_id = {user_id} AND name = 'laptop';")
        return cursor.fetchall()


user_id = 2
user_equipment = get_user_equipment(user_id)
print(user_equipment)


conn = sqlite3.connect(DATABASE_FILE)
with conn:
    cursor = conn.cursor()
    # cursor.execute(SELECT_USER_EQUIPMENT.format(user_id))
    cursor.execute(f"SELECT * FROM workers;")
    print(cursor.fetchall())
    # cursor.execute(TRUNCATE_WORKERS)  # removes data from table
    cursor.execute(f"SELECT * FROM workers;")
    print(cursor.fetchall())
