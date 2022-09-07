

# from models import db
from app.models import db

from sqlalchemy_utils.types import ChoiceType

class image(db.Model):
    types = [('cpu','cpu'),('gpu','gpu')]
    __tablename__ = 'image'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    img = db.Column(db.Text  , nullable = False)
    name = db.Column(db.Text , nullable = False )
    processor = db.Column(ChoiceType(types))
    mimetype = db.Column(db.Text , nullable = False )

    def __init__(self, img , name , mimetype , processor):
        self.name = name
        self.img = img
        self.mimetype = mimetype
        self.processor = processor




db.create_all()
db.session.commit()