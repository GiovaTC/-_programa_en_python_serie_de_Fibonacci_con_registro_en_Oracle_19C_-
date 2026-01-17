CREATE TABLE fibonacci_log (
    id              NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    n_terminos      NUMBER NOT NULL,
    serie           CLOB NOT NULL,
    suma_total      NUMBER NOT NULL,
    fecha_registro  DATE DEFAULT SYSDATE
);

COMMIT;