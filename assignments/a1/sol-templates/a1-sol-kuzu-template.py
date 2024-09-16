import kuzu as kz

def q1(conn: kz.Connection) -> kz.QueryResult:
  return conn.execute(
      """                                                                                                                          
      <Write Your Query Here>                                                                                                          
      """)

def q2(conn: kz.Connection) -> kz.QueryResult:
  return conn.execute(
      """                                                                                                                          
      <Write Your Query Here>                                                                                                          
      """)

def q3(conn: kz.Connection) -> kz.QueryResult:
  return conn.execute(
      """                                                                                                                          
      <Write Your Query Here>                                                                                                          
      """)

def q4(conn: kz.Connection) -> kz.QueryResult:
  return conn.execute(
      """                                                                                                                          
      <Write Your Query Here>                                                                                                          
      """)

def q5(conn: kz.Connection) -> kz.QueryResult:
  return conn.execute(
      """                                                                                                                          
      <Write Your Query Here>                                                                                                          
      """)

def main():
    # See the comment in insert_data_kuzu.py about Kuzu database directories.
    db = kz.Database("./ex_db_kuzu")
    conn = kz.Connection(db)
    res = q1(conn)
    # res = q2(conn)
    # res = q3(conn)
    # res = q4(conn)
    # res = q5(conn)
    while res.has_next():
      print(res.get_next())


if __name__ == "__main__":
    main()
