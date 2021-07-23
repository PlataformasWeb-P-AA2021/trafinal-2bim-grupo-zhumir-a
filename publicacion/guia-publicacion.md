# Trabajo Final - Segundo Bimestre

## Grupo: zhumir-a
## Asignatura: Plataformas Web

### Guía para levantar el proyecto de Django en Nginx

Desde el CLI:

1. Instalar la librería nginx

`$ sudo apt install nginx`

![Instalación Nginx](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo-zhumir-a/blob/main/publicacion/images/paso1_instalar%20Nginx.png)

2. Instalar el entorno virtual para Python

`$ sudo apt install -y python3-venv`

![Instalación Entorno Virtual](../images/paso2_entornoPython.png)

3. Crear un entorno para Django, en este caso se llamará *django_env*

`$ python3 -m venv django_env`

![Creación de entorno Django](../images/paso3_entornoDjango.png)

Con el comando `ls` verificamos que se ha creado correctamente y lo visualizamos entre los archivos dentro de la ubicación actual.

4. Activación del entorno virtual *django_env*

`$ source django_env/bin/activate`

![Activación de entorno Django e Instalación de Django](../images/paso4_ActivacionInstalacion.png)

Así mismo se debe instalar django desde los paquetes de instalación de Python (*pip*). `$ pip install django`

5. Instalar Gunicorn esde los paquetes de instalación de Python (*pip*).

`$ pip install gunicorn`

![Instalación de Gunicorn](../images/paso5_InstalacionGunicorn.png)

6. Añadir la/las direcciones IP al archivo *settings.py* dentro de nuestro proyecto de Django

`ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]`

![Modificación Settings](../images/paso6_modificacionSettings.png)

7. Realizar la configuración para Gunicorn, para ello primero se creó un directorio donde se ubicará el archivo *gunicorn_config.py*

`$ mkdir conf`

Después creamos el archivo *gunicorn_config.py* dentro del directorio creado y escribiremos la configuración:

![Configuración Gunicorn](../images/paso7_configuracionGunicorn.png)

* command -> Especificamos el ejecutable de Gunicorn.
* pythonpath -> Especificamos la ruta de nuestro proyecto Django.
* bind -> Especificamos el socket del servidor para enlazar.
* workers -> Trabajadores utilizados por Gunicorn para controlar las solicitudes.

8. Empezar a emplear Gunicorn, indicando la ubicación del archivo de configuración creado recientemente y el .wsgi de nuestro proyecto.

`$ gunicorn -c conf/gunicorn_config.py proyectoCatastros.wsgi`

![Levantanmiento Gunicorn](../images/paso8_LevantamientoGunicorn.png)

Ctrl+Z para pausar el proceso y después usamos el comando `$ bg` para reaunudar el proceso que se suspendió en segundo plano.

9. Iniciamos el servicio Nginx

`$ sudo service nginx start`

![Levantanmiento Gunicorn](../images/paso9_InicioNginx.png)

10. Creamos el directorio static y su ruta será ingresada en el *settings.py*

`STATIC_URL = '/home/castle/static/'`

![Modificación settings.py](../images/paso10_StaticEnSettings.png)

11. Añadimos la configuración de nuestro proyecto desde un archivo de configuración creado para Nginx, en este caso se ubicará en el directorio:

`/etc/nginx/sites-available/proyectoCatastros`

![Configuración de proyecto para Nginx](../images/paso11_ConfiguracionProyectoNginx.png)

Tome en consideración para para la creación del archivo se debe ingresar con permisos de administrador (sudo).

12. Habilitar nuestro sitio: para ello primero nos ubicamos en el directorio `/etc/nginx/sites-enabled`, una vez dentro del directorio lo habilitamos creando el enlace a nuestro proyecto `$ sudo ln -s /etc/nging/sites-available/proyectoCatastros`

![Enlace a sitio](../images/paso12_EnlaceProyecto.png)

Podemos verificar que se enlazaron correctamente con el enlace `$ ls -l`

![Comprobación de enlace](../images/paso12_comprobacionEnlace.png)

13. Reiniciamos Nginx

`$ sudo systemctl restart nginx`

![Reinicio Nginx](../images/paso13_reinicioNginx.png)

14. Comprobamos su funcionalidad en el navegador

![Prueba en Navegador](../images/pasoFinal_Comprobacion.png.png)
