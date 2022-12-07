import os, logging
from datetime import datetime
from flask import Flask, jsonify, request, redirect, render_template, url_for
from flask_cors import CORS

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
CORS(app)

@app.errorhandler(500)
def general_app_error(e):
    """ General Error Hanlder
        returns 500 on invocation
    """
    return jsonify(error=str(e)), 500

@app.route('/')
def appRoot():
    person = {'name': 'PR request 1', 'birth-year': 2001}
    return jsonify(person)

@app.route('/map')
def map():
    r = jsonify({'type':'FeatureCollection',
    'features': [
        {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1674,
             36.1263
             ]},
    'properties':{
        'title': "Encore",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1745,
             36.1162
             ]},
    'properties':{
        'title': "Caesars Palace",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1703,
             36.1025
             ]},
    'properties':{
        'title': "MGM Grand",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 100
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1697,
             36.1212
             ]},
    'properties':{
        'title': "Venetian",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1749,
             36.0920
             ]},
    'properties':{
        'title': "Mandalay Bay",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1721,
             36.1247
             ]},
    'properties':{
        'title': "Treasure Island",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1741,
             36.1212
             ]},
    'properties':{
        'title': "Mirage",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1712,
             36.1197
             ]},
    'properties':{
        'title': "LINQ",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1726,
             36.1180
             ]},
    'properties':{
        'title': "Flamingo",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1708,
             36.1164
             ]},
    'properties':{
        'title': "Bellagio",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1379,
             36.1098
             ]},
    'properties':{
        'title': "Bellagio",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1379,
             36.1098
             ]},
    'properties':{
        'title': "Cosmo",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1758,
             36.1076
             ]},
    'properties':{
        'title': "Aria",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1667,
             36.1062
             ]},
    'properties':{
        'title': "MGM Signature",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 10
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -115.1773,
             36.0931
             ]},
    'properties':{
        'title': "Delano",
        'cluster': False,
        'venue': 'blackcat',
        'event_count': 5
    }
    },
    ]})
    return r

if __name__ == "__main__":

    if os.getenv('ENVIRONMENT') is not None:
        app.config['environment'] = os.getenv('ENVIRONMENT')
    else:
        app.config['environment'] = "dev"

    app.run(debug=False, host='0.0.0.0', port=os.getenv("PORT", default=8080))