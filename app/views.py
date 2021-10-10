from flask import render_template,flash, redirect, request, jsonify, Response
from flask import after_this_request
from flask_cors import CORS
from app import app
import json
import os

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html",
                           title='Packlistengenerator',
                           )

@app.route('/api/packliste', methods=["POST"])
def packliste():
    payload=request.get_json(force = True)
    print(payload)
    packliste = {
      "Infrastruktur":[],
      "Kleidung":[],
      "Kochen":[],
      "Hygiene":[],
    }
    if "ultralight" in payload["checkboxes"]:
        if "fahrrad" in payload["checkboxes"] and "wandern" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["UL-Zelt", "Fahrrad", "Fahrradhelm", "Wanderstöcke", "Wanderrucksack", "Schlafsack", "Isomatte", "Heringe", "Kissen", "Iso-Sitzmatte"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "Unterhosen"]
           packliste["Kochen"] += ["UL-Kocher", "X-Bowl", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
        elif "fahrrad" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["UL-Zelt", "Fahrrad", "Fahrradhelm", "Schlafsack", "Isomatte", "Heringe", "Kissen", "Iso-Sitzmatte"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "Unterhosen"]
           packliste["Kochen"] += ["UL-Kocher", "X-Bowl", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
        elif "wandern" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["UL-Zelt", "Wanderstöcke", "Wanderrucksack", "Schlafsack", "Isomatte", "Heringe", "Kissen", "Iso-Sitzmatte"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "Unterhosen"]
           packliste["Kochen"] += ["UL-Kocher", "X-Bowl", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
    elif "glamping" in payload["checkboxes"]:
        if "fahrrad" in payload["checkboxes"] and "camper" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["Fahrrad", "Fahrradhelm", "Palettenkissen", "Heckzelt", "Kissen", "Decke"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "Unterhosen"]
           packliste["Kochen"] += ["Gaskocher", "Gas", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
        if "camper" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["Palettenkissen", "Heckzelt", "Kissen", "Decke"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "Unterhosen"]
           packliste["Kochen"] += ["Gaskocher", "Gas", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
    return Response(
      json.dumps(packliste),
      mimetype = "application/json"
    )
