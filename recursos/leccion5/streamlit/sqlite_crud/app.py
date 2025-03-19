import datetime
import logging
import matplotlib as plt
import os
import pandas as pd
import sqlite3
import streamlit as st
from db import create_connection
from layouts import (
    BLOG_HEADER_HTML_TPL,
    ENTRY_DETAILS_HTML_TPL,
    ENTRY_CONTENT_MSG_HTML_TPL,
    HOME_ENTRIES_HTML_TPL,
    NOTFOUND_ENTRY_MSG_HTML_TPL,
    NOTFOUND_SEARCH_MSG_HTML_TPL,
)
from settings import (
    APP_TITLE,
    PRIMARY_COLOR,
    BACKGROUND_COLOR,
    SECONDARY_BACKGROUND_COLOR,
    TEXT_COLOR,
    DB,
    INSERT_SQL_SCRIPTS,
    SELECT_DISTINCT_SQL_SCRIPTS,
    SELECT_SQL_SCRIPTS,
)
from streamlit_quill import st_quill
from wordcloud import WordCloud

# Logging App
logging.basicConfig(level=logging.INFO)

# Streamlit
st.set_option("deprecation.showPyplotGlobalUse", False)
st.set_page_config(page_title=APP_TITLE, page_icon=":page_facing_up:", layout="wide")
st.markdown(
    """<style type="text/css">
    #MainMenu{visibility: hidden;}
    footer{visibility: hidden;}
    /*#root>div:nth-child(1)>div>div>div>div>section>div{padding-top: 0rem;}*/
    </style>""",
    unsafe_allow_html=True,
)

# Functions
def add_data(db_connection, sql_script, author, title, content, postdate):
    """Add a Blog entry

    Args:
        db_connection (Connection): SQLite database connection representation
        sql_script (str): SQL script to execute
        author (str): The Article author
        title (str): The Article title
        content (str): The Article body
        postdate (datetime): The Article post date
    """

    try:
        cursor = db_connection.cursor()
        cursor.execute(
            sql_script,
            (author, title, content, postdate),
        )
        db_connection.commit()
        logging.info(
            "¡{} record(s) was(were) successfully added to the table!".format(
                cursor.rowcount
            )
        )
    except sqlite3.Error as error:
        logging.error(f"Query for record(s) in table failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info("The cursor for add a Blog entry was closed successfully!")


def view_all_articles(db_connection, sql_script):
    """View all Blog Articles

    Args:
        db_connection (Connection): SQLite database connection representation
        sql_script (str): SQL script to execute

    Returns:
        list: Records list
    """

    records = []
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_script)
        records = cursor.fetchall()
        logging.info("The query to the table was successful!")
    except sqlite3.Error as error:
        logging.error(f"Query for record(s) in table failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info(
                "The cursor for view all Blog articles was closed successfully!"
            )
    return records


def view_all_article_titles(db_connection, sql_script):
    """View all Titles Blog Articles

    Args:
        db_connection (Connection): SQLite database connection representation
        sql_script (str): SQL script to execute

    Returns:
        list: Records list
    """

    records = []
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_script)
        records = cursor.fetchall()
        logging.info("The query to the table was successful!")
    except sqlite3.Error as error:
        logging.error(f"Query for record(s) in table failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info(
                "The cursor for view all titles Blog articles was closed successfully!"
            )
    return records


def get_blog_by_title(db_connection, title):
    """Get the title of Blog article

    Args:
        db_connection (Connection): SQLite database connection representation
        title (str): The Article title

    Returns:
        list: Records list
    """

    records = []
    try:
        cursor = db_connection.cursor()
        cursor.execute(f'SELECT * FROM articles WHERE title="{title}"')
        records = cursor.fetchall()
        logging.info("The query to the table by title was successful!")
    except sqlite3.Error as error:
        logging.error(f"Query for record(s) in table failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info(
                "The cursor for get the title of Blog article was closed successfully!"
            )
    return records


def get_blog_by_author(db_connection, author):
    """Get all Blog articles by author

    Args:
        db_connection (Connection): SQLite database connection representation
        author (str): The Article author

    Returns:
        list: Records list
    """

    records = []
    try:
        cursor = db_connection.cursor()
        cursor.execute(f'SELECT * FROM articles WHERE author="{author}"')
        records = cursor.fetchall()
        logging.info("The query to the table by author was successful!")
    except sqlite3.Error as error:
        logging.error(f"Query for record(s) in table failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info(
                "The cursor for get all Blog articles by author was closed successfully!"
            )
    return records


# def update_data(db_connection, author, title, content, postdate):
#     """Update the Blog article

#     Args:
#         db_connection (Connection): SQLite database connection representation
#         author (str): The Article author
#         title (str): The Article title
#         content (str): The Article body
#         postdate (datetime): The Article post date
#     """
#     pass


