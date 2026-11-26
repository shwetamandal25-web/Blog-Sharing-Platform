from connection import getConnection

username = input("Enter username: ")
password = input("Enter password: ")

con = getConnection()

if con:
    cursor = con.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username,password)
    )

    user = cursor.fetchone()

    if user:
        print("Login Successful")
    else:
        print("Invalid Username or Password")

    cursor.close()
    con.close()