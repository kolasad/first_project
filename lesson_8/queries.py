SQLITE_VERSION_QUERY = 'select sqlite_version()'

CREATE_WORKERS_TABLE = """
CREATE TABLE workers (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    salary REAL NOT NULL,
    level INTEGER,
    gender VARCHAR(20)
);
"""

CREATE_EQUIPMENT_TABLE = """
CREATE TABLE IF NOT EXISTS equipment (
    id INTEGER PRIMARY KEY,
    worker_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    FOREIGN KEY (worker_id) REFERENCES workers (id)
);
"""

# insert into workers table
INSERT_WORKERS = """
INSERT INTO workers (first_name, last_name, salary, level, gender)
VALUES('{}', '{}', {}, {}, '{}');
"""

# select all values fro workers table
SELECT_WORKERS = """
SELECT * FROM workers;
"""

# select first and last name
SELECT_NAMES = """
SELECT first_name, last_name FROM workers;
"""

# count workers
COUNT_WORKERS = """
SELECT COUNT(*) FROM workers;
"""

# get salary average per seniority level
SALARY_AVG_PER_LEVEL = """
SELECT AVG(salary), level FROM workers GROUP BY level;
"""

SELECT_WORKERS_WITH_EQUIPMENT = """
SELECT * FROM workers
LEFT JOIN equipment
ON workers.id = equipment.worker_id;
"""

SELECT_USERS_WITH_EQUIPMENT_COUNT = """
SELECT w.id, w.first_name, w.last_name, COUNT(e.id)
FROM workers w
LEFT JOIN equipment e
ON w.id = e.worker_id
GROUP BY w.id;
"""

SELECT_USER_EQUIPMENT = """
SELECT * FROM equipment WHERE worker_id = {};
"""

# Remove table and data contained by it
DROP_WORKERS = """
DROP TABLE workers;
"""

# Removes all data from workers table
TRUNCATE_WORKERS = """
DELETE FROM workers;
"""
