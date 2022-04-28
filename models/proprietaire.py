from db import db


class ProprietaireModel(db.Model):
    
    __tableName__ = "proprietaire"
    
    id = db.Column(db.Integer, primary_key = True, nullable=False, unique=True, autoincrement=True)
    nom  = db.Column(db.String(255))
    prenom = db.Column(db.String(255))
    dateNaissance = db.Column(db.Date)
    
    bienImmobilier = db.relationship("BienImmobilierModel", lazy="dynamic")
    
    def __init__(self, nom, prenom, dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        
    def json(self):
        return { 'id' : self.id,'nom' : self.nom, 'prenom' : self.prenom, 'dateNaissance': str(self.dateNaissance)}
    
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()