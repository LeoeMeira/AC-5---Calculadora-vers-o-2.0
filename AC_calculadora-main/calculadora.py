import math
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    print('02')
    return render_template('calc.html')


@app.route('/calculadora', methods=['POST'])
def calcular():
    print('teste')
    valor1 = int(request.form['v1'])
    valor2 = int(request.form['v2'])
    operacao = request.form['operacao'].upper()
    if operacao == 'SOMA':
        resultado = valor1 + valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'SUB':
        resultado = valor1 - valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'MULT':
        resultado = valor1 * valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'DIV':
        if valor2 == 0:
            return '<h1>Não existe divisão por zero</h1>'
        resultado = valor1 / valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'RAIZ':
        resultado = math.sqrt(valor1)
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'EXP':
        resultado = valor1 ** valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'LOG':
        resultado = math.log(valor1)
        return render_template('resultado.html', resultado=resultado)
    else:
        return '<h1> Operação inválida </h1>'


app.run(debug=True)
