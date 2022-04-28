from db import db


class BienImmobilierModel(db.Model):
    __tableName__ = "immobilier"
    
    id = db.Column(db.Integer, primary_key = True, nullable=False, unique=True, autoincrement=True)
    nom  = db.Column(db.String(100))
    description  = db.Column(db.String(255))
    type_bien = db.Column(db.String(45))
    ville = db.Column(db.String(150))
    nb_pieces = db.Column(db.Integer)
    caracteristiques_pieces = db.Column(db.String(255))
    id_propr = db.Column(db.Integer, db.ForeignKey('proprietaire_model.id'))
    
    def __init__(self, nom, description, type_bien, ville , nb_pieces, caracteristiques_pieces,id_propr):
        
        self.nom = nom
        self.description = description
        self.ville = ville
        self.type_bien = type_bien
        self.nb_pieces = nb_pieces
        self.caracteristiques_pieces = caracteristiques_pieces
        self.id_propr = id_propr
        
    
    def json(self):
        return {'id ': self.id, 
                'nom': self.nom, 
                'description': self.description, 
                'type_bien' : self.type_bien,
                'ville' : self.ville,
                'nb_pieces' : self.nb_pieces,
                'caracteristiques_pieces' :  self.caracteristiques_pieces,
                'id_proprietaire' : self.id_propr
                
                }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    
    @classmethod
    def retrieve_bienImmob_by_city(cls, ville):
        return cls.query.filter_by(ville = ville)
    
    @classmethod
    def retrieve_by_id_Bien_and_id_propr(cls, id_bienImmobilier, id_proprietaire):
        return cls.query.filter_by(id=id_bienImmobilier,id_propr=id_proprietaire).first()

    
        