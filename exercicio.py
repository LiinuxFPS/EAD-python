from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('exercicio.html')

@app.route('/somar/')
@app.route('/somar/<x>/<y>')
def somar(x=0,y=0):
    resultado = float(x)+float(y)
    return str(resultado)


if __name__ == '__main__':
    app.run()