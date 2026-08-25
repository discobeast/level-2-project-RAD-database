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
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            name,
            code             TEXT    UNIQUE
                                    NOT NULL,
            last_device      TEXT    REFERENCES devices (id),
            last_device_date TEXT
        );
    """

    SEED_DATA = """
        INSERT INTO users (
                            id,
                            name,
                            code,
                            last_device,
                            last_device_date
                        )
                        VALUES (
                            1,
                            'Jesse',
                            'EF45A',
                            'RAD1234',
                            NULL
                        );

        INSERT INTO users (
                            id,
                            name,
                            code,
                            last_device,
                            last_device_date
                        )
                        VALUES (
                            2,
                            'Zander',
                            'EGQ3',
                            'RAD1861',
                            NULL
                        )
    """

class deviceTable:

    NAME = "users"

    SCHEMA = """
        CREATE TABLE devices (
            id                TEXT    PRIMARY KEY,
            model             TEXT,
            state             INTEGER,
            replaced_parts    TEXT,
            notes             TEXT,
            last_worked_on_by INTEGER REFERENCES users (id) 
        );
    """

    SEED_DATA = """
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD1234', 'Tobishia thinkpad', 1, 'wigga', 'Jesse: What the actual shit', 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD1861', 'Chat AI', 3, 'RAM', 'Zander: I am gay, Jesse: Heh', 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14022', 'HP Elitebook x360 1030 g4', 4, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14023', 'HP Elitebook x360 1030 g4', 4, NULL, NULL, 2);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14024', 'HP Elitebook x360 1030 g4', 2, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14025', 'HP Elitebook x360 1030 g4', 0, NULL, NULL, 2);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14027', 'HP Elitebook x360 1030 g4', 3, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14029', 'HP Elitebook x360 1030 g4', 2, NULL, NULL, 2);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14030', 'HP Elitebook x360 1030 g4', 4, NULL, NULL, 2);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14038', 'HP Elitebook x360 1030 g4', 5, NULL, NULL, 2);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14053', 'HP Elitebook x360 1030 g4', 5, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14057', 'HP Elitebook x360 1030 g4', 4, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14058', 'HP Elitebook x360 1030 g4', 5, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14101', 'HP Elitebook x360 1030 g4', 1, NULL, NULL, 2);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14116', 'HP Elitebook x360 1030 g4', 1, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14117', 'HP Elitebook x360 1030 g4', 1, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD14118', 'HP Elitebook x360 1030 g4', 0, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD20253', 'Toshiba Portege X3OL-J', 5, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD20254', 'Toshiba Portege X3OL-J', 5, NULL, NULL, 2);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD20255', 'Toshiba Portege X3OL-J', 0, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD20256', 'Toshiba Portege X3OL-J', 3, NULL, NULL, 1);
    INSERT INTO devices (id, model, state, replaced_parts, notes, last_worked_on_by) VALUES ('RAD20257', 'Toshiba Portege X3OT-E', 5, NULL, NULL, 1);
    """

class wordDoneTable:

    NAME = "work_done"

    SCHEMA = """

    """

    SEED_DATA = """

    """

class statusTable:

    NAME = "status"

    SCHEMA = """

    """

    SEED_DATA = """
    
    """

class checksTable:

    NAME = "checks"

    SCHEMA = """

    """

    SEED_DATA = """
    
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
    deviceTable
]

