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

