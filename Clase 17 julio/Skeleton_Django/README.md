Esqueleto de Django para proyectos de Wunderman Phantasia
=========================================================

Este esqueleto debe usarse para TODOS los proyectos que usen Django.

Una vez descargado, se debe:
  
  * Eliminar la carpeta `.git` y comenzar un proyecto nuevo en un repositorio distinto. **ESTO ES MUY IMPORTANTE. POR FAVOR NO OLVIDAR ESTE PASO.**
  * Crear un nuevo virtualenv e instalar los *requirements*: `pip install -r requirements.txt`. (A menos que se tenga completa conciencia de no querer hacerlo)
  * Comprobar que todo funciona correctamente ejecutando `python settings/manage.py runserver --settings=settings_development`. No debería aparecer ningún mensaje de error y un enlace al home de localhost.
  * Editar `settings/settings.py`, `settings/settings_development.py`, `settings/settings_staging.py` convenientemente. Recordar el cambiar la variable `SECRET_KEY` con un valor completamente aleatorio.
  
Sobre la estructura del esqueleto:

  * Se debe mantener todo el código dentro de la carpeta `apps`, y distribuirlo convenieentemente a través de *apps* (como `common`, y `website`).
  * Las *apps* no necesitan tener archivos obligatorios. No dejar archivos/carpetas vacías o inútiles.
  * Toda la configuración y archivos de inicialización del proyecto deben estar dentro de la carpeta `settings`.
  
Documentación:

  * Leer la documentación ubicada en `docs/build/html/index.html`
  * Si se desea incluir más documentación o nuevos módulos, añadirlos a `docs/source/common/index.rst` y ejecutar (dentro de la carpeta `docs`): `make html`
