from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Contatos')
def Contatos():
    return render_template('Contatos.html')
@app.route('/Procurados')
def Procurados():
    return render_template('Procurados.html')
app.run(debug=True)