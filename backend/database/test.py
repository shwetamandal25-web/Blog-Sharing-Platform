from connection import getConnection
con = getConnection()
print("database connected sucessfully")
cursor = con.cursor()
cursor.execute("SELECT version()")
print(cursor.fetchone())
cursor.close()
con.close()