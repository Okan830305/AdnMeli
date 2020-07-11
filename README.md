***ApiADN Challenge MELI***
--

[![Unix Build Status](https://img.shields.io/travis/flask-api/flask-api.svg)](https://travis-ci.org/flask-api/flask-api)
[![Coverage Status](https://img.shields.io/coveralls/flask-api/flask-api.svg)](https://coveralls.io/r/flask-api/flask-api)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/flask-api/flask-api.svg)](https://scrutinizer-ci.com/g/flask-api/flask-api/)
[![PyPI Version](https://img.shields.io/pypi/v/Flask-API.svg)](https://pypi.org/project/Flask-API/)

Api para la validacion de el DNA para comprobar si se es o no mutante.
- La Api fue desarrollada en PYTHON con el framework Flask
- Como Db se uso un Cluster Free De MONGODB

##Uso de la API en ambiente LOCAL


#### Clone el repositorio:

    git clone https://github.com/Okan830305/AdnMeli.git
    cd AdnMeli

#### Instale y Cree el Entorno Virtual (PIPENV):

    pip install pipenv
    pipenv install

#### Corra el Servidor Flask:

    python app.py

#### Pruebe los endpoints:

    curl -XGET http://localhost:5000/stats
    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/mutant -d '{"dna": ["ACTG","GTGG","CGAC","GGGG"]}'
    
    Restricciones
        - Las letras de los Strings solo pueden ser: (A,T,C,G)
        - Todos los strings deben ser del mismo tamaño y concordante a la cantidad de filas (NxN)
        Nota: En caso de no cumplirse estas restricciones la api deveuelve la misma respuesta para no mutante 403-Forbidden.

#### Execucion de Test Atuomaticos:

    python test.py

License
-------

MIT, see LICENSE file


