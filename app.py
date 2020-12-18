# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import re
import json

from flask import Flask, request, Response, redirect, render_template

from configs import API
from url import URL

app = Flask(__name__)


@app.route('/short_url', methods=['GET'])
def get_short_url():
    if request.method == "GET":
        url = request.args.get('url')
        if not re.match(r"(?P<URL>http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|("
                        r"?:%[0-9a-fA-F][0-9a-fA-F]))+)", url):
            return Response(
                status=400,
                response=json.dumps({"msg": "Invalid url"}, ensure_ascii=False),
                mimetype="application/json"
            )
        url = URL(raw_url=url)
        try:
            short_url = url.short_url
        except Exception as e:
            return Response(
                status=500,
                response=json.dumps({"msg": str(e)}, ensure_ascii=False),
                mimetype="application/json",
            )
        return Response(
            response=json.dumps({"short_url": short_url}, ensure_ascii=False),
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
