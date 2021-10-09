from flask import render_template,flash, redirect, request, jsonify, Response
from app import app
import json
import os

@app.route('/', methods=("GET", "POST"))
def index():
    return render_template("index.html",
                           title='VSUP - Meteogram',
                           )

@app.route('/api/packliste', methods=("POST",))
def packliste():
    payload=request.get_json(force = True)
    print(payload)
    return Response(
      json.dumps({}),
      mimetype = "application/json"
    )
