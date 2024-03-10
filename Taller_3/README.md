1. ejecutar el comando:
docker exec -it taller_3-mysql-1 bash
```
mysql -u airflow -p airflow
```
docker exec -it taller_3-airflow-worker bash

2. ingresar a la url:
    ```url
    localhost:8080/home
3. ingresar las siguientes credenciales en la ventana de inicio de sesion
    Usuario: airlflow
    Password: Airflow
    ![alt text]()
4. activar el DAG "main" haciendo clic en el boton encerrado en el recuadro rojo
5. ingresar al dag haciendo clic sobre el nombre
6. hacer clic en la pestaña "grahp"
7. validar que cada una de las cajas de grafo de tareas este en estado success
8. Acceder a la url:
	```url
 	localhost:8000/docs
9. Consultar los modelos disponibles a traves del metodo GET "get_models"
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso1.png)
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso2.png)
	En el recuadro rojo se observan los modelos disponibles
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso3y4.png)
	Copiar el nombre del modelo deseado SIN comillas
10. Realizar una prediccion a traves del metodo POST "predict"
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso1predict.png)
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso2predict.png)
	En el campo de texto "model_name" pegar el nombre del modelo SIN comillas
	Dentro del campo de texto "request_body" se encuentra ya un body definido por defecto
	Hacer clic en el recuadro execute
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso3y4predict.png)
	En la seccion "server_response" encontrara un objeto json que contiene el tipo de modelo usado y la prediccion para los valores ingresados
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/predictFinal.png)
	
