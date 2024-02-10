1. desde la consola de GIT ejecutar el comando
	git clone https://github.com/marinho14/MLOps.git
2. desplazarse al directorio
	cd MLOps/Taller_1
3. constuir la imagen mediante el comando
	docker build -t mlopstaller1 .
4. correr la imagen creada mediante el comando
	docker run --name instancia_taller1 -p 8000:80 mlopstaller1 
5. acceder a la url 
	localhost:8000/docs
6. consultar los modelos disponibles a traves del metodo GET "get_models"
   	![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_1/images/paso1.png)
	en el recuadro rojo se observan los modelos disponibles
	copiar el nombre del modelo deseado SIN comillas
8. realizar una prediccion a traves del metodo POST "predict"
	en el campo de texto "model_name" pegar el nombre del modelo SIN comillas
	dentro del campo de texto "request_body" se encuentra ya un bodu definido por defecto
	hacer clic en el recuadro execute
	en la seccion "server_response" encontrara un objeto json que contiene el tipo de modelo usado y la prediccion para los valores ingresados
	
