from app import app
from flask import render_template, request
from matchup import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        post_data = request.form
        form_res = {}
        form_res['Name'] = post_data['Name']
        form_res['Roles'] = post_data['Roles']
        res_data = role_winrate(form_res['Roles'])

        return render_template('result.html', data=res_data)


    return render_template('result.html')
