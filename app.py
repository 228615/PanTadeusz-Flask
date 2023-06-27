from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')

def main():
    return 'To jest strona główna'

@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/k1', methods=['GET','POST'])
def index():
    return render_template('k1.html')

@app.route('/k2', methods=['GET','POST'])
def index():
    return render_template('k2.html')

@app.route('/k3', methods=['GET','POST'])
def index():
    return render_template('k3.html')

@app.route('/k4', methods=['GET','POST'])
def index():
    return render_template('k4.html')

@app.route('/k5', methods=['GET','POST'])
def index():
    return render_template('k5.html')

@app.route('/k6', methods=['GET','POST'])
def index():
    return render_template('k6.html')

@app.route('/k7', methods=['GET','POST'])
def index():
    return render_template('k7.html')

@app.route('/k8', methods=['GET','POST'])
def index():
    return render_template('k8.html')

@app.route('/k9', methods=['GET','POST'])
def index():
    return render_template('k9.html')

@app.route('/k10', methods=['GET','POST'])
def index():
    return render_template('k10.html')

@app.route('/k11', methods=['GET','POST'])
def index():
    return render_template('k11.html')

@app.route('/k12', methods=['GET','POST'])
def index():
    return render_template('k12.html')
