import sqlite3

conexion = sqlite3.connect('estudiante.db')

# Creamos el cursor
cursor = conexion.cursor()

#-----------------------------------------------------------------------------------

#CREAR UNA TABLA Estudiante

#cursor.execute('''
#    CREATE TABLE Estudiante(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre VARCHAR(50) NOT NULL,
#    apellido VARCHAR(50) NOT NULL,
#    cedula VARCHAR(11)NOT NULL,
#    telefono VARCHAR(15)
#     )
#     ''')


# CREAR UN ARRAY DE ESTUDIANTES
estudiantes = [
    ('Carlos' ,'monsalve' ,'1155' ,'2385122'),
    ('a' ,'monsalve' ,'1155' ,'2385122'),
    ('c' ,'monsalve' ,'1155' ,'2385122')
]
#INSERT
cursor.executemany("INSERT INTO Estudiante VALUES (null,?,?,?,?)",estudiantes)

#UPDATE
cursor.execute("UPDATE Estudiante set nombre='Camilo' where id =1")

#DELETE
cursor.execute("DELETE FROM Estudiante WHERE id = 16")
#DELETE
cursor.execute("SELECT * FROM Estudiante")
estudiante=cursor.fetchall()
print(estudiante)

# Guardamos los cambios haciendo un commit
conexion.commit()
conexion.close()
