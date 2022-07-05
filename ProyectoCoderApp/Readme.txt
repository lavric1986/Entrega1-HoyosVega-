Almacen AppCoder

##Descripcion
Para la realizacion de este proyecto, se tomo como referencia el ejemplo 
que se ha realizado durante las clases es decir el "ProyectoCoderApp", que 
consta de 3 models, "Maquinaria", "Operarios", "Herramientas", cada modelo 
con su respectiva pestaña en el Base.html, con su respectiva funcion en el 
view de la app y URLS, la funcion principal de la pagina es guardar los 
datos de los modelos ya explicados anteriormente.

 ├── Requerimientos
    │   # requiere una version de python preferiblemente la 9.4
    │
    ├── Setup Project
    │   # Comandos que se deben ejecutar para configurar por primera vez el proyecto 
    │   1-"python manage.py makemigrations"(migrar las clases creadas en models)
    │   2-"python .\manage.py migrate"(confirmar las migraciones hechas en el proyecto)
    ├── Run Project
    │   # Para arrancar el servidor de manera correcta se debe ejecutar el comando "python .\manage.py runserver" 
    │
    ├── Account
    │   ├── API
    │   │    # El servidor que se utilizara por defecto sera el http://127.0.0.1:8000/ el cual nos llevara al 
    │   │       administrador(Admin) y a la aplicacion(coderapp)
    │   └── DB
    │        # El password para acceder a la bases de datos se debe hacer con el comando 
    │        "python manage.py createsuperuser"
    │
    ├── Miscellaneous Tools
    │   ├── Clean Project
    │   │   # los pasos para restablecer el proyecto, se sugiere descaragar el archivo zip desde Github 
    │   │
    │   ├── Reset DB
    │   │    # Por ahora los datos seran por defecto, y solo seran utilizados para pruebas de la misma app
    │   │
    │   ├── Visual estudio
    │       # se recomienda utilizar dicho programa configurado con las extenciones y la version correpsondiente
    │       de python 
    │   
    │   
    │     
    │
    └── Other topics
         # Este anteproyecto cuenta con unos fallos de visualizacion de los datos en maquinaria y operarios, pero esta version
         es funcional y con margen de mejora