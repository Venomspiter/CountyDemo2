from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
@app.route("/")
def render_main():
    return render_template('index.html')
    
def get_state_options(counties):
  for 
    options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
