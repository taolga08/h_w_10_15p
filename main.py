from flask import Flask

import utils

app = Flask(__name__)


@app.route("/")
def index():
    result = '<br>'
    candidates = utils.get_oll()

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_by_pk(pk)

    if candidate == 'Not Found':
        return 'Not Found'

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'

    return f"""
        <img src="{candidate['picture']}">
        <pre> {result} </pre>
    """
