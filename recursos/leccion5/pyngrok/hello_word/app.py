"""Hello world with pyngrok and Flask"""

from flask import Flask
from pyngrok import ngrok

# Crear una aplicación Flask
app = Flask(__name__)

# Definir una ruta para el servidor web
@app.route("/")
def hola():
    return "Hola, mundo!"

# Iniciar el servidor web en el puerto 5000
app.run(port=5000)

# Abrir un túnel HTTP con PyNgrok en el mismo puerto
http_tunnel = ngrok.connect(5000)

# Imprimir la URL pública del túnel
print(http_tunnel.public_url)
