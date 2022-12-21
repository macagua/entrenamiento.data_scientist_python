.. _python_pkg_matplotlib:

Matplotlib
==========

.. note::
    **Propósito:** es una librería de Python especializada en la creación de
    gráficos en dos dimensiones.

Permite crear y personalizar los tipos de gráficos más comunes, entre ellos:

-  Diagramas de barras.

-  Histograma.

-  Diagramas de sectores.

-  Diagramas de caja y bigotes.

-  Diagramas de violín.

-  Diagramas de dispersión o puntos.

-  Diagramas de lineas.

-  Diagramas de areas.

-  Diagramas de contorno.

-  Mapas de color.

y combinaciones de todos ellos.

En la siguiente `galería de gráficos <https://matplotlib.org/gallery/index.html>`_
pueden apreciarse todos los tipos de gráficos que pueden crearse con esta librería.

.. figure:: ../_static/images/matplotlib_logo.png
    :align: center
    :width: 60%

    Logotipo de librería Matplotlib


.. _python_pkg_matplotlib_instalar:

Instalación
-----------

Para instalar el paquete `matplotlib`_ ejecute el siguiente comando, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install matplotlib

   .. group-tab:: Windows

      .. code-block:: console

          > pip install matplotlib


Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python -c "import matplotlib ; print(matplotlib.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python -c "import matplotlib ; print(matplotlib.__version__)"


Si muestra el numero de la versión instalada de ``matplotlib``, tiene
correctamente instalada la paquete. Con esto, ya tiene todo listo para continuar.

.. todo::
    TODO Terminar de escribir esta sección.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`matplotlib`: https://pypi.org/project/matplotlib/
