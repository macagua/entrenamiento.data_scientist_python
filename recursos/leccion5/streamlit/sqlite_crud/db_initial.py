import logging
import os
import sqlite3
from faker import Faker
from db import create_connection, create_table
from settings import (
    ARTICLES_RANGE,
    DB,
    INSERT_SQL_SCRIPTS,
    TABLE_SQL_SCRIPTS,
)

# Logging App
logging.basicConfig(level=logging.INFO)

# Faker
fake = Faker()

# Functions
def generate_data_fake(faker):
    """Generate data fake for articles table

    Args:
        faker (faker.proxy.Faker): Faker proxy object

    Returns:
        list: Data faker records list
    """
    article, articles = (), []
    for _ in range(ARTICLES_RANGE):
        article = (
            faker.name(),
            faker.sentence(),
            str(faker.texts())
            .replace("['", "")
            .replace("']", "")
            .replace("\\n", "<br/>")
            .replace(".', '", ". "),
            faker.past_date(),
        )
        articles.append(article)
    return articles


def add_data_initial(db_connection, sql_script, sql_script_values):
    """Add data initial of Blog entry post

    Args:
        db_connection (Connection): SQLite database connection representation
        sql_script (str): SQL script to execute
        sql_script_values (list): Data faker records list

    Returns:
        list: Records list
    """

    try:
        cursor = db_connection.cursor()
        cursor.executemany(sql_script, sql_script_values)
        db_connection.commit()
        logging.info(
            "¡{} record(s) was(were) successfully added to the table!".format(
                cursor.rowcount
            )
        )
    except sqlite3.Error as error:
        logging.error(f"The add of record(s) in the table failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info(
                "The cursor for data initial of blog entry posts was closed successfully!"
            )
        if db_connection:
            db_connection.close()
            logging.info(
                "Disconnect to database 'simple_blog.sqlite3' was closed successfully!"
            )


if __name__ == "__main__":

    connection = create_connection(DB)
    if connection is not None:
        create_table(connection, TABLE_SQL_SCRIPTS)
        add_data_initial(connection, INSERT_SQL_SCRIPTS, generate_data_fake(fake))
    else:
        logging.error(f"ERROR! cannot create the database connection to the {DB} file.")
