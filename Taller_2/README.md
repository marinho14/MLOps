1. Clonar el repo mediante el comando:
    ```shell
    git clone https://github.com/marinho14/MLOps.git
    
2. Pararse en el directorio del taller 2 mediante el comando:
    ```shell
    cd MLOps/Taller_2/
    
3. Iniciar el servicio contenerizado mediante en comando:
    ```shell
    docker compose up
    (esta operacion puede tardar un poco)

4. Acceder a la url:
    ```shell
    http://localhost:8888/
    
5. Será redirigido a la pagina:
    ```shell
    http://localhost:8888/login?next=%2Flab%3F
    
    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20180426.png)

6. Abrir una ventana de terminal y ejecutar el siguiente comando:
    ```shell
    docker exec -it taller_2-tfx-1 bash
    
7. Este comando lo llevara a un terminal al interior del contenedor, ejecutar el comando y seguir
   las instrucciones desplegadas en la imagen del paso 5.
    ```shell
    jupyter server list

8. Hacer clic en login & set new password.
   
   ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20181247.png)
   
9. Hacer clic en build una vez esta ventana salga en pantalla.
 
   ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20181227.png)

10. Hacer clic en "save & reload".
 
    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20195320.png)

11. Abir el archivo ipynb y ejecutar cada celda haciendo clic en el boton run.
    
    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20200601.png)

    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20200618.png)
    
