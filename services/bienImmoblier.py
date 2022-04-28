import logging

from  flask_restful import Resource, reqparse
from sqlalchemy import null
from sqlalchemy.exc import SQLAlchemyError
from models.bienImmobilier import BienImmobilierModel
from models.proprietaire import ProprietaireModel

class BienImmobilierRegistre(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("id",
                        type=int,
                        required = False
                        )
    
    parser.add_argument("nom",
                        type = str,
                        required = False
                        )
    
    parser.add_argument("description",
                        type = str,
                        required = False
                        )
    
    parser.add_argument("type_bien",
                        type = str,
                        required = False
                        )
    parser.add_argument("ville",
                        type = str,
                        required = False
                        )
    parser.add_argument("nb_pieces",
                        type = int,
                        required = False
                        )
    
    parser.add_argument("caracteristiques_pieces",
                        type = str,
                        required = False
                        )
    
    parser.add_argument("id_proprietaire",
                        type = int,
                        required = False
                        )
    
    
    def get(self):
        
        data = BienImmobilierRegistre.parser.parse_args()
        #process data ville with variable
        if data['ville']:
            
            ville_request = data['ville'].strip()
            try:
                biensImmobiliers = BienImmobilierModel.retrieve_bienImmob_by_city(ville_request)
                resultat = list(map(lambda x : x.json(), biensImmobiliers))
                if len(resultat) > 0:
                    return {'Biens Immobiliers by city' : resultat}
                else:
                    return  {"message": "please check your city !"}, 200
            except SQLAlchemyError as ex:
                logging.error( "An error occurred in retrieving the element",exc_info=ex)
                return  {"message": "An error occurred in retrieving the element."}, 500

        else :
            return {"message": "Bien Immobilier not  found "}, 201
        
    
    def post(self):
        
        data = BienImmobilierRegistre.parser.parse_args()
 
        if data['nom'] and  data['description'] and data['ville'] and data['nb_pieces'] >= 1 and data['caracteristiques_pieces'] and data['id_proprietaire']:
            
            proprietaire = ProprietaireModel.find_by_id(data['id_proprietaire'])
            
            if proprietaire is not None:
                bienImmoblier = BienImmobilierModel(data['nom'],
                                                    data['description'],
                                                    data['type_bien'],
                                                    data['ville'],
                                                    data['nb_pieces'],
                                                    data['caracteristiques_pieces'],
                                                    data['id_proprietaire']
                                                    )
                    
                try:
                    bienImmoblier.save_to_db()
                    return {"message": "Bien Immobilier added successfully "}, 201
                except SQLAlchemyError as ex:
                    logging.error( " An error occurred inserting the element ",exc_info=ex)                   
                    return {"message": "An error occurred inserting the element."}, 500
            else:
                logging.debug(f" proprietaire with id {data['id_proprietaire']} not found ! ")
                return {"message": f" proprietaire with id {data['id_proprietaire']} not found ! "}, 400
        else:
            return {"message": "verify your fields ! "}, 400
            

    def put(self):
        data = BienImmobilierRegistre.parser.parse_args()
        id = data['id']
        if id is not null:
            try:
             # get bien immobilier by id
                bienImmobilier = BienImmobilierModel.find_by_id(id)
                if bienImmobilier is not None:
                    # check if proprietaire exist 
                    id_propr = ProprietaireModel.find_by_id(data['id_proprietaire'])
                    if id_propr:
        
                        if data['nom']:
                            bienImmobilier.nom = data['nom']
                        if data['description']:
                            bienImmobilier.description = data['description']
                        if data['type_bien']:
                            bienImmobilier.type_bien = data['type_bien']
                        if data['ville']:
                            bienImmobilier.ville = data['ville']
                        if data['nb_pieces']:
                            bienImmobilier.nb_pieces = data['nb_pieces']
                        if data['caracteristiques_pieces']:
                            bienImmobilier.caracteristiques_pieces = data['caracteristiques_pieces']
                    else :
                        return  {"message": " proprietaire  not found , check id_proprietaire"}, 400
                    
                else :
                    return  {"message": " Bien Immobilier not found !"}, 400
            
                # update 
                bienImmobilier.save_to_db()
                logging.info( " *** Bien Immobilier updated *** ")
            except SQLAlchemyError as ex:
                logging.error( " An error occurred updating the element ",exc_info=ex)
                return {"message": "An error occurred updating the element."}, 500
            
        return bienImmobilier.json(), 200
        
    # update Bien Immobilier by owner
    def patch(self):
        
        data = BienImmobilierRegistre.parser.parse_args()
        id_bienImmobilier = data['id']
        id_proprietaire_request = data['id_proprietaire']
        
        
        if id_bienImmobilier is not null and id_proprietaire_request is not null:
            # search bien immoblier by id_bienImmobilier
            bienImmobilier = BienImmobilierModel.retrieve_by_id_Bien_and_id_propr(id_bienImmobilier,id_proprietaire_request)
            # get id proprietaire from table Bien immobilier dataBase
            if bienImmobilier is not None:
                if data['nom']:
                    bienImmobilier.nom = data['nom']
                if data['description']:
                    bienImmobilier.description = data['description']
                if data['type_bien']:
                    bienImmobilier.type_bien = data['type_bien']
                if data['ville']:
                    bienImmobilier.ville = data['ville']
                if data['nb_pieces']:
                    bienImmobilier.nb_pieces = data['nb_pieces']
                if data['caracteristiques_pieces']:
                    bienImmobilier.caracteristiques_pieces = data['caracteristiques_pieces']
                try:
                    # update 
                    bienImmobilier.save_to_db()  
                    logging.info( " *** Bien Immobilier updated *** ")
                    return bienImmobilier.json(), 200 
                except SQLAlchemyError as ex:
                    logging.error( " An error occurred updating the element ",exc_info=ex)
                    return {"message": "An error occurred updating the element."}, 500
                
            else:
                return  {"message": f" proprietaire with id {id_proprietaire_request} is not an owner "}, 400
            

class BienImmobilierList(Resource):
    def get(self):
        return {'Biens Immobiliers ': list(map(lambda x : x.json(), BienImmobilierModel.query.all()))}