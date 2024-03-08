from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from utils.train import *

def write_to_mysql():
    # Conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="mysql",
        user="airflow",
        password="airflow",
        database="airflow"
    )
    cursor = conn.cursor()

    # create dataframe pandas
    df = pd.read_csv('/opt/airflow/data/penguins_lter.csv', sep=',')
    # Step 2: Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine("mysql+mysqlconnector://airflow:airflow@mysql/airflow")

    # Step 3: Convert the Pandas DataFrame to a format for MySQL table insertion
    df.to_sql('penguins', con=engine, if_exists='replace', index=False)

    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    conn.close()

def delete_to_mysql():
    # Conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="mysql",
        user="airflow",
        password="airflow",
        database="airflow"
    )
    cursor = conn.cursor()

    # Step 1: SQL que borrara los rows que tengan mal el sexo
    delete_query = "DELETE FROM penguins WHERE sex NOT IN ('MALE', 'FEMALE') OR sex IS NULL"

    # Step 2: Ejecutar la query
    cursor.execute(delete_query)

    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    conn.close()


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 8),
    'retries': 1,
}

with DAG('main', default_args=default_args, schedule_interval='@once') as dag:
    write_to_mysql_task = PythonOperator(
        task_id='write_to_mysql_task',
        python_callable=write_to_mysql
    )
    delete_to_mysql = PythonOperator(
        task_id='delete_to_mysql',
        python_callable=delete_to_mysql
    )
    train_model = PythonOperator(
        task_id='train_model',
        python_callable=run_train
    )
write_to_mysql_task >> delete_to_mysql >> train_model