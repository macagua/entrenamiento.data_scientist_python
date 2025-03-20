.. _python_leccion5:

Reportes y Dashboard
=====================

La **generación de reportes y dashboards interactivos en Python** es una técnica clave para presentar
datos de manera visual y dinámica, permitiendo a los usuarios analizar información de forma intuitiva.
A diferencia de los reportes estáticos, los dashboards interactivos ofrecen la posibilidad de filtrar,
explorar y profundizar en los datos en tiempo real, lo que facilita la toma de decisiones basadas en
información actualizada. Python se ha convertido en un lenguaje popular para la creación de dashboards
gracias a su ecosistema de librerías especializadas en visualización y desarrollo web, proporcionando
herramientas flexibles y escalables para diferentes tipos de usuarios.

Entre las librerías más utilizadas para la creación de dashboards interactivos destacan :ref:`Streamlit <python_pkg_streamlit>`,
`Dash`_ y `Panel`_.

- :ref:`Streamlit <python_pkg_streamlit>` es una opción sencilla y rápida para construir aplicaciones
  interactivas con pocas líneas de código, ideal para científicos de datos y analistas que buscan compartir
  sus modelos y visualizaciones sin necesidad de desarrollar interfaces complejas.

- `Dash`_, basada en :ref:`Flask <python_flask_introduccion>` y :ref:`Plotly <python_pkg_plotly>`, permite
  la creación de dashboards altamente personalizables con componentes interactivos, adecuados para
  aplicaciones empresariales.

- Por otro lado, `Panel`_ es una herramienta poderosa que facilita la integración de diferentes bibliotecas
  de visualización, como :ref:`Matplotlib <python_pkg_matplotlib>`, `Bokeh`_ y :ref:`Plotly <python_pkg_plotly>`,
  para construir interfaces ricas en funcionalidad.

El proceso de construcción de un dashboard interactivo en Python generalmente incluye la **carga y procesamiento
de datos, la generación de gráficos interactivos y la implementación de controles dinámicos** como filtros,
botones y deslizadores. Además, estos dashboards pueden integrarse en aplicaciones web, permitiendo a los usuarios
acceder a ellos desde cualquier dispositivo. La facilidad de implementación y la versatilidad de estas herramientas
han convertido a Python en una de las opciones más populares para la creación de reportes dinámicos y dashboards,
optimizando la comunicación de datos y facilitando la toma de decisiones estratégicas en diversos sectores.

A continuación el temario de esta lección:

.. toctree::
   :maxdepth: 2

   streamlit
   pyngrok

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion5>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`Dash`: https://dash.plotly.com/tutorial
.. _`Panel`: https://panel.holoviz.org/
.. _`Bokeh`: https://bokeh.org/
