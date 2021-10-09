from flask import render_template,flash, redirect, request, jsonify
from app import app
import json
import os

@app.route('/', methods=("GET", "POST"))
def index():
    return render_template("index.html",
                           title='VSUP - Meteogram',
                           )
