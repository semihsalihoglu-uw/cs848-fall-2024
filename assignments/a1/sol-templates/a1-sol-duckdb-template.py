import duckdb as duck

def q1(conn: duck.DuckDBPyConnection) ->duck.DuckDBPyRelation:
  print("Running q1")
  return conn.query(
      """                                                                                                                          
      <Write Your Query Here>                                                                                                      
  """)

def q2(conn: duck.DuckDBPyConnection) ->duck.DuckDBPyRelation:
  print("Running q2")
  return conn.query(
      """                                                                                                                          
      <Write Your Query Here>                                                                                                      
  """)


def main():
  # See the comment in insert_data_duckdb.py about DuckDB database files.  
  conn = duck.connect(database="ex_db.duckdb")
  res = q1(conn)
  # res = q2(conn)                                                                                                               
  print(res.show());

if __name__ == "__main__":
    main()
