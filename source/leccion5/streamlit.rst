.. _python_pkg_streamlit:

Streamlit
=========

.. note::
    **Propósito:** es una libraría permite la creación de Dashboard interactivos.

Es un framework de aplicación de código abierto (un paquete de Python) que nos
brinda el poder de crear aplicaciones atractivas sin ningún conocimiento de
desarrollo de front-end.

Esto nos libera de involucrarnos en cualquier marco de trabajo front-end o codificación
en HTML, CSS y JavaScript.

Utiliza Python puro para desarrollar su front-end.

.. figure:: ../_static/images/streamlit_logo.png
    :align: center
    :width: 60%

    Logotipo de librería Streamlit


¿Cuándo usar Streamlit?
-----------------------

En primer lugar, si está codificando secuencias de comandos de Python que se ejecutan
regularmente en una máquina con un programador de trabajos como cron, Streamlit no es útil
para usted.

Pero si está desarrollando una herramienta que desea compartir con los miembros de su equipo,
por ejemplo, una aplicación de investigación de palabras clave, puede usar Streamlit.

Además, si necesita un método de autenticación de usuario, la comunidad Streamlit desarrolló
un paquete que puede manejarlo por usted.


.. _python_pkg_streamlit_instalar:

Instalación
-----------

Para instalar el paquete `streamlit`_ ejecute el siguiente comando, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install streamlit

   .. group-tab:: Windows

      .. code-block:: console

          > pip install streamlit


Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python -c "import streamlit ; print(streamlit.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python -c "import streamlit ; print(streamlit.__version__)"


Si muestra el numero de la versión instalada de ``streamlit``, tiene
correctamente instalada la paquete. Con esto, ya tiene todo listo para continuar.


.. _python_pkg_streamlit_hello:

Práctica - Hello
----------------

A continuación se presenta la ejecución de una demostración que incluye ``Streamlit``,
ejecutando el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ streamlit hello

   .. group-tab:: Windows

      .. code-block:: console

          > streamlit hello


El anterior comando al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Welcome to Streamlit. Check out our demo in your browser.

    Local URL: http://localhost:8501
    Network URL: http://172.28.94.109:8501

    Ready to create your own Python apps super quickly?
    Head over to https://docs.streamlit.io

    May you create awesome apps!

``Local URL``
    Dirección local de tu PC donde ejecuta esta demostración, valor por
    defecto es **http://localhost:8501**

``Network URL``
    Dirección de la red local de tu PC donde donde puede compartir la forma
    como accede a esta demostración.

Abra el navegador web en la dirección local definida en el valor ``Local URL``:

.. figure:: ../_static/images/streamlit_hello_index.png
    :align: center
    :width: 60%

    Streamlit Hello - Welcome to Streamlit! 👋

----

.. figure:: ../_static/images/streamlit_hello_animation_demo.png
    :align: center
    :width: 60%

    Streamlit Hello - Animation Demo

Esta aplicación muestra cómo puede usar Streamlit para crear animaciones
geniales. Muestra un fractal animado basado en el conjunto de Julia. Utilice
el control deslizante para ajustar diferentes parámetros.

----

.. figure:: ../_static/images/streamlit_hello_plotting_demo.png
    :align: center
    :width: 60%

    Streamlit Hello - Plotting Demo

Esta demostración ilustra una combinación de Plotting y animación con Streamlit.
En este ejemplo se genera un montón de números aleatorios en un bucle durante
unos 5 segundos.

----

.. figure:: ../_static/images/streamlit_hello_mapping_demo.png
    :align: center
    :width: 60%

    Streamlit Hello - Mapping Demo

Esta demostración muestra cómo usar st.pydeck_chart para mostrar datos geoespaciales.


----

.. figure:: ../_static/images/streamlit_hello_dataframe_demo.png
    :align: center
    :width: 60%

    Streamlit Hello - DataFrame Demo

Esta demostración muestra cómo usar st.write para visualizar Pandas DataFrames.
(Datos cortesía de `UN Data Explorer <http://data.un.org/Explorer.aspx>`_).

.. _python_pkg_streamlit_hello_word:

Práctica - Hello World
----------------------

A continuación se presenta una práctica del famoso `Hello World`_ usando con ``Streamlit``,
a continuación la estructura de proyecto llamado ``hello_word``:

.. code-block:: console

    hello_word/
    ├── __init__.py
    ├── app.py
    └── requirements.txt

