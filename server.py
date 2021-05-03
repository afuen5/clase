#flask Framework app web (backend-servidor) en python
#tambien esta DJANGO
#Ahora vamos hacer Servidor que responde
#Hogar/punto de inicio = host
#host ocupa una "ventana" = Port
#Host + port = servidor 
#serividor es una direccion
#IP= host
#local host ex(127.0.0.1)
#puerto estandar (http/https): 80
#puerto diferente -> 3000,5000,8000,8001, 8008
 
import logging

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
	return app.send_static_file('BotonDelujo.html')
	
if __name__ == '__main__':
		app.run()