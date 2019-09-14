Estructura
==========

El esqueleto está distribuido de la siguiente manera:

::

    .
    ├── README.md
    ├── apps
    |   ├── common
    |   │   ├── __init__.py
    |   │   ├── badwords
    |   │   ├── context_processors.py
    |   │   ├── datastructures.py
    |   │   ├── decorators.py
    |   │   ├── facebook.py
    |   │   ├── functional.py
    |   │   ├── middleware.py
    |   │   ├── models.py
    |   │   ├── sabmiller
    |   │   ├── sms.py
    |   │   ├── ubigeo
    |   │   ├── utils.py
    |   │   ├── validators.py
    |   │   └── views.py
    |   └── website
    |       ├── __init__.py
    |       ├── urls.py
    |       └── views.py
    ├── db.sqlite3
    ├── docs
    |   ├── Makefile
    |   ├── build
    |   │   ├── doctrees
    |   │   └── html
    |   ├── documentation.txt
    |   ├── make.bat
    |   └── source
    ├── media
    ├── requirements.txt
    ├── settings
    │   ├── __init__.py
    │   ├── manage.py
    │   ├── settings.py
    │   ├── settings_development.py
    │   ├── settings_staging.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── wsgi_staging.py
    ├── static
    │   ├── admin
    │   └── grappelli
    └── templates
        └── index.html

En donde:

* ``README.md`` - Readme inicial del esqueleto.
* ``apps`` - Carpeta contenedora de todas las aplicaciones del proyecto.
* ``apps/common`` - Aplicación que contiene funcionalidad común a la mayoría de proyeyctos.
* ``apps/website`` - Aplicación básica que contiene una única vista.
* ``db.sqlite3`` - Base de datos en formato sqlite v3 usada principalmente para el desarrollo.
* ``docs`` - Carpeta que contiene que contiene la documentación del esqueleto.
* ``docs/build/html`` - Raíz de la documentación generada del proyecto.
* ``media`` - Carpeta donde se ubicará todo el contenido estático generado por el proyecto.
* ``requirements.txt`` - Archivo de definición de dependencias del entorno de ejecución del proyecto, se usa en conjunto con ``pip`` para la instalación de las dependencias.
* ``settings`` - Carpeta que aloja todos los archivos de configuración del proyecto de django del esqueleto.
* ``settings/settings.py`` - Archivo principal de configuración del proyecto, usado para todas las configuraciones que afectan al proyecto en general y aquellas específicas del entorno de producción.
* ``settings/settings_development.py`` - Archivo de configuración para el entorno de desarrollo. Debe importar todas las configuraciones del archivo general y sobreescribir aquellas que sólo se usan en este entorno.
* ``settings/settings_staging.py`` - Archivo de configuración para el entorno de staging. Debe importar todas las configuraciones del archivo general y sobreescribir aquellas que sólo se usan en este entorno.
* ``settings/wsgi.py`` - Definición del adaptador WSGI del proyecto. Preparado específicamente para su uso en el entorno de producción.
* ``settings/wsgi_staging.py`` - Definición del adaptador WSGI del proyecto. Preparado específicamente para su uso en el entorno de staging.
* ``static`` - Carpeta que contiene todo el contenido estático usado por el proyecto.
* ``templates`` - Carpeta que contiene todas las plantillas que usará el proyecto.
