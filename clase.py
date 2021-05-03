from flask import render_template, request

app =Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return '<h1> Bienvenido</h1>'

@app.route('/autor', methods=['GET'])
def autor():
	return '<h2>Hola</h2>'

@app.route('/alcohol', methods=['GET'])
def alcohol():
	if request.method == 'POST':

		alcohol = request.form.get('alcohol')
		if alcohol == 'cheve' or alcohol == 'cerveza':
			alcohol = 'cerveza'

			if alcohol == 'tequila':
				alcohol = 'que perro asco'

		return '''

		<hr>
		<h2>Elegiste {} !</h2>
		<hr>

		'''.format(alcohol)
		#hacer algo si es post
	else:
		#es un GET
		return '''

		<form method="POST">
		<hr>
		<h3>Elige un alcohol:</h3>
		<input type='text' name='alcohol'><br>
		<input type='submit' value='A tomar!'>

		</form>
		'''

		app.run()
