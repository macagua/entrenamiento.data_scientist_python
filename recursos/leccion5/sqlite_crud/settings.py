""" Simple Blog Settings """

import os
from dotenv import load_dotenv

### DotENV #################################################################
load_dotenv()

# Name of the database to which to connect.
DB_FILE = os.getenv("DB_FILE")

# Application title name
APP_TITLE = os.getenv("APP_TITLE")

# Number of range of blog posts to create
ARTICLES_RANGE = int(os.getenv("ARTICLES_RANGE"))

# Color Palette: #3C6255 #61876E #A6BB8D #EAE7B1
# Color Hunt https://colorhunt.co/palette/3c625561876ea6bb8deae7b1

# Primary accent color for interactive elements.
# using by Blog Entry Post Information Sheet
PRIMARY_COLOR = os.getenv("PRIMARY_COLOR")

# Background color for the main content area.
BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR")

# Background color used for the sidebar and most interactive widgets.
# using by Blog Header Main Title Color
SECONDARY_BACKGROUND_COLOR = os.getenv("SECONDARY_BACKGROUND_COLOR")

# Color used for almost all text.
# using by Blog Header Main Title Background Color
TEXT_COLOR = os.getenv("TEXT_COLOR")

### SQLite3 ################################################################

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep

# DB File
if "DB_PATH" in globals() and "DB_FILE" in globals():
    DB = DB_PATH + DB_FILE

# Script CREATE TABLE SQL a usar al crear la tabla
TABLE_SQL_SCRIPTS = """
    CREATE TABLE IF NOT EXISTS articles (
        author TEXT NOT NULL,
        title TEXT NOT NULL UNIQUE,
        content TEXT NOT NULL,
        post_date DATE NOT NULL
    );
"""

# Script INSERT SQL a usar al ingresar datos
INSERT_SQL_SCRIPTS = """
    INSERT INTO articles
        (author, title, content, post_date)
    VALUES (?, ?, ?, ?);
"""

# SELECT SQL script to use when querying data
SELECT_SQL_SCRIPTS = """SELECT * FROM articles;"""

# SELECT DISTINCT SQL script to use when querying data by title
SELECT_DISTINCT_SQL_SCRIPTS = """SELECT DISTINCT title FROM articles;"""
