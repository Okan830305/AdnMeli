import json
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from func import ADN

app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://Okan:Wil830305*@cluster0-ryris.mongodb.net/adnmeli?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def home():
    return 'Api ADN MELI Challenge'


@app.route('/mutant', methods=['POST'])
def ismutant():
    adn = request.json['adn']
    if adn:
        isMut = ADN.isMutant(adn)
        id = mongo.db.humans.insert({'adn': adn, 'ismutant': isMut.valid,'idMsj': isMut.idMsj, 'Msl': isMut.msj})
        if isMut.valid:
            response = app.response_class(response=json.dumps({'mutante':True}),
            status=200,
            mimetype='application/json')
        else:
            response = app.response_class(response=json.dumps({'mutante':False}),
            status=403,
            mimetype='application/json')
    return response
    
@app.route('/stats', methods=['GET'])
def stats():
    rTrue = mongo.db.humans.find({"ismutant":True})
    rFalse = mongo.db.humans.find({"ismutant":False})
    hTotal = rTrue.count() + rFalse.count()
    rRatio = rTrue.count() / hTotal
    return {
            "count_mutant_dna":rTrue.count(),
            "count_human_dna":hTotal,
            "ratio": rRatio
        }

if __name__ == "__main__":
    app.run(debug= True)
