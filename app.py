import json
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from func import Mutants

app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://Okan:Wil830305*@cluster0-ryris.mongodb.net/adnmeli?retryWrites=true&w=majority'
mongo = PyMongo(app)

def GrabaDB(Exist,isMut,dna):
    if Exist == 0:
        id = mongo.db.humans.insert_one({'dna': dna, 'ismutant': isMut.valid,'idMsj': isMut.idMsj, 'Msl': isMut.msj})

@app.route('/')
def home():
    return 'Api ADN MELI Challenge'

@app.route('/mutant', methods=['POST'])
def ismutant():
    if('dna' not in request.json):
        response = app.response_class(response=json.dumps({'Error':'Parametro incorrecto'}),
        status=400,
        mimetype='application/json')
        return response
    else:
        dna = request.json['dna']
        if dna:
            isMut = Mutants.isMutant(dna)
            Exist =  mongo.db.humans.count_documents({"dna":dna})
            if isMut.valid:
                GrabaDB(Exist,isMut,dna)
                response = app.response_class(response=json.dumps({'mutante':True}),
                status=200,
                mimetype='application/json')
            else:
                GrabaDB(Exist,isMut,dna)
                response = app.response_class(response=json.dumps({'mutante':False}),
                status=403,
                mimetype='application/json')
        else:
            response = app.response_class(response=json.dumps({'mutante':False}),
            status=204,
            mimetype='application/json')
        return response
    
@app.route('/stats', methods=['GET'])
def stats():
    rTrue = mongo.db.humans.count_documents({"ismutant":True})
    rFalse = mongo.db.humans.count_documents({"ismutant":False})
    hTotal = rTrue + rFalse
    rRatio = rTrue / hTotal
    return {
            "count_mutant_dna":rTrue,
            "count_human_dna":hTotal,
            "ratio": rRatio
        }

if __name__ == "__main__":
    app.run(debug= True)
