Utilización de URLs Dinámicas
=============================

Con el fin de estandarizar el uso de URLs y parámetros en la configuración de proyectos utilizando Django, se presenta el siguiente Guideline.


Configuración de URLS
---------------------
En los archivos de configuración settings.py de cada entorno (``settings_development.py``, ``settings_staging.py`` y ``settings.py``) deberán especificarse las tres siguientes variables:

* ``DOMAIN_URL``: Deberá especificar el nombre del dominio en el que se está trabajando, dependiendo del contexto en el que se ejecute el proyecto. **No** deberá contener un trailing slash (slash al final de la ruta).
* ``RELATIVE_URL``: Deberá especificar la ruta relativa en la que se ejecuta el proyecto. Si el proyecto se encuentra en la raíz, deberá ser una cadena vacía. **No** deberá contener un trailing slash (slash al final de la ruta).
* ``STATIC_URL``: Por default, este campo tiene el valor ``/static/``. En caso de que el proyecto, se ejecute en una ruta relativa en el dominio de ejecución, esta ruta relativa deberá ser agregada al inicio de la cadena, precedida por la palabra ``/static/``.  **Sí** llevará un slash inicial.


Ejemplos de configuraciones
---------------------------

Ambiente de Desarrollo
^^^^^^^^^^^^^^^^^^^^^^
Teniendo en cuenta que el proyecto corre en nuestro localhost y en el puerto ``8000``, entonces:

``settings_development.py``::

    DOMAIN_URL = 'http://localhost:8000'
    RELATIVE_URL = ''
    STATIC_URL = '/static/'


Ambiente de Pruebas (Staging)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Teniendo en cuenta que el proyecto se ejecuta en una URL de la forma ``http://marca-campana-staging.phantasia.pe``, entonces:

``settings_staging.py``::

    DOMAIN_URL = 'http://marca-campana-staging.phantasia.pe'
    RELATIVE_URL = ''
    STATIC_URL = '/static/'


Ambiente de Producción
^^^^^^^^^^^^^^^^^^^^^^
Teniendo en cuenta que el proyecto se ejecuta en una URL de la forma ``http://marca.com/campana``, entonces:

``settings.py``::

    DOMAIN_URL = 'http://marca.com'
    RELATIVE_URL = '/campana'
    STATIC_URL = '/campana/static/'


Uso de reverse y reverse_lazy
-----------------------------
Las funciones ``reverse`` y ``reverse_lazy`` nos devuelven la URL de una vista declarada en los archivos ``urls.py`` de nuestras apps, utilizando los nombres y namespaces definidos:

``settings/urls.py``::

    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^', include('website.urls', namespace='website')),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Notar que se incluyó la app ``website`` identificada con la propiedad ``namespace`` ``website``. Esta propiedad nos servirá para poder hacer ``reverse`` apropiadamente.


``website/urls.py``::

    urlpatterns = [
        url(r'^register/$', views.PlayerView.as_view(), name='register'),
    ]

Se incluyó la vista PlayerView, identificada con la propiedad ``name`` ``register``, para la ruta indicada. Esta propiedad nos servirá para poder hacer ``reverse`` apropiadamente.


``website/views.py``::

    class PlayerView(TemplateView):
        template_name = register.html'
        success_url = reverse("website:register")

Usamos la función ``reverse`` mandando una cadena con el formato ``namespace:name``, de acuerdo a la configuración en los archivos urls.py vista previamente. Lo que devolverá esta función será lo siguiente (dependiendo del contexto en el que se encuentre ejecutándose la aplicación):

* Ambiente de desarrollo (localhost): ``/register``
* Ambiente de Pruebas (Staging): ``/register``
* Ambiente de Producción ``/campana/register``


Trabajando con Envío de Mails
-----------------------------
Cuando se envían mails, es importante indicarle al template las rutas de los archivos estáticos (imágenes, fuentes y otros recursos). La forma en que estos templates resuelven una ruta estática es a través del uso de los tags de Django::

    src="{% static 'images/orientation-sm.png' %}"

Sin embargo, estos tags resuelven una ruta relativa, la cual resulta inútil para el envío de mails, donde se precisa una ruta global para todos los recursos usados. Para resolver esto, es necesario indicar la URL del dominio antes de la ruta relativa del recurso. Habiendo hecho las configuraciones correspondientes en ``settings.py`` (dependiendo del contexto de ejecución del proyecto), se recomienda enviar la variable ``DOMAIN_URL`` como parte del contexto del template, para que se configura de la siguiente manera::

    src="{{ DOMAIN_URL }}{% static 'images/orientation-sm.png' %}"

De esta manera se asegura que todos los recursos mostrados en los clientes de mail sean rutas globales. Tomar en cuenta que el tag ``static`` resolverá la URL estática con el valor de ``STATIC_URL``; asegurarse que esta esté configurada correctamente dependiendo del contexto de ejecución del proyecto.
