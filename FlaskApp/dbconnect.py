import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "flask",
                           passwd = "F2l0a1s7k",
                           db = "Tweets")
    c = conn.cursor()

    return c, conn
		
