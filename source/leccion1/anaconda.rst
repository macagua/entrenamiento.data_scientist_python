.. -*- coding: utf-8 -*-


.. _python_anaconda:

Entorno de desarrollo Anaconda
------------------------------

Este articulo es un tutorial con las instrucciones para instalar la distribución
Anaconda con el instalador para distribuciones Windows 11/Debian GNU/Linux y Python.

Introducción
............

`Anaconda`_, *La distribución más confiable para la ciencia de datos*, es un
administrador de paquetes, un administrador de entorno, una distribución de
ciencia de datos Python/`R`_ y una colección de `más de 8000 paquetes de código abierto`_.

Ofrece una de la forma más fácil de realizar la ciencia de
datos y el aprendizaje automático de Python/`R`_ en los
sistemas operativos Linux, Windows y Mac OS X.

.. figure:: ../_static/images/anaconda_logo.png
    :target: ../_static/images/anaconda_logo.png
    :align: center
    :width: 50%
    :alt: Logotipo de Anaconda

    Logotipo de Anaconda

Es el estándar de la industria para desarrollar, probar y capacitar en
una sola máquina, que permite a *los científicos de datos individuales*
realizar:

-  Descarga rápidamente más de 1500 paquetes de ciencia de
   datos en Python/`R`_.

-  Administre bibliotecas, dependencias y entornos con la herramienta `Conda`_.

-  Desarrolle y capacite modelos de aprendizaje automático (*Machine Learning*)
   y aprendizaje profundo (*Deep Learning*) con las librerías
   `scikit-learn`_, `TensorFlow`_ y `Theano`_.

-  Analice los datos con escalabilidad y rendimiento con las librerías
   `Dask`_, :ref:`NumPy <python_pkg_numpy>`, :ref:`pandas <python_pkg_pandas>` y `Numba`_.

-  Visualice los resultados con las
   librerías :ref:`Matplotlib <python_pkg_matplotlib>`, `Bokeh`_, `Datashader`_ y `Holoviews`_.

Requisitos previos
..................

Para instalar Anaconda debe instalar dependencias mínimas
necesarias, con el siguiente comando:

.. code-block:: console

    sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 \
                     libxrandr2 libxss1 libxcursor1 libxcomposite1 \
                     libasound2 libxi6 libxtst6 wget

Luego debe descargar el instalador de la distribución
Anaconda, ejecutando el siguiente comando:

.. code-block:: console

    wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

Así de esta forma esta listo para ejecutar el instalador de
la distribución Anaconda, en la sección siguiente se explicara como ejecutarlo.


Instalación
...........

Para ejecutar el instalador de la distribución Anaconda,
debe otorgar permisos de ejecución, ejecutando el siguiente
comando:

.. code-block:: console

    chmod 755 ./Anaconda3-2024.10-1-Linux-x86_64.sh

Entonces luego de otorgar permisos de ejecución ya esta
listo para iniciar el instalador de la distribución
Anaconda, ejecutando el siguiente comando:

.. code-block:: console

    ./Anaconda3-2024.10-1-Linux-x86_64.sh

Siga y respondas las preguntas realizadas por el instalador
a continuación. Al finalizar la instalación dispone lo
siguiente paquetes disponibles en Anaconda:

-  Más de `300 paquetes`_ se instalan automáticamente con Anaconda.

-  Más de 8000 paquetes de código abierto adicionales
   (incluida `R`_) se pueden instalar individualmente desde el
   repositorio de Anaconda con el comando :command:`conda install`.

-  Miles de otros paquetes están disponibles en `Anaconda Cloud`_.

-  Puede descargar otros paquetes usando el comando :command:`pip install` que se
   instala con Anaconda. Los `paquetes Pip`_ proporcionan muchas de las características
   de los paquetes ``conda`` y, en algunos casos, pueden funcionar juntos. Sin embargo,
   la preferencia debe ser instalar el paquete ``conda`` si está disponible.

