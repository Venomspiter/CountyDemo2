
from flask import Flask, render_template, request, Markup, flash, Markup
import os 
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
def render_fact():
    state = request.args['options']
    return render_template('index.html', stateFact =  state_Fact(state), option = get_state_options())
    

def get_state_options():
        with open('county_demographics.json') as demographics_data:
            counties = json.load(demographics_data)
        options = ""
        state = ""
        for x in counties:
            if  x["State"] != state:
                options += Markup("<option value=\"" + x["State"] + "\">" + x["State"] + "</option>")
                state = x["State"]
        return render_template('index.html', option = options)

@app.route("/")
def render_main():
    return render_fact()

def state_Fact(state):
    with open('county_demographics.json') as demographics_data:
            counties = json.load(demographics_data)
    total = 0
    for c in counties:
        if state == c['state']:
            total = total + c['Population']['2014 Population']
    return MarkUp( "The total number of people living in this state in 2014 was " + total + " people.")
if __name__== '__main__':
    main()
    app.run(debug=False, port=54321)
