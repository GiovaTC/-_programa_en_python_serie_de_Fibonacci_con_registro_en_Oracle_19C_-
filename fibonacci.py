import cx_Oracle
from datetime import datetime

# ===============================
# CONFIGURACIÓN DE BASE DE DATOS
# ===============================
DB_USER = "system"
DB_PASSWORD = "Tapiero123"
DB_DSN = "localhost:1521/orcl"

# ===============================
# FUNCIÓN FIBONACCI
# ===============================
def fibonacci(n):
    serie = []
    a, b = 0, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

# ===============================
# REGISTRO EN ORACLE
# ===============================
def registrar_en_oracle(n, serie, suma):
    connection = None
    try:
        connection = cx_Oracle.connect(
            user = DB_USER,
            password = DB_PASSWORD,
            dsn=DB_DSN
        )

        cursor = connection.cursor()

        sql = """
        INSERT INTO fibonacci_log (n_terminos, serie, suma_total, fecha_registro)
        VALUES (:n, :serie, :suma, :fecha)
        """

        cursor.execute(sql, {
                       "n": n,
            "serie": ", ".join(map(str, serie)),
            "suma": suma,
            "fecha": datetime.now()  
        })

        connection.commit()
        print("registro almacenado correctamente en oracle.")
    
    except cx_Oracle.DatabaseError as e:
        print("error en base de datos:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()

# ===============================
# PROGRAMA PRINCIPAL
# ===============================   