def delete_data(db_connection, title):
    """Delete the Blog article

    Args:
        db_connection (Connection): SQLite database connection representation
        title (str): The Article title
    """

    try:
        cursor = db_connection.cursor()
        cursor.execute(f'DELETE FROM articles WHERE title="{title}"')
        db_connection.commit()
        logging.info("The selected record was successfully deleted!")
    except sqlite3.Error as error:
        logging.error(f"Delete record(s) in table failed! {error}")
    finally:
        if cursor:
            cursor.close()
            logging.info(
                "The cursor for delete the blog article was closed successfully!"
            )


def render_about(*_) -> None:
    """Show App info"""

    st.write(
        """\
# Streamlit App Demo - {app_title}
Howdy :wave:!
Welcome to my Streamlit Full Stack App exploration.
This started as the {app_title} Fullstack App with just Streamlit + SQLite.
""".format(
            app_title=APP_TITLE
        )
    )


def main(db_connection):
    """A Simple CRUD Blog

    Args:
        db_connection (Connection): SQLite database connection representation
    """

    st.markdown(
        BLOG_HEADER_HTML_TPL.format(
            div_bg_color=SECONDARY_BACKGROUND_COLOR,
            h1_color=TEXT_COLOR,
            app_title=APP_TITLE,
        ),
        unsafe_allow_html=True,
    )

    menu = [
        "Home",
        "View Posts",
        "Add Posts",
        # "Update Posts",
        "Search...",
        "Manage Blog",
        "About",
    ]

    choice = st.sidebar.selectbox(
        "Menu", menu, help="Select a choice from the select list!"
    )

    if choice == "Home":
        st.subheader("Home")
        result = view_all_articles(db_connection, SELECT_SQL_SCRIPTS)

        if len(result) == 0:
            st.markdown(NOTFOUND_ENTRY_MSG_HTML_TPL, unsafe_allow_html=True)
        else:
            for article in result:
                post_author = article[0]
                post_title = article[1]
                post_content = str(article[2])[0:90]
                post_date = article[3]
                st.markdown(
                    HOME_ENTRIES_HTML_TPL.format(
                        div_bg_color=PRIMARY_COLOR,
                        title=post_title,
                        author=post_author,
                        date=post_date,
                        content=post_content,
                    ),
                    unsafe_allow_html=True,
                )

    elif choice == "View Posts":
        st.subheader("View Articles")
        all_titles = [
            article[0]
            for article in view_all_article_titles(
                db_connection, SELECT_DISTINCT_SQL_SCRIPTS
            )
        ]
        post_list = st.sidebar.selectbox(
            "View Posts", all_titles, help="Select a choice from the select list!"
        )
        post_result = get_blog_by_title(db_connection, post_list)

        if len(all_titles) == 0:
            st.markdown(NOTFOUND_ENTRY_MSG_HTML_TPL, unsafe_allow_html=True)
        else:
            for article in post_result:
                post_author = article[0]
                post_title = article[1]
                post_content = article[2]
                post_date = article[3]
                # st.text(f"Reading Time:{readingTime(post_content)}")
                st.markdown(
                    ENTRY_DETAILS_HTML_TPL.format(
                        div_bg_color=PRIMARY_COLOR,
                        title=post_title,
                        author=post_author,
                        date=post_date,
                    ),
                    unsafe_allow_html=True,
                )
                st.markdown(
                    ENTRY_CONTENT_MSG_HTML_TPL.format(content=post_content),
                    unsafe_allow_html=True,
                )

    elif choice == "Add Posts":
        st.subheader("Add Articles")
        blog_author = st.text_input(
            label="Enter Author Name",
            help="Please, enter the Author Name",
            placeholder="Example, Leonardo Caballero",
            max_chars=50,
        )
        blog_title = st.text_input(
            label="Enter Post Title",
            help="Please, enter the Post Title",
            placeholder="Example, Data science for Python",
        )
        blog_content = st_quill(
            # value='',
            placeholder="Example, Python is very great option for Data science today!",
            html=True,
        )
        blog_post_date = st.date_input(
            label="Pick publication date",
            help="Please, pick the publication date",
            value=datetime.date.today(),
        )
        if st.button(
            label="Add entry post",
            help="Here you safe a new entry post!",
        ):
            add_data(
                db_connection,
                INSERT_SQL_SCRIPTS,
                blog_author,
                blog_title,
                blog_content,
                blog_post_date,
            )
            st.success(f"Post: {blog_title} saved")

    # elif choice == "Update Posts":
    #     unique_titles = [article[0] for article in view_all_article_titles(db_connection, SELECT_DISTINCT_SQL_SCRIPTS)]
    #     st.subheader("Update Posts")
    #     st.markdown("Select a article to delete on the follow select list")
    #     update_blog_by_title = st.selectbox(
    #         "Unique Title", unique_titles,
    #         help="Select a choice from the select list!"
    #     )
    #     if st.button(
    #         label="Update (This Can't Be Undone!)",
    #         help="I hope you know what you're getting into!",
    #     ):
    #         update_data(db_connection, update_blog_by_title)
    #         st.warning(f"Updated: '{update_blog_by_title}'")

    elif choice == "Search...":
        st.subheader("Search Articles")
        search_term = st.text_input(
            label="Enter Search Term",
            help="Enter the Search Term!",
            placeholder="Example fot title, Data science for Python or Example fot author, Leonardo Caballero",
        )
        search_choice = st.radio(
            label="Field to Search By",
            options=("title", "author"),
            help="Check one criteria option to search!",
            horizontal=True,
        )

        if st.button(
            label="Search",
            help="I hope you will found what do you search!",
        ):

            if search_choice == "title":
                article_result = get_blog_by_title(db_connection, search_term)
            elif search_choice == "author":
                article_result = get_blog_by_author(db_connection, search_term)

            if len(article_result) == 0:
                st.markdown(
                    NOTFOUND_SEARCH_MSG_HTML_TPL.format(
                        div_bg_color=PRIMARY_COLOR,
                    ),
                    unsafe_allow_html=True,
                )
            else:
                for article in article_result:
                    post_author = article[0]
                    post_title = article[1]
                    post_content = article[2]
                    post_date = article[3]
                    # st.text(f"Reading Time:{readingTime(post_content)}")
                    st.markdown(
                        ENTRY_DETAILS_HTML_TPL.format(
                            div_bg_color=PRIMARY_COLOR,
                            title=post_title,
                            author=post_author,
                            date=post_date,
                        ),
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        ENTRY_CONTENT_MSG_HTML_TPL.format(content=post_content),
                        unsafe_allow_html=True,
                    )

    elif choice == "Manage Blog":
        st.subheader("Manage Articles")

        result = view_all_articles(db_connection, SELECT_SQL_SCRIPTS)

        if len(result) == 0:
            st.markdown(
                NOTFOUND_ENTRY_MSG_HTML_TPL.format(
                    div_bg_color=PRIMARY_COLOR,
                ),
                unsafe_allow_html=True,
            )
        else:
            clean_db = pd.DataFrame(
                result, columns=["Author", "Title", "Articles", "Post Date"]
            )
            st.dataframe(clean_db)

            unique_titles = [
                article[0]
                for article in view_all_article_titles(
                    db_connection, SELECT_DISTINCT_SQL_SCRIPTS
                )
            ]

            st.subheader("Delete Article")
            st.markdown("Select a article to delete on the follow select list")
            delete_blog_by_title = st.selectbox(
                "Unique Title",
                unique_titles,
                help="Select a choice from the select list!",
            )
            new_df = clean_db
            if st.button(
                label="Delete (This Can't Be Undone!)",
                help="I hope you know what you're getting into!",
            ):
                delete_data(db_connection, delete_blog_by_title)
                st.warning(f"Deleted: '{delete_blog_by_title}'")

            st.subheader("Generate Graphics")
            st.markdown("Select the checkbox for generate graphics")
            if st.checkbox(
                label="Metrics",
                help="Check this option for generate the Metrics Stats!",
            ):

                new_df["Length"] = new_df["Articles"].str.len()
                st.dataframe(new_df)

                st.subheader("Author Stats")
                new_df["Author"].value_counts().plot(kind="bar")
                st.pyplot()

                st.subheader("Author Stats")
                new_df["Author"].value_counts().plot.pie(autopct="%1.1f%%")
                st.pyplot()

            if st.checkbox(
                label="Word Cloud",
                help="Check this option for generate a Term Word Cloud!",
            ):
                st.subheader("Generate Word Cloud")
                # text = new_df['Articles'].iloc[0]
                text = ",".join(new_df["Articles"])
                wordcloud = WordCloud().generate(text)
                plt.pyplot.imshow(wordcloud, interpolation="bilinear")
                plt.pyplot.axis("off")
                st.pyplot()

            if st.checkbox(
                label="Bar Horizontal Plot",
                help="Check this option for generate a Bar Horizontal Plot!",
            ):
                st.subheader("Length of Articles")
                new_df = clean_db
                new_df["Length"] = new_df["Articles"].str.len()
                barh_plot = new_df.plot.barh(x="Author", y="Length", figsize=(20, 10))
                st.pyplot()

    elif choice == "About":
        render_about()


if __name__ == "__main__":

    connection = create_connection(DB)
    if connection is not None:
        main(connection)
    else:
        logging.error(f"ERROR! cannot create the database connection to the {DB} file.")
