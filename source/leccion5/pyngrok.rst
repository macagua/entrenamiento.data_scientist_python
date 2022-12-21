.. _python_pkg_pyngrok:

PyNgrok
=======

.. note::
    **Propósito:** es una libraría permite usar un proxy inverso que abre
    conexiones seguras desde URL públicas a computador local, hacer demostraciones
    desde su propia máquina y más.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi congue urna
a bibendum rhoncus. Vestibulum ante ipsum primis in faucibus orci luctus et
ultrices posuere cubilia curae; Vestibulum ante ipsum primis in faucibus
orci luctus et ultrices posuere cubilia curae; Donec varius, tortor nec
tristique bibendum, ligula massa suscipit augue, nec finibus magna ante ac
purus. Maecenas eget felis vulputate, lobortis leo at, mattis felis. Quisque
commodo purus vitae velit facilisis gravida. Maecenas vitae viverra justo.
Quisque venenatis tortor eget tortor cursus pulvinar.


.. _python_pkg_pyngrok_instalar:

Instalación
-----------

Para instalar el paquete `pyngrok`_ ejecute el siguiente comando, el cual
a continuación se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install pyngrok

   .. group-tab:: Windows

      .. code-block:: console

          > pip install pyngrok


Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ python -c "import pyngrok ; print(pyngrok.__package__)"

   .. group-tab:: Windows

      .. code-block:: console

          > python -c "import pyngrok ; print(pyngrok.__package__)"


Si muestra el nombre del paquete como ``pyngrok``, tiene correctamente
instalada la paquete. Con esto, ya tiene todo listo para continuar.


.. todo::
    TODO Terminar de escribir esta sección.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion5>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::


.. _`pyngrok`: https://pypi.org/project/pyngrok
