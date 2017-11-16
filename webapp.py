from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
if __name__== '__main__':
    main()
    app.run(debug=False, port=54321)
        
def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
   
def get_state_options(counties):
    curState = counties[0]['state']
    options = ""
    for state in counties:
        if state["State"] != curState:
            s = state["State"]
            options += Markup("<option value=\"" + s + "\">" + s + "</option>")
            curState = state["State"]
    return options

@app.route("/")
def render_main():
    #return render_template('index.html', stateBlock = get_state_options(), stateFact = state_Fact())
    return render_template('index.html', stateBlock = get_state_options())
    
"""def state_Fact(state, counties):
    total = 0
     for c in counties:
            if state == c['state']:
                total = total + c['Population']['2014 Population']
     return "The total number of people living in this state in 2014 was " + total + " people."
     """
    