A continuación se presenta y explica el uso de cada archivo para esta proyecto:

*Archivo app.py*

Modulo de principal del programa.

.. literalinclude:: ../../recursos/leccion5/hello_word/app.py
    :language: python
    :linenos:
    :lines: 1-3

*Archivo requirements.txt*

Archivo de `requirements.txt`_ de la herramienta de gestión de paquetes `pip`_.

.. literalinclude:: ../../recursos/leccion5/hello_word/requirements.txt
    :language: text
    :linenos:
    :lines: 1-1

A continuación se presenta la ejecución de una demostración personalizada de `Hello World`_,
ejecutando los siguientes comandos correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install -r hello_word/requirements.txt
          $ streamlit run hello_word/app.py

   .. group-tab:: Windows

      .. code-block:: console

          > pip install -r hello_word/requirements.txt
          > streamlit run hello_word/app.py


El anterior comando al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://172.28.94.109:8501

``Local URL``
    Dirección local de tu PC donde ejecuta esta demostración, valor por
    defecto es **http://localhost:8501**

``Network URL``
    Dirección de la red local de tu PC donde donde puede compartir la forma
    como accede a esta demostración.

Abra el navegador web en la dirección local definida en el valor ``Local URL``:

.. figure:: ../_static/images/streamlit_hello_world.png
    :align: center
    :width: 60%

    Streamlit - Hello World


.. _python_pkg_streamlit_dashboard:

Práctica - Dashboard
--------------------

A continuación se presenta una práctica de un Dashboard de análisis de ventas de
tres (03) sucursales a nivel nacional de una cadena de supermercado usando
con ``Streamlit``, a continuación la estructura de proyecto llamado ``dashboard``:

.. code-block:: console

    dashboard/
    ├── app.py
    ├── __init__.py
    ├── requirements.txt
    ├── .streamlit
    │   └── config.toml
    └── ventas_supermercado.xlsx

A continuación se presenta y explica el uso de cada archivo para esta proyecto:

*Archivo app.py*

Modulo de principal del programa.

.. literalinclude:: ../../recursos/leccion5/dashboard/app.py
    :language: python
    :linenos:
    :lines: 1-137

*Archivo .streamlit/config.toml*

Archivo de configuración de proyecto Streamlit.

.. literalinclude:: ../../recursos/leccion5/dashboard/.streamlit/config.toml
    :language: python
    :linenos:
    :lines: 1-16

*Archivo requirements.txt*

Archivo de `requirements.txt`_ de la herramienta de gestión de paquetes `pip`_.

.. literalinclude:: ../../recursos/leccion5/dashboard/requirements.txt
    :language: text
    :linenos:
    :lines: 1-4

*Archivo ventas_supermercado.xlsx*

Archivo de la hoja de calculo de ``Microsoft Excel`` llamado :file:`ventas_supermercado.xlsx`
la cual no se incluye ya que cada vez que se inicia el programa :file:`app.py`, para cuidar la
creación de los datos iniciales.

.. figure:: ../_static/images/streamlit_ventas_supermercado_xlsx.png
    :align: center
    :width: 60%

    Archivo de Excel ventas_supermercado.xlsx

A continuación se presenta la ejecución de una demostración personalizada de ``Tablero de Ventas``,
ejecutando los siguientes comandos correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install -r dashboard/requirements.txt
          $ streamlit run dashboard/app.py

   .. group-tab:: Windows

      .. code-block:: console

          > pip install -r dashboard/requirements.txt
          > streamlit run dashboard/app.py


El anterior comando al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://172.28.94.109:8501

``Local URL``
    Dirección local de tu PC donde ejecuta esta demostración, valor por
    defecto es **http://localhost:8501**

``Network URL``
    Dirección de la red local de tu PC donde donde puede compartir la forma
    como accede a esta demostración.

Abra el navegador web en la dirección local definida en el valor ``Local URL``:

.. figure:: ../_static/images/streamlit_tablero_ventas.png
    :align: center
    :width: 60%

    Streamlit - Tablero de Ventas


.. todo::
    TODO Terminar de escribir esta sección.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion5>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::


.. _`streamlit`: https://pypi.org/project/streamlit/
.. _`requirements.txt`: https://pip.pypa.io/en/stable/reference/requirements-file-format/
.. _`pip`: https://pip.pypa.io/en/stable/
.. _`Hello World`: https://es.wikipedia.org/wiki/Hola_mundo
