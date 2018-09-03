from app import app
from flask import render_template, request
from matchup import matchup, convert

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

        api_res = matchup(form_res)
        return render_template('result.html', data = api_res)

    return render_template('result.html')
