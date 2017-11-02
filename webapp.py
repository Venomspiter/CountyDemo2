from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
if __name__== '__main__':
    main()
    app.run(debug=False, port=54321)
    
@app.route("/")
def render_main():
    return render_template('index.html')
    
def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties)) 
   
def get_state_options(counties):
    options = ""
    for s in counties:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
def Markup(str):
    
