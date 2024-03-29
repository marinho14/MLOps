1. Clonar el repo mediante el comando:
    ```shell
    git clone https://github.com/marinho14/MLOps.git
    
2. Pararse en el directorio del taller 2 mediante el comando:
    ```shell
    cd MLOps/Taller_2/
    
3. Iniciar el servicio contenerizado mediante en comando:
    ```shell
    docker compose up
    ```
    
    (esta operacion puede tardar un poco)
   
    Una vez finaliza este proceso, el sistema presenta una URL a traves de la cual acceder a jupyter.
    (en este caso puede saltar al paso 9)

    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/MicrosoftTeams-image.png)

    En caso de que el sistema no presente la url, por favor continuar con los pasos en el orden presentado.
    
5. Acceder a la url:
    ```shell
    http://localhost:8888/
    
6. Será redirigido a la pagina:
    ```shell
    http://localhost:8888/login?next=%2Flab%3F
    ```

    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20180426.png)

7. Abrir una ventana de terminal y ejecutar el siguiente comando:
    ```shell
    docker exec -it taller_2-tfx-1 bash
    
8. Este comando lo llevara a un terminal al interior del contenedor, ejecutar el comando y seguir
   las instrucciones desplegadas en la imagen del paso 5.
    ```shell
    jupyter server list

9. Hacer clic en login & set new password.
   
   ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20181247.png)
   
10. Hacer clic en build una vez esta ventana salga en pantalla.
 
   ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20181227.png)

11. Hacer clic en "save & reload".
 
    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20195320.png)

12. Abir el archivo ipynb y ejecutar cada celda haciendo clic en el boton run.
    
    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20200601.png)

    ![alt text](https://github.com/marinho14/MLOps/blob/main/Taller_2/imagenes/Captura%20de%20pantalla%202024-02-18%20200618.png)
    
