from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

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
        CREATE TABLE IF NOT EXISTS penguins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            studyName VARCHAR(255),
            SampleNumber INT,
            Species VARCHAR(255),
            Region VARCHAR(255),
            Island VARCHAR(255),
            Stage VARCHAR(255),
            IndividualID VARCHAR(255),
            ClutchCompletion VARCHAR(255),
            DateEgg DATE,
            CulmenLength FLOAT,
            CulmenDepth FLOAT,
            FlipperLength FLOAT,
            BodyMass INT,
            Sex VARCHAR(255),
            Delta15N FLOAT,
            Delta13C FLOAT,
            Comments VARCHAR(255)
        )
    """
    cursor.execute(create_table_query)

    # create dataframe pandas
    df = pd.read_csv('data\penguins_lter.csv', sep=',')
    # Step 2: Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine("mysql+mysqlconnector://root:new_password@localhost/mydatabase")

    # Step 3: Convert the Pandas DataFrame to a format for MySQL table insertion
    df.to_sql('penguins', con=engine, if_exists='append', index=False)

    # Ejemplo de inserción de datos en la tabla
    # insert_query = "INSERT INTO my_table (column1, column2) VALUES (%s, %s)"

    print(cursor.rowcount, "record inserted.")

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
