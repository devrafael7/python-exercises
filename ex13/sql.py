import mysql.connector

nome = input("type your name: ")

conection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="boladeneve12",
    database="user_conection"
)

cursor = conection.cursor()

sql_comand = "INSERT INTO user (name) VALUES (nome)"
cursor.execute(sql_comand, (nome,))

conection.commit()

conection.commit()  # Certifique-se de confirmar a transação
cursor.close()
conection.close()

print("Data inserted successfully!")