-  También puede crear sus propios `paquetes personalizados`_ utilizando el comando
   :command:`conda build` y puede compartirlos con otros usuarios subiéndolos a
   `Anaconda Cloud`_, PyPi u otros repositorios.

Usted puede instalar, eliminar o actualizar cualquier paquete de Anaconda/Python
con unos pocos clics en `Anaconda Navigator`_ o con un solo comando :command:`conda` en
la consola de comando Anaconda (terminal en Linux o macOS).


Verificar la instalación
........................

Después de instalar Anaconda, si usted prefiere una interfaz
gráfica de usuario (GUI) de escritorio, use *Anaconda
Navigator*. Si prefiere usar la consola de comando Anaconda
(o el terminal en Linux o macOS),  con la herramienta
*conda*. También puedes cambiar entre ellos cuando lo
necesite.

Para usarlo abra la consola de comando en Anaconda activa en
Linux, después elija cualquiera de los siguientes métodos:

-  Si Anaconda está instalado y funcionando, usted puede
   mostrar una lista de los paquetes instalados y sus
   versiones, introduzca el siguiente comando:

.. code-block:: console

    conda list

-  Ejecutar el shell de Python, ejecutando el siguiente
   comando:

.. code-block:: console

   python3

.. code-block:: console

   Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

Si Anaconda está instalado y funcionando, la información de
la versión que muestra cuando se inicia incluirá «Anaconda».

Para salir del shell interactivo Python/Anaconda, ejecutando
el siguiente comando:

.. code-block:: pycon

    >>> quit()

De esta forma verifico que tiene instalado correctamente
instalado la distribución Anaconda.


----


.. _python_anaconda_conda:

Conda
.....

`Conda`_, es una herramienta para administrar e implementar aplicaciones,
entornos y paquetes en Anaconda.

.. figure:: ../_static/images/conda_logo.png
    :target: ../_static/images/conda_logo.png
    :align: center
    :width: 50%
    :alt: Logotipo de CONDA

    Logotipo de CONDA


*Administración de paquetes, dependencias y entornos para cualquier lenguaje —
Python, R, Ruby, Lua, Scala, Java, JavaScript, C / C ++, FORTRAN*

Es un sistema de gestión de paquetes de código abierto el cual le permite:

-  Ser un sistema de gestión del entorno que se ejecuta en
   Windows, macOS y Linux.

-  Instala, ejecuta y actualiza rápidamente los paquetes y
   sus dependencias.

-  Crea, guarda, carga y cambia fácilmente entre los
   entornos de su computadora local.

Fue creado para los programas de Python, pero puede
empaquetar y distribuir software para cualquier lenguaje de
programación. Para más información sobre la herramienta
consulte la `documentación disponible`_.

`Anaconda Navigator`_, es una interfaz gráfica de usuario (GUI) de escritorio
incluida en la distribución de Anaconda® que le permite iniciar aplicaciones y
administrar fácilmente los paquetes, entornos y canales de `Conda`_ sin usar
los comandos de la línea de comandos. El navegador puede buscar paquetes en
`Anaconda Cloud`_ o en un repositorio local de Anaconda. Está disponible para
Windows, macOS y Linux.

Si Anaconda está instalado correctamente, puede abrir el programa gráfico
`Anaconda Navigator`_, el cual se instala automáticamente cuando instala
Anaconda, entonces puede abrirlo, ejecutando el siguiente comando:

.. code-block:: console

      anaconda-navigator


Seguidamente se abrirá la interfaz de `Anaconda Navigator`_ como se muestra a
continuación:

.. figure:: ../_static/images/anaconda_navigator_home.png
    :target: ../_static/images/anaconda_navigator_home.png
    :align: center
    :width: 50%
    :alt: Interfaz de Anaconda Navigator corriendo

    Interfaz de *Anaconda Navigator* corriendo

Este mostrar la Interfaz de `Anaconda Navigator`_ ejecutándose correctamente.


