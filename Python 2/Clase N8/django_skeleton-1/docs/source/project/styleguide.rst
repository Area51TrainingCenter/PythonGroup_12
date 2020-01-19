Guía de estilo para el código del proyecto
==========================================

A continuación se detallan una serie de directivas para el estilo de escritura del código en este proyecto. Si bien estas no son de caracter obligatorio, se recomiendan para escribir código legible y de formato uniforme a lo largo de los proyectos que se irán realizando con el tiempo.


Ancho de línea
--------------
Se utilizará un límite máximo de 80 caracteres para el código escrito de Python.

Nombre de clases y funciones
----------------------------
Se utilizará el estilo ``snake_case`` para los nombres de variables y funciones. Se usará ``CamelCase`` en cambio, para los nombres de clase. Si dos o más variables/métodos están relacionadas de alguna forma, se recomienda nombrarlas con un mismo prefijo. Adicionalmente, todo el código para los proyectos de la empresa debe estar escrito en el idioma inglés.


Saltos de línea
---------------
Se separarán métodos con salto de línea y clases con dos. Se pueden separar secciones de código con un salto de línea si esto aumenta su legibilidad.

Ejemplo:

.. code:: python

    def function():
        return result

    def another_funcion():
        return another_result


    class TestClass:
        def method(self):
            return result

        def another_method(self):
            result = function()
            result = result + 1

            result_extra = another_function()
            return result_extra


Si las líneas de código a escribir sobrepasaran necesariamente el límite de 80 caracteres, estas deben separarse considerando:

1. Si se trata de una secuencia de elementos, la siguiente línea debe empezar donde empezó la definición de la secuencia.

    Ejemplo:

.. code:: python

    def function():
        return [9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
                9999999999, 9999999999, 9999999999, 9999999999, 9999999999]


2. Si el inicio de la definición de la secuencia está muy cerca al límite de caracteres, puede iniciarse la definición de sus elementos en la línea siguiente, en un nivel de indentación superior al de la línea anterior y terminar la definición en una nueva línea.

    Ejemplo:

.. code:: python

    def function():
        return call_to_a_very_long_named_function_with_a_lot_of_params(
            param1, param2, param3, param4, param5
        )


3. Para llamadas a funciones encadenadas, puede separarse la línea utilizando el caracter ``\`` después del punto de la siguiente llamada.

    Ejemplo:

.. code:: python

    def function():
        return call().to().a().very_long().chain().with_a().lot().\
            of_params()


4. Para condicionales que tienen muchos componentes, se prefiere separar los componentes antes del operador lógico de conjunción e indentar la nueva linea dos niveles más allá respecto a la anterior.

    Ejemplo:

.. code:: python

    def function():
        if variable1 == value1 and variable2 == value2 or variable3 == value3 \
                and variable4 == value4 or variable5 == value5:
            return


5. Si una llamada a función tiene una cantidad de argumentos considerable o estos son lo suficientemente largos, se puede optar por poner cada argumento en una única línea.

    Ejemplo:

.. code:: python

    def function():
        return a_function_withlong_arguments(
            the_first_argument=the_first_value,
            the_second_argument=the_second_value,
            the_third_argument=the_third_value
        )


Diccionarios
------------
Para definir diccionarios, se preferirá separar sus componentes en líneas independientes, a menos que se cuente con un elemento únicamente (o no se supere el límite de caracteres). Las llaves de los diccionarios definidos en una sola línea no deben estar rodeadas de espacios.

    Ejemplo:

.. code:: python

    def function():
        return {
            'key': 'value',
            'key2': {'value2': 2},
            'key3': [1, 2, 3],
            'key4': 4 ** 4,
            'key5': 'G'
        }


Imports
-------
El orden sugerido de los imports es el siguiente:

1. Librería estándard de Python
2. Librerías de terceros
3. Módulos locales

En cada nivel, los imports deben ordenarse alfabéticamente y los niveles de imports deben separarse con un salto de línea.


Modelos y Formularios
---------------------
Se sugieren las siguientes reglas para la escritura de modelos y formualrios:

1. Si la definición de las columnas del modelo es lo suficientemente larga, estas se deben escribir separadas con un salto de línea y con sus atributos separados por saltos de línea también.

    Ejemplo:

.. code:: python

    class TestModel(models.Model):
        column1 = models.SomeField(
            attr1=val1,
            attr2=val2,
            # ...
        )

        column2 = models.SomeField(
            attr1=val1,
            attr2=val2,
            # ...
        )


2. El orden sugerido para los atributos de las columnas en los modelos es el siguiente:

* ``max_length``
* ``verbose_name``
* ``choices``
* ``(otros)``
* ``validators``
* ``blank``
* ``null``


Clases
------

Al momento de escribir clases se deben considerar las siguientes sugerencias:

1. El orden de declaración de los componentes de la clase debe ser el siguiente:

* Miembros de clase
* Método ``__new__``
* Método ``__init__``
* Propiedades
* Métodos de clase
* Métodos estáticos
* Métodos de instancia
    * Métodos personalizados
    * Métodos de clases superiores
* Otros métodos mágicos
* Clases de configuración (``Meta``)
