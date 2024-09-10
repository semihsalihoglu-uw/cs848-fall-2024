import shutil
import duckdb

# DuckDB databases are single files. Here we're setting up a database file ex_db.duckdb 
# that lives under the current directory from which you're running this script. You need 
# to run this script only once to set up your database and then work on your solutions script
# to work on your queries, which should also point to the same file.
shutil.rmtree("ex_db.duckdb", ignore_errors=True)
conn = duckdb.connect(database="ex_db.duckdb")

# Create tables and insert data
conn.execute(
    """
    CREATE OR REPLACE TABLE Person AS
    SELECT *
    FROM read_csv(
        'data/person.csv',
        header = true,
        delim = ',',
        escape = '"'
    )
    """
)

conn.execute(
    """
    CREATE OR REPLACE TABLE Account AS
    SELECT id, account_id, owner, CAST(balance AS DOUBLE) AS balance
    FROM read_csv(
        'data/account.csv',
        header = true
    )
    """
)

conn.execute(
    """
    CREATE OR REPLACE TABLE Transfer AS
    SELECT source, target, CAST(amount AS DOUBLE) AS amount, transaction_id
    FROM read_csv('data/transfer.csv', header = true)
    """
)




