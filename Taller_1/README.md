1. Desde la consola de GIT ejecutar el comando
   	```shell
	git clone https://github.com/marinho14/MLOps.git
2. Desplazarse al directorio
   	```shell
	cd MLOps/Taller_1
3. Constuir la imagen mediante el comando
   	```shell
	docker build -t mlopstaller1 .
4. Correr la imagen creada mediante el comando
   	```shell
	docker run --name instancia_taller1 -p 8089:80 mlopstaller1
5. Acceder a la url:
	```url
 	localhost:8089/docs
6. Consultar los modelos disponibles a traves del metodo GET "get_models"
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso1.png)
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso2.png)
	En el recuadro rojo se observan los modelos disponibles
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso3y4.png)
	Copiar el nombre del modelo deseado SIN comillas
7. Realizar una prediccion a traves del metodo POST "predict"
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso1predict.png)
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso2predict.png)
	En el campo de texto "model_name" pegar el nombre del modelo SIN comillas
	Dentro del campo de texto "request_body" se encuentra ya un body definido por defecto
	Hacer clic en el recuadro execute
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso3y4predict.png)
	En la seccion "server_response" encontrara un objeto json que contiene el tipo de modelo usado y la prediccion para los valores ingresados
	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/predictFinal.png)
	
