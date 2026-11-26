from connection import getConnection

username = input("Enter username: ")
password = input("Enter password: ")

con = getConnection()

if con:
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )

    con.commit()

    print("User registered successfully")

    cursor.close()
    con.close()