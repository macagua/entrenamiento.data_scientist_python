.. _python_pkg_plotly:

Plotly
======

.. note::
    **Propósito:** es una libraría permite la creación de gráficos Plotly para Python

La libraría de gráficos Python de Plotly crea gráficos interactivos con calidad
de publicación. Ejemplos de cómo hacer diagramas de líneas, diagramas de dispersión,
gráficos de área, gráficos de barras, barras de error, diagramas de caja, histogramas,
mapas de calor, subgráficos, gráficos de ejes múltiples, gráficos polares y gráficos
de burbujas.

.. figure:: ../_static/images/plotly_logo.png
    :align: center
    :width: 60%

    Logotipo de librería Plotly


.. _python_pkg_plotly_instalar:

Instalación
-----------

Para instalar el paquete `plotly`_ ejecute el siguiente comando, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install plotly

   .. group-tab:: Windows

      .. code-block:: console

          > pip install plotly


Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python -c "import plotly ; print(plotly.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python -c "import plotly ; print(plotly.__version__)"


Si muestra el numero de la versión instalada de ``plotly``, tiene
correctamente instalada la paquete. Con esto, ya tiene todo listo para continuar.


.. todo::
    TODO Terminar de escribir esta sección.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion5>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
   .. disqus::


.. _`plotly`: https://pypi.org/project/plotly/