----


Aplicaciones en Anaconda
........................

La distribución de Anaconda incorpora varias aplicaciones para el uso de la
ciencia computacional, a continuación describo las aplicaciones de principal
uso cotidiano:

.. _python_anaconda_spider:

Spyder
......

`Spyder`_, es un entorno integrado de desarrollo en Python para ciencia
computacional, con muchas funcionalidades útiles para la investigación, el
análisis de datos y la creación de paquetes científicos.

Para acceder al entorno integrado accediendo desde el `Anaconda Navigator`_ en
Home > Spyder > Launch, esto ejecutara el entorno integrado, como se muestra a
continuación:

.. figure:: ../_static/images/anaconda_navigator_spyder_python3.png
    :target: ../_static/images/anaconda_navigator_spyder_python3.png
    :align: center
    :width: 50%
    :alt: Interfaz de Spyder corriendo

    Interfaz de *Spyder* corriendo

Este mostrar la Interfaz de *Spyder* ejecutándose correctamente.

Jupyter Notebook
................

`Jupyter Notebook`_, es una aplicación web de código abierto que permite crear y
compartir documentos que contienen código vivo,ecuaciones, visualizaciones y texto
narrativo.

Para acceder al entorno integrado accediendo desde el `Anaconda Navigator`_ en
**Home > Notebook > Launch**, esto ejecutara el entorno integrado, como se muestra
a continuación:

.. figure:: ../_static/images/anaconda_navigator_jupiter_python3.png
    :target: ../_static/images/anaconda_navigator_jupiter_python3.png
    :align: center
    :width: 50%
    :alt: Interfaz de Jupyter Notebook corriendo

    Interfaz de *Jupyter Notebook* corriendo

Este mostrar la Interfaz de `Jupyter Notebook`_ ejecutándose correctamente.

.. tip::

   Para más entender su funcionamiento de la distribución Anaconda
   debe leer la `guía del usuario`_.



Conclusiones
............

De esta forma usted ha aprendido a:

-  **Introductorio** a la distribución Anaconda.

-  **Descargar dependencias** de la distribución Anaconda en Debian.

-  **Instalar** la distribución Anaconda en Debian.

-  **Verificar** la instalación en Debian.

-  **Ejecutar** el `Anaconda Navigator`_.

-  **Abrir aplicaciones** incorporadas en `Anaconda Navigator`_.

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion1>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
   .. disqus::

.. _`Anaconda`: https://www.anaconda.com/
.. _`más de 8000 paquetes de código abierto`: https://www.anaconda.com/docs/tools/working-with-conda/packages/main
.. _`Conda`: https://docs.conda.io/en/latest/
.. _`scikit-learn`: https://scikit-learn.org/stable/
.. _`TensorFlow`: https://www.tensorflow.org/
.. _`Theano`: https://pypi.org/project/Theano/
.. _`Dask`: https://www.dask.org/
.. _`Numba`: http://numba.pydata.org/
.. _`Bokeh`: https://docs.bokeh.org/en/latest/
.. _`Datashader`: https://datashader.org/
.. _`Holoviews`: https://holoviews.org/
.. _`300 paquetes`: https://www.anaconda.com/docs/tools/working-with-conda/packages/main
.. _`R`: https://www.r-project.org/
.. _`Anaconda Cloud`: https://anaconda.org/account/login
.. _`paquetes Pip`: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html
.. _`paquetes personalizados`: https://docs.conda.io/projects/conda-build/en/latest/
.. _`Anaconda Navigator`: https://www.anaconda.com/docs/tools/anaconda-navigator/main
.. _`documentación disponible`: https://docs.conda.io/projects/conda/en/latest/index.html
.. _`Spyder`: https://www.spyder-ide.org/
.. _`Jupyter Notebook`: https://jupyter.org/
.. _`guía del usuario`: https://www.anaconda.com/docs/tools/working-with-conda/main
