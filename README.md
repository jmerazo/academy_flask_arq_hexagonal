# academy_flask_arq_hexagonal
Arquitectura hexagonal y Dockerizado de proyecto Academy

1. academy: corresponde al proyecto de flask con arquitectura hexagonal

  Para ejecutar el proyecto de forma correcta se debe:
  - Inicializar el entorno virtual: python -m venv env
  - Ejecutar el entorno virtual: env\Scripts\activate
  - Instalar los requerimientos: pip install -r requirements.txt
  - Instalar el archivo sql en la ruta: academy/src/sql/academy.sql
  - Ejecutar el servidor del frontend: python main_frontend.py
  
2. docker_academy: descarga y ejecuta las imagenes de la base de datos y el proyecto de academy de docker hub
3. sql_academy: se crea la imagen de la base de datos con docker
