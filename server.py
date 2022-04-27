import config
from ressources.bienImmoblier import BienImmobilierList, BienImmobilierRegistre
from ressources.utilisateur import UserRegistre


from flask import Flask,request
from flask_restful import Api

from ressources.utilisateur import UserList
from ressources.proprietaire import ProprietaireList, ProprietaireRegistre


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = config.mySQLConnection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)




# add & update proprietaire
api.add_resource(ProprietaireRegistre,"/api/v1/propr", endpoint="propr")

# add, update  bien immobilier and fetch bien immobilier by city

api.add_resource(BienImmobilierRegistre, "/api/v1/immobilier", endpoint="immobilier")



# get all proprietaire
api.add_resource(ProprietaireList, "/api/v1/proprs")
# get all bien immobiliers
api.add_resource(BienImmobilierList,"/api/v1/immobiliers")

# to remove  
api.add_resource(UserList, "/api/v1/users")
api.add_resource(UserRegistre, "/api/v1/user")

if __name__ == '__main__':
    from db import db
    
    db.init_app(app)
    app.run(port=5000, debug=True)
