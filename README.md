# -_programa_en_python_serie_de_Fibonacci_con_registro_en_Oracle_19C_- :. 
# Programa en Python – Serie de Fibonacci con Registro en Oracle 19c .

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/c993ce19-0896-4a0a-8d58-5a6ab6ce7e12" />  

## 1. Descripción general:

A continuación se presenta una solución completa, profesional y ejecutable para un programa en **Python** que:

- Calcula la serie de Fibonacci hasta **N** términos  
- Suma los valores generados  
- Registra la ejecución en **Oracle Database 19c**  
- Está alineado con buenas prácticas técnicas y académicas.  

### Funcionalidades principales:

El programa realiza lo siguiente:

- Solicita al usuario un número **N**
- Genera la serie de Fibonacci hasta **N** términos
- Calcula la suma total de la serie
- Inserta en Oracle:
  - Número de términos
  - Serie generada (como texto)
  - Resultado de la suma
  - Fecha de ejecución.

---

## 2. Tecnologías utilizadas:

- Python 3.9+
- Oracle Database 19c
- cx_Oracle (driver oficial)
- SQL Developer (opcional)

---

## 3. Script SQL – Oracle 19c:

Ejecutar previamente el siguiente script en Oracle Database 19c:

```sql
CREATE TABLE fibonacci_log (
    id              NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    n_terminos      NUMBER NOT NULL,
    serie           CLOB NOT NULL,
    suma_total      NUMBER NOT NULL,
    fecha_registro  DATE DEFAULT SYSDATE
);
4. Instalación del driver Oracle para Python
Instalar el driver oficial cx_Oracle:

pip install cx_Oracle
Nota:
Es obligatorio tener Oracle Instant Client instalado y correctamente configurado en el sistema operativo.

5. Programa completo en Python

import cx_Oracle
from datetime import datetime

# ===============================
# CONFIGURACIÓN DE BASE DE DATOS
# ===============================
DB_USER = "system"
DB_PASSWORD = "oracle"
DB_DSN = "localhost:1521/ORCLCDB"

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
            user=DB_USER,
            password=DB_PASSWORD,
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
        print("Registro almacenado correctamente en Oracle.")

    except cx_Oracle.DatabaseError as e:
        print("Error en base de datos:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()

# ===============================
# PROGRAMA PRINCIPAL
# ===============================
def main():
    n = int(input("Ingrese el número de términos Fibonacci: "))

    if n <= 0:
        print("El número debe ser mayor que cero.")
        return

    serie = fibonacci(n)
    suma = sum(serie)

    print("\nSerie Fibonacci generada:")
    print(serie)

    print("\nSuma total:")
    print(suma)

    registrar_en_oracle(n, serie, suma)

if __name__ == "__main__":
    main()
6. Ejemplo de ejecución
Entrada

Ingrese el número de términos Fibonacci: 7
Salida

Serie Fibonacci generada:
[0, 1, 1, 2, 3, 5, 8]

Suma total:
20

Registro almacenado correctamente en Oracle.
7. Consulta de verificación en Oracle

SELECT
    id,
    n_terminos,
    serie,
    suma_total,
    fecha_registro
FROM fibonacci_log
ORDER BY id DESC;
8. Buenas prácticas aplicadas
Separación lógica de funciones

Manejo adecuado de excepciones

Uso de tipo CLOB para almacenar la serie

Cierre seguro de conexiones y cursores

Código legible, mantenible y documentado :. / .
