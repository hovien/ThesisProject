import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "S1a9m0i487Sql",
                           db = "Tweets")
    c = conn.cursor()

    return c, conn
		
