1. ejecutar el comando:   

	```url
	docker exec -it taller_3-mysql-1 bash   

	```url
	mysql -u airflow -p airflow   
	
	```url
	docker exec -it taller_3-airflow-worker bash

2. ingresar a la url:   
    ```url
    localhost:8080/home   
3. ingresar las siguientes credenciales en la ventana de inicio de sesion   
    Usuario: airlflow   
    Password: Airflow   
    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_3/images/Captura%20de%20pantalla%202024-03-10%20071307.png)   
4. activar el DAG "main" haciendo clic en el boton encerrado en el recuadro rojo   
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_3/images/Captura%20de%20pantalla%202024-03-10%20071425.png)   
5. ingresar al dag haciendo clic sobre el nombre "main"   
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_3/images/Captura%20de%20pantalla%202024-03-10%20081005.png)   
6. hacer clic en la pestaña "grahp"   
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_3/images/Captura%20de%20pantalla%202024-03-10%20081019.png)   
7. validar que cada una de las cajas de grafo de tareas este en estado success   
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_3/images/Captura%20de%20pantalla%202024-03-10%20071506.png)   
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_3/images/Captura%20de%20pantalla%202024-03-10%20071513.png)   
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_3/images/Captura%20de%20pantalla%202024-03-10%20071520.png)   
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
	
