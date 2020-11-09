import os
from flask import Flask, render_template, url_for, request, redirect, jsonify, _app_ctx_stack
# from flask_cors import CORS
from sqlalchemy.orm import scoped_session
from database import models
from database.database import SessionLocal, engine, Base
from utilities.conversions import celsius_to_fahrenheit, fahrenheit_to_celsius
from reactor.pychronium import Pychronium
from reactor.reactor import FlaskReactor
from database.models import Element, Daily, News
from database.elements import periodic_table
from config import ENV
from secrets import LOCAL_DB

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "https://flaskreactor.herokuapp.com"}})
# pg = os.environ.get('DATABASE_URL')

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = LOCAL_DB


# if ENV == 'prod':
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = pg


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SessionLocal()
models.Base.metadata.create_all(bind=engine)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/daily')
def daily():
    e_select = db.query(Daily).all()[0]
    e_info = vars(e_select)
    e_data = list(e_info.items())
    e_list = e_data[1:]
    e_filter = [item for item in e_list if 'symbol' in item]
    e = e_filter[0][1]
    element = {
        "name": "",
        "symbol": "",
        "atomic number": None,
        "melting point": None,
        "boiling point": None,
        "weight": None,
        "phase": "",
        "period": None,
        "class": ""
    }
    for i in periodic_table:
        if i['symbol'] == e:
            element['name'] = i['element']
            element['symbol'] = i['symbol']
            element['atomic number'] = i['atomic number']
            element['class'] = i['class']
            element['melting point'] = i['melting point']
            element['boiling point'] = i['boiling point']
            element['weight'] = i['atomic weight']
            element['phase'] = i['phase']
            element['period'] = i['period']
    return render_template('daily.html', element=element)

@app.route('/chem')
def chem():
    return render_template('chem.html', elements=periodic_table)


@app.route('/chem/<symbol>')
def chem_symbol(symbol):
    element = {
        "name": "",
        "symbol": "",
        "atomic number": None,
        "melting point": None,
        "boiling point": None,
        "weight": None,
        "phase": "",
        "period": None,
        "class": ""
    }
    for i in periodic_table:
        if i['symbol'] == symbol:
            element['name'] = i['element']
            element['symbol'] = i['symbol']
            element['atomic number'] = i['atomic number']
            element['class'] = i['class']
            element['melting point'] = i['melting point']
            element['boiling point'] = i['boiling point']
            element['weight'] = i['atomic weight']
            element['phase'] = i['phase']
            element['period'] = i['period'] 
    print('symbol => ', symbol)
    return jsonify(element)


@app.route('/industry')
def industry():
    news_select = db.query(News).all()
    industry_list = []
    for w in news_select:
        x = vars(w)
        y = list(x.items())
        z = y[1:]
        industry_list.append(z)
    return render_template('industry.html', news=industry_list)

@app.route('/tempconvert/<id>', methods=['GET'])
def convert(id):
    print('id!', id)
    temp = id[:-1]
    units = id[-1:]
    if units == 'F':
        converted = str(round(fahrenheit_to_celsius(float(temp)), 1)) + ' C'
        return jsonify(converted)
    elif units == 'C':
        converted = str(round(celsius_to_fahrenheit(float(temp)), 1)) + ' F'
        return jsonify(converted)


@app.route('/reactor')
def reactor():
    return render_template('reactor.html', elements=periodic_table)

@app.route('/reactor/<reactants>', methods=['GET'])
def reaction(reactants):
    elements = reactants.split('|')
    reaction = False
    el_info = []
    for el in periodic_table:
        if el['element'] == elements[0].lower():
            el_info.append(el)

    for ele in periodic_table:
        if ele['element'] == elements[1].lower():
            el_info.append(ele)
    new_reaction = FlaskReactor(Pychronium(),el_info[0], el_info[1])
    new_reaction.heating()
    new_reaction.magnetic_confinement()
    new_reaction.pychronium_beam_injection('magnetized at 268435456')
    new_element = new_reaction.cooling()
    return jsonify(new_element)


if __name__ == '__main__':
    app.run()