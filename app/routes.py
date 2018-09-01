from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        res = request.form
        print(dict(res))
        return render_template('result.html', data = res)

    return render_template('result.html')
