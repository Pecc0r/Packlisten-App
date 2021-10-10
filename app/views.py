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
    payload["slider"] = int(payload["slider"])
    packliste = {
      "Infrastruktur":[],
      "Kleidung":[],
      "Kochen":[],
      "Hygiene":["Hörgeräte", "Maske"],
    }
    if "ultralight" in payload["checkboxes"]:
        if "fahrrad" in payload["checkboxes"] and "wandern" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["UL-Zelt", "Fahrrad", "Fahrradhelm", "Wanderstöcke", "Wanderrucksack", "Schlafsack", "Luftmatratze", "Heringe", "Kissen", "Iso-Sitzmatte", "Stirnlampe", "Powerbank", "Stempelhefte"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "3 Unterhosen", "Wanderschuhe", "Jacke/Cape", "Sonnenbrille"]
           packliste["Kochen"] += ["UL-Kocher", "X-Bowl", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Pflaster", "Sonnencreme", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
        elif "fahrrad" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["UL-Zelt", "Fahrrad", "Fahrradhelm", "Schlafsack", "Isomatte", "Heringe", "Kissen", "Iso-Sitzmatte"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "Unterhosen"]
           packliste["Kochen"] += ["UL-Kocher", "X-Bowl", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
        elif "wandern" in payload["checkboxes"]:
           packliste["Infrastruktur"] += ["UL-Zelt", "Wanderstöcke", "Wanderrucksack", "Schlafsack", "Isomatte", "Heringe", "Kissen", "Iso-Sitzmatte"]
           packliste["Kleidung"] += ["Buff", "Sporthose", "Wandersocken", "Sportkleid", "Merinopulli", "BH", "Unterhosen"]
           packliste["Kochen"] += ["UL-Kocher", "X-Bowl", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
           packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "Handtuch", "Schminke"]
    else:
        if "wandern" in payload["checkboxes"]:
            packliste["Infrastruktur"] += ["Wanderstöcke", "Wanderrucksack", "Stempelhefte"]
        if "fahrrad" in payload["checkboxes"]:
            packliste["Infrastruktur"] += ["Fahrrad", "Fahrradhelm"]
        if "auto" in payload["checkboxes"]:
             packliste["Infrastruktur"] += ["Schlafsack", "Isomatte", "Kissen", "Stuhl"]
             packliste["Kochen"] += ["Gaskocher", "Infrastrukturbox", "Hauptmahlzeiten", "Wasserflaschen"]
             packliste["Hygiene"] += ["Hörgeräte", "Bürste", "Deo", "Zahnbürste", "UL-Handtuch", "Schminke"]
             if not "zelten" in payload["checkboxes"]:
                 payload["checkboxes"].append("zelten")
        if "zelten" in payload["checkboxes"]:
            packliste["Infrastruktur"] += ["Zelt", "Heringe"]
        if "camper" in payload["checkboxes"]:
            packliste["Infrastruktur"] += ["Palettenkissen", "Heckzelt", "Kissen", "Decke", "Stühle"]
            packliste["Kleidung"] += ["Buff", "Schlafsachen", "Socken", "BH"]
            packliste["Kochen"] += ["Gaskocher", "Gas", "Titanlöffel", "Hauptmahlzeiten", "Wasserflaschen", "Trailmix"]
            if "fahrrad" in payload["checkboxes"]:
                packliste["Infrastruktur"] += ["Fahrradträger"]
        if "glamping" in payload["checkboxes"]:
            if "camper" in payload["checkboxes"]:
                packliste["Infrastruktur"] += ["Teppich", "Heizung"]
                packliste["Kleidung"] += ["Kleider",]
        if payload["slider"] > 1:
            if "glamping" in payload["checkboxes"]:
                packliste["Kleidung"].append(f"{payload['slider'] * 2} Unterhosen")
            else:
                packliste["Kleidung"].append(f"{payload['slider'] + 2} Unterhosen")
    return Response(
      json.dumps(packliste),
      mimetype = "application/json"
    )
