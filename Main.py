from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/here-is-your-car', methods=['POST'])
def result():
    
    car_brand  = request.form.get('car_brand')
    
    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer
    
    address = get_parked_place()
    
    user = {
        'car_brand' : car_brand,
        'address': address,
        'ticket_amount' : ticket_amount 
    }
    
    #return content
    return render_template('result.html', user=user)

def get_parked_place():
    return '288, Spadina Road'

def get_ticket_amount():
    return 45

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