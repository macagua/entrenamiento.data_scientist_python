""" SQLite database functions """

import logging
import os
import sqlite3


def create_connection(path):
    """Create a database connection to a SQLite database

    Args:
        path (str): The full path used to read the database

    Returns:
        db_connection (Connection): SQLite database connection representation
    """

    db_connection = None
    if os.path.exists(path):
        try:
            db_connection = sqlite3.connect(path)
            logging.info(
                f"Connection to database '{os.path.basename(path)}' was successful!"
            )
        except sqlite3.ProgrammingError as e:
            print(f"ERROR: A programming error has occurred: '{e}'!")
        except sqlite3.OperationalError as e:
            print(f"ERROR: The following occurred: '{e}'")
        # finally:
        #     if db_connection:
        #         db_connection.close()
        #         logging.info("The database connection was closed successfully!")
    else:
        try:
            db_connection = sqlite3.connect(path)
            logging.info(
                f"Database creation '{os.path.basename(path)}' was successful!"
            )
            logging.info(
                f"Connection to database '{os.path.basename(path)}' was established successfully!"
            )
        except sqlite3.ProgrammingError as e:
            print(f"ERROR: A programming error has occurred: '{e}'!")
        except sqlite3.OperationalError as e:
            print(f"ERROR: The following occurred: '{e}'")
        # finally:
        #     if db_connection:
        #         db_connection.close()
        #         logging.info("The database connection was closed successfully!")

    return db_connection


def create_table(db_connection, sql_script):
    """Create Database table

    Args:
        db_connection (Connection): SQLite database connection representation
        sql_script (str): SQL script to execute
    """

    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_script)
        db_connection.commit()
        logging.info("The table was created successfully!")
    except sqlite3.Error as error:
        logging.error(f"Table creation failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info(
                "The cursor for create database table was closed successfully!"
            )
    #     if db_connection:
    #         db_connection.close()
    #         logging.info("The database connection was closed successfully!")
