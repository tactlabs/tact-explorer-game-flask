from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

'''
    http://localhost:5000/country_code?country=india
'''
@app.route('/country_code')
def find_country_code():

    country  = request.args.get('country')

    code = get_country_code(country)

    print('code : ', code)

    result = {
        'country' : country,
        'code': code
    }
    
    #return content
    return render_template('country-code.html', result=result)

'''
    http://localhost:5000/show/map
'''
@app.route("/show/map" , methods=['POST'])
def show_map():

    country1  = request.form.get('country1')
    country2  = request.form.get('country2')

    code1 = get_country_code(country1)
    code2 = get_country_code(country2)

    latlong1 = get_lat_long(code1)
    latlong2 = get_lat_long(code2)

    #print('code1 : ', code1)

    result = {
        'country1' : country1,
        'code1': code1,
        'latlong1': latlong1,

        'country2' : country2,
        'code2': code2,
        'latlong2': latlong2
    }
    
    #return content
    return render_template('countrymap.html', result=result)    


@app.route('/samplemap')
def get_sample_map():
    return render_template('sample-map.html')    


def get_lat_long(country_code):

    with open('assets/countrycode-latlong-array.json') as f:
        data = json.load(f)

    return data[country_code]    

def get_country_code(country):

    with open('assets/countries.json') as f:
        data = json.load(f)

    #print(data['country_codes'])

    codes = data['country_codes']

    for item in codes:
        #print(item)

        if(item['name'].lower() == country):
            return item['code'].lower()

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/
    
    https://www.learnpython.org/en/String_Formatting
    
    https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    
    https://github.com/googlemaps/google-maps-services-python
    
    AIzaSyCRhRz_mw_5wIGgF-I6PUy3js6dcY6zQ6Q
    
    Get Current Location:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
'''