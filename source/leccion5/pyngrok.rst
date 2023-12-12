.. _python_pkg_pyngrok:

PyNgrok
=======

.. note::
    **Propósito:** es una libraría permite usar un proxy inverso que abre
    conexiones seguras desde URL públicas a computador local, hacer demostraciones
    desde su propia máquina y más.

PyNgrok es una librería externa de Python que permite usar ngrok desde un código Python.
ngrok es una herramienta que crea túneles seguros desde URLs públicas a localhost, ideal
para exponer servidores web locales, construir integraciones con webhooks, habilitar acceso
SSH, probar chatbots, hacer demostraciones desde tu propia máquina y más.


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

.. code-block:: python
    :linenos:

    # Importar las librerías necesarias
    from flask import Flask
    from pyngrok import ngrok

    # Crear una aplicación Flask
    app = Flask(__name__)

    # Definir una ruta para el servidor web
    @app.route("/")
    def hello():
        return "Hola, mundo!"

    # Iniciar el servidor web en el puerto 5000
    app.run(port=5000)

    # Abrir un túnel HTTP con PyNgrok en el mismo puerto
    http_tunnel = ngrok.connect(5000)

    # Imprimir la URL pública del túnel
    print(http_tunnel.public_url)

Este código crea un servidor web local que responde con “Hola, mundo!” cuando se accede a la ruta “/”.
Luego, usa PyNgrok para abrir un túnel HTTP en el puerto 5000, que es el mismo que usa el servidor web.
Finalmente, imprime la URL pública del túnel, que se puede usar para acceder al servidor web desde
cualquier navegador.

Espero que este ejemplo te haya ayudado a entender el funcionamiento de PyNgrok. Si quieres saber más sobre
esta librería, puedes consultar su documentación oficial en 3.

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
