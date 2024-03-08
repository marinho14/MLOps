from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import mysql.connector

def write_to_mysql():
    # Conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="mysql",
        user="airflow",
        password="airflow",
        database="airflow"
    )
    cursor = conn.cursor()

    # Crear la tabla si no existe
    create_table_query = """
        CREATE TABLE IF NOT EXISTS my_table (
            column1 VARCHAR(255),
            column2 VARCHAR(255)
        )
    """
    cursor.execute(create_table_query)

    # Ejemplo de inserción de datos en la tabla
    insert_query = "INSERT INTO my_table (column1, column2) VALUES (%s, %s)"
    data = ("value1", "value2")
    cursor.execute(insert_query, data)

    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    conn.close()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 6),
    'retries': 1,
}

with DAG('write_to_mysql', default_args=default_args, schedule_interval='@once') as dag:
    write_to_mysql_task = PythonOperator(
        task_id='write_to_mysql_task',
        python_callable=write_to_mysql
    )
