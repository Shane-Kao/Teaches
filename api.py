# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import json

from flask import Flask, request, Response, redirect, render_template

from configs import API
from url import URL

app = Flask(__name__)


@app.route('/short_url', methods=['GET'])
def get_short_url():
    if request.method == "GET":
        url = request.args.get('url')
        url = URL(raw_url=url)
        return Response(
            response=json.dumps({"short_url": url.short_url}, ensure_ascii=False),
            mimetype="application/json",
            status=200
        )
    else:
        return Response(response="Method Not Allowed", mimetype="application/json", status=405)


@app.route('/short2raw', defaults={'path': ''})
@app.route('/short2raw/<path:path>')
def short2raw(path):
    return redirect(URL.short2raw[request.url])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=API.port.value)
