"""
MySQL Configuration.

Set of configuration required for connecting to MySQL database.
"""
from __future__ import annotations

import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from mysql import connector
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from mysql.connector.cursor_cext import CMySQLCursor
from mysql.connector.pooling import (
    PooledMySQLConnection,
    MySQLConnection,
    CMySQLConnection,
)

################
# LOAD THE ENV #
################
env_file: str = find_dotenv()
if env_file:
    load_dotenv(env_file)


###############################
# CONNECTION | IBS (IBSCARDS) #
###############################
def test_connection() -> None:
    """
    Test the connection.

    Returns
    -------
    None
    """
    connection: Optional[
        PooledMySQLConnection,
        MySQLConnection,
        CMySQLConnection,
    ] = None
    cursor: Optional[MySQLCursor, CMySQLCursor] = None

    try:
        connection = connector.connect(
            host=os.environ.get("CARDS_DB_HOST"),
            port=os.environ.get("CARDS_DB_PORT"),
            user=os.environ.get("CARDS_DB_USER"),
            password=os.environ.get("CARDS_DB_PASSWD"),
            dbname=os.environ.get("CARDS_DB_NAME"),
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(
                f"Connected to {os.environ.get('CARDS_DB_NAME', None)}",
                db_info
            )
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(
                "You're connected to database: ", record)

    except Error as error:
        print("Error while connecting to MYSQL", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


######################
# CONNECTION | MySQL #
######################
def connect_to_mysql() -> Optional[
    PooledMySQLConnection,
    MySQLConnection,
    CMySQLConnection,
]:
    """
    Connect to MySQL (IBSCARDS).

    Returns
    -------
    Optional[
        PooledMySQLConnection,
        MySQLConnection,
        CMySQLConnection,
    ]

    Raises
    ------
    Error
    """
    try:
        connection = connector.connect(
            host=os.environ.get("CARDS_DB_HOST"),
            port=os.environ.get("CARDS_DB_PORT"),
            user=os.environ.get("CARDS_DB_USER"),
            password=os.environ.get("CARDS_DB_PASSWD"),
            dbname=os.environ.get("CARDS_DB_NAME"),
        )

        return connection

    except Error as error:
        raise error
