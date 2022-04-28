import config
from services.bienImmoblier import BienImmobilierList, BienImmobilierRegistre
from flask import Flask,request
from flask_restful import Api
from services.proprietaire import ProprietaireList, ProprietaireRegistre
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.mySQLConnexion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# add & update proprietaire
api.add_resource(ProprietaireRegistre,"/api/v1/propr", endpoint="propr")

# add, update  bien immobilier and fetch bien immobilier by city
api.add_resource(BienImmobilierRegistre, "/api/v1/immobilier", endpoint="immobilier")

# get all proprietaire
api.add_resource(ProprietaireList, "/api/v1/proprs")
# get all bien immobiliers
api.add_resource(BienImmobilierList,"/api/v1/immobiliers")



if __name__ == '__main__':
    from db import db
    
    db.init_app(app)
    app.run(port=5000, debug=True)
