from turtle import st
from flask_restful import Resource, reqparse
from sqlalchemy import null
from models.proprietaire import ProprietaireModel




class ProprietaireRegistre(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("id",
                        type = int,
                        required = False
                        )
    
    parser.add_argument("nom",
                        type = str,
                        required = False
                        )
    parser.add_argument("prenom",
                        type = str,
                        required = False
                        )
    
    parser.add_argument("dateNaissance",
                        type = str,
                        required = False
                        )
    
      
    def post(self):
        data = ProprietaireRegistre.parser.parse_args()
        
        
        if data['nom'] and data['prenom'] and data['dateNaissance']:
            
            proprietaire = ProprietaireModel(data['nom'], data['prenom'], str(data['dateNaissance']))
            
            try:
                proprietaire.save_to_db()
            except:
                return {"message": "An error occurred inserting the element."}, 500
                
            #return proprietaire.json(),201
            return {"message": "proprietaire added successfully "}, 201
        else :
            return {"message": "verify your field ! "}, 400
    
    

    def put(self):
        data = ProprietaireRegistre.parser.parse_args()
        id = data['id']
        if id is not null:
            
            proprietaire = ProprietaireModel.find_by_id(id)
            if proprietaire is not None:
    
                if data['nom']:
                    proprietaire.nom = data['nom']
                if data['prenom']:
                    proprietaire.prenom = data['prenom']
                if data['dateNaissance']:
                    proprietaire.dateNaissance = data['dateNaissance']
            
            else :
                return  {"message": " proprietaire not found "}, 400
        
            proprietaire.save_to_db()
        return proprietaire.json()
    
    

class ProprietaireList(Resource):
    
    def get(self):
        return {'proprietaires ': list(map(lambda x : x.json(), ProprietaireModel.query.all()))}
    