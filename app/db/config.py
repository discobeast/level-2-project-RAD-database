#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class userTable:

    NAME = "users"

    SCHEMA = """
        CREATE TABLE users (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT    UNIQUE,
            name TEXT
        );
    """

    SEED_DATA = """
        INSERT INTO users (id, code, name) 
            VALUES (1, 'ALE2J', 'Zander'),
            (2, 'KWJ15', 'Ellis'),
            (3, 'U4H34', 'Jesse'),
            (4, 'IWGR1', 'Zach')
    """

class deviceTable:

    NAME = "devices"

    SCHEMA = """
        CREATE TABLE devices (
            id    TEXT PRIMARY KEY,
            model TEXT
        );
    """

    SEED_DATA = """
        INSERT INTO devices (id, model) 
            VALUES ('RAD14022', 'HP Elitebook x360 1030 g4'),
            ('RAD14023', 'HP Elitebook x360 1030 g4'),
            ('RAD14024', 'HP Elitebook x360 1030 g4'),
            ('RAD14025', 'HP Elitebook x360 1030 g4'),
            ('RAD14027', 'HP Elitebook x360 1030 g4'),
            ('RAD14029', 'HP Elitebook x360 1030 g4'),
            ('RAD14030', 'HP Elitebook x360 1030 g4'),
            ('RAD14038', 'HP Elitebook x360 1030 g4'),
            ('RAD14053', 'HP Elitebook x360 1030 g4'),
            ('RAD14057', 'HP Elitebook x360 1030 g4'),
            ('RAD14058', 'HP Elitebook x360 1030 g4'),
            ('RAD14101', 'HP Elitebook x360 1030 g4'),
            ('RAD14116', 'HP Elitebook x360 1030 g4'),
            ('RAD14117', 'HP Elitebook x360 1030 g4'),
            ('RAD14118', 'HP Elitebook x360 1030 g4'),
            ('RAD20253', 'Toshiba Portege X3OL-J'),
            ('RAD20254', 'Toshiba Portege X3OL-J'),
            ('RAD20255', 'Toshiba Portege X3OL-J'),
            ('RAD20256', 'Toshiba Portege X3OL-J'),
            ('RAD20257', 'Toshiba Portege X3OT-E'),
            ('RAD20258', 'Toshiba Portege X3OT-E'),
            ('RAD20259', 'Toshiba Portege X3OT-E'),
            ('RAD20260', 'Toshiba Portege X3OT-E'),
            ('RAD20261', 'Toshiba Portege X3OT-E'),
            ('RAD20262', 'Toshiba Portege X3OT-E'),
            ('RAD20263', 'Toshiba Portege X3OL-J'),
            ('RAD20264', 'Toshiba Portege X3OT-E'),
            ('RAD20265', 'Toshiba Portege X3OT-E'),
            ('RAD20266', 'Toshiba Portege X3OT-E'),
            ('RAD20267', 'Toshiba Portege X3OT-E'),
            ('RAD21320', 'Dell Precision 5540'),
            ('RAD21318', 'Dell Precision 5540'),
            ('RAD21321', 'Dell Precision 5540'),
            ('RAD21315', 'Dell Precision 5540'),
            ('RAD21316', 'Dell Precision 5540'),
            ('RAD21319', 'Dell Precision 5540'),
            ('RAD21309', 'Dell Latitude 7210'),
            ('RAD21310', 'Dell Latitude 7210'),
            ('RAD21311', 'Dell Latitude 7210'),
            ('RAD21462', 'Dell Latitude 7210')
    """

class workDoneTable:

    NAME = "work_done"

    SCHEMA = """
        CREATE TABLE work_done (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            computer  TEXT    REFERENCES computers (id),
            user      INTEGER REFERENCES users (id),
            notes     TEXT,
            timestamp TEXT
        );
    """

    SEED_DATA = """
        INSERT INTO work_done (id, computer, user, notes, timestamp) 
            VALUES (1, 'RAD14025', 2, NULL, '9:00'),
             (2, 'RAD14053', 1, NULL, '5:21'),
             (3, 'RAD14022', 2, NULL, '00:30')
    """

class statusTable:

    NAME = "status"

    SCHEMA = """
        CREATE TABLE status (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            computer TEXT    REFERENCES computers (id),
            user     INTEGER REFERENCES users (id),
            outcome  INTEGER NOT NULL,
            notes    TEXT,
            check_id INTEGER REFERENCES checks (id) 
        );
    """

    SEED_DATA = """
        INSERT INTO status (id, computer, user, outcome, notes, check_id) 
            VALUES (1, 'RAD14022', 2, 1, 'Works', 1),
             (2, 'RAD14022', 2, 0, 'No battery', 5)
    """

class checksTable:
    NAME = "checks"

    SCHEMA = """
        CREATE TABLE checks (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
    """

    SEED_DATA = """
        INSERT INTO checks (id, name) 
        VALUES (1, 'Physical damage'),
         (2, 'Charges with charger'),
         (3, 'OS'),
         (4, 'BIOS accessable'),
         (5, 'Boots on battery'),
         (6, 'Boots with charger')
    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    userTable,
    deviceTable,
    checksTable,
    statusTable,
    workDoneTable
]

