from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        peso = float(request.form['peso'])
        tamano = request.form['tamano']
        actividad = request.form['actividad']
        castrado = request.form['castrado']
        raza = request.form['raza']
        edad = float(request.form['edad'])
        pauta = pauta_alimenticia_barf(peso, tamano, actividad, castrado, raza, edad)
        return render_template('respuesta.html', pauta=pauta)
    return render_template('formulario.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    peso = float(request.form['peso'])
    tamano = request.form['tamano']
    actividad = request.form['actividad']
    castrado = request.form['castrado']
    raza = request.form['raza']
    edad = float(request.form['edad'])
    pauta = pauta_alimenticia_barf(peso, tamano, actividad, castrado, raza, edad)
    return render_template('respuesta.html', pauta=pauta)

def pauta_alimenticia_barf(peso, tamano, actividad, castrado, raza, edad):
    cantidad_total = peso * (2 if actividad == 'baja' else 3) / 100
    cantidad_carne = cantidad_total * 0.7
    cantidad_huesos = cantidad_total * 0.1
    cantidad_frutas_verduras = cantidad_total * 0.1
    cantidad_lacteos = cantidad_total * 0.05
    cantidad_aceites_grasas = cantidad_total * 0.05
    return {
        "carne": cantidad_carne,
        "huesos": cantidad_huesos,
        "frutas_verduras": cantidad_frutas_verduras,
        "lacteos": cantidad_lacteos,
        "aceites_grasas": cantidad_aceites_grasas,
        "total": cantidad_total,
    }

if __name__ == '__main__':
    app.run(debug=True)