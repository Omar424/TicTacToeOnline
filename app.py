from flask import Flask, render_template, jsonify,request
import json
from random import randrange
from alla_funktioner import *
app = Flask('app')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/offline')
def offline_tictactoe():
    return render_template("offline_tictactoe.html")

@app.route('/join',methods = ['POST', 'GET'])
def join():
    #Sparar informationen från requestst i code variablen
    code = request.form['data']
    #Sprar koden med storbokstav i variablen code!
    code = code.upper()
    
    if len(code) == 4:
        return jsonify({"success":"Joining..."})
    else:
        return jsonify({"error":"The server code must contain 4 characters"})


@app.route('/host')
def host():
    game_id = id_generator()
    game_id = str(game_id)

    with open('data.txt', 'a') as f:
        f.write(game_id + "\n")
    return render_template("host.html", game_id=game_id)
  
  
if __name__ == "__main__": 
    app.run(debug=True)


    
