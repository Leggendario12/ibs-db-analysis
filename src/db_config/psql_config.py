"""
PSQL Configuration.

Set of configuration required for connecting to the database.

Set the configuration inside the .env files for setting up the
environment variables.
"""
from __future__ import annotations

import os

import psycopg2 as ps
from dotenv import find_dotenv, load_dotenv

################
# LOAD THE ENV #
################
env_file: str = find_dotenv()
if env_file:
    load_dotenv(env_file)

###############################
# CONNECTION | IBS (IBSCARDS) #
###############################
connection = ps.connect(
    host=os.environ.get("CARDS_DB_HOST", None),
    port=os.environ.get("CARDS_DB_PORT", None),
    dbname=os.environ.get("CARDS_DB_NAME", None),
    user=os.environ.get("CARDS_DB_USER", None),
    password=os.environ.get("CARDS_DB_PASSWD", None)
)
