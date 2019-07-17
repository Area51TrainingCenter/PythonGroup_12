Instalación
===========

El esqueleto de desarrollo requiere de las siguientes dependencias, cuya instalación varía en relación al sistema operativo.

* ``Python > 2.7.10 && < 3.0 (incluyendo cabeceras de desarrollo)``
* ``pip + virtualenv (pip viene con Python en últimas versiones)``
* ``virtualenvwrapper (opcional/recomendado)``
* ``MySQL 5.X (incluyendo cabeceras de desarrollo)``
* ``gcc``
* ``libpng``
* ``libjpeg``
* ``zlib``

1. Una vez instaladas las dependencias, el repositorio perteneciente al esqueleto debe clonarse (si no se cuenta ya con una copia) usando git:

::

    > git clone git@bitbucket.org:wunderman-phantasia/django_skeleton.git

*Nota: si se está trabajando con el* ``project_skeleton`` *este contiene el esqueleto de backend y no es necesario realizar este paso.*

2. Activar el virtualenv del proyecto. En la mayoría de casos basta con tener un único virtualenv para todos los proyectos que se hagan con el presente skeleton ya que se asume que se usa la última versión estable de los paquetes necesarios y las dependencias adicionales propias del proyecto no tendrían que tener problemas entre sí.

::

    # virtualenvwrapper: Para crear el virtualenv (nombrado 'env')
    > mkvirtualenv env

    # virtualenvwrapper: Para volver a activarlo, o cambiar entre virtualenvs
    > workon env

    # virtualenv: Para crear el virtualenv (nombrado 'env')
    > virtualenv env

    # Para desactivar el virtualenv
    > deactivate

3. Instalar los paquetes requeridos por el proyecto en el virtualenv (es necesario activarlo primero). Los paquetes a instalar se encuentran definidos en el archivo ``requirements.txt`` ubicado en la raíz del esqueleto:

::

    > pip install -r requirements.txt

4. Lanzar el proyecto de prueba incluido en el esqueleto para verificar su correcto funcionamiento:

::

    > python settings/manage.py runserver --settings=settings_development
    Performing system checks...

    System check identified no issues (0 silenced).
    Jan 01, 2016 - 00:00:00
    Django version 1.9.6, using settings 'settings_development'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
