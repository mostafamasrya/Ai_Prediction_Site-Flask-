
from datetime import date
from email.policy import default
from statistics import mode
from xmlrpc.client import DateTime
from sqlalchemy_utils import URLType
from . import db
from sqlalchemy_utils.types import ChoiceType
from datetime import datetime

class myusers(db.Model):
    __tablename__ = 'myusers'

    id=db.Column(db.Integer , autoincrement = True , primary_key = True)

    username = db.Column(db.String(30) , unique = True , nullable = False )
    firstname = db.Column(db.String(30) , nullable = False)
    lastname = db.Column(db.String(30) , nullable = False)
    email = db.Column(db.String(255),unique = True , nullable = False)
    password = db.Column(db.String(255) , nullable = False)
    country = db.Column(db.String(20))
    Address = db.Column(db.Text)
    bdate = db.Column(db.Date)
    # image = db.Column(db.LargeBinary)

    def __init__(self, username , firstname , lastname ,email , country , password , Address , bdate ):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.country = country
        self.password = password
        self.Address = Address
        self.bdate = bdate
        # self.image = image



# image = db.Column(db.LargeBinary , nullable = True)


class Myvideo(db.Model):
    types = [('cpu','cpu'),('gpu','gpu')]
    __tablename__ = 'Myvideo'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    name = db.Column(db.String(50) , nullable = False)
    processor = db.Column(ChoiceType(types))

    def __init__(self , name ,processor ):
        self.name = name
        self.processor = processor



class Myvideo2(db.Model):
    types = [('cpu','cpu'),('gpu','gpu')]
    __tablename__ = 'Myvideo2'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    name = db.Column(db.String(50) , nullable = False)
    processor = db.Column(ChoiceType(types))


    def __init__(self , name , processor):
        self.name = name
        self.processor = processor



class image2(db.Model):
    types = [('cpu','cpu'),('gpu','gpu')]
    __tablename__ = 'image2'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    img = db.Column(db.Text , nullable = False)
    name = db.Column(db.Text , nullable = False )
    processor = db.Column(ChoiceType(types))
    mimetype = db.Column(db.Text , nullable = False )

    def __init__(self, img , name , mimetype , processor):
        self.name = name
        self.img = img
        self.mimetype = mimetype
        self.processor = processor



class CamLink(db.Model):
    types = [('cpu','cpu'),('gpu','gpu')]
    __tablename__ = 'CamLink'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    email = db.Column(db.String(255),unique = False , nullable = False)
    processor = db.Column(ChoiceType(types))
    link = db.Column(URLType)


   

    def __init__(self, email , link ,processor):
        self.email = email
        self.link = link
        self.processor = processor



class CamLink2(db.Model):
    types = [('cpu','cpu'),('gpu','gpu')]
    __tablename__ = 'CamLink2'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    email = db.Column(db.String(255),unique = False , nullable = False)
    link = db.Column(URLType)
    processor = db.Column(ChoiceType(types))



   

    def __init__(self, email , link , processor ):
        self.email = email
        self.link = link
        self.processor = processor


class LiveCam(db.Model):
    __tablename__ = 'LiveCam'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    link = db.Column(URLType)
    type = db.Column(db.String(255),unique = False , nullable = True)
    location = db.Column(db.String(255),unique = False , nullable = True)
    username = db.Column(db.String(255),unique = False , nullable = True)
    password = db.Column(db.String(255) , unique = False,nullable = True)
    email = db.Column(db.String(255),unique = False , nullable = False)


    def __init__(self, link , type , location , username , password , email ):
        self.link = link
        self.type = type
        self.location = location
        self.username = username
        self.password = password
        self.email = email


# events ==================================
# =================================
# ===========================
# ======================
# ================
# ========

class EventVO(db.Model):
    __tablename__ = 'EventVO'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    model = db.Column(db.String(255),unique = False , nullable = True , default = "Object Detection")
    videoID = db.Column(db.Integer ,db.ForeignKey('Myvideo.id'))
    message = db.Column(db.String(255),unique = False , nullable = True)
    date = db.Column(db.DateTime)

    def __init__(self , model , videoID , message , date ):
        self.model = model
        self.videoID = videoID
        self.message = message
        self.date = date

class EventVE(db.Model):
    __tablename__ = 'EventVE'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    model = db.Column(db.String(255),unique = False , nullable = True , default = "Emotional Detection")
    videoID = db.Column(db.Integer ,db.ForeignKey('Myvideo2.id'))
    message = db.Column(db.String(255),unique = False , nullable = True)
    date = db.Column(db.DateTime)

    def __init__(self , model , videoID , message , date ):
        self.model = model
        self.videoID = videoID
        self.message = message
        self.date = date


class EventCO(db.Model):
    __tablename__ = 'EventCO'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    model = db.Column(db.String(255),unique = False , nullable = True , default = "Object Detection")
    CamID = db.Column(db.Integer ,db.ForeignKey('CamLink.id'))
    message = db.Column(db.String(255),unique = False , nullable = True)
    date = db.Column(db.DateTime)

    def __init__(self , model , CamID , message , date ):
        self.model = model
        self.CamID = CamID
        self.message = message
        self.date = date

class EventCE(db.Model):
    __tablename__ = 'EventCE'
    id=db.Column(db.Integer , autoincrement = True , primary_key = True)
    model = db.Column(db.String(255),unique = False , nullable = True , default = "Emotional Detection")
    CamID = db.Column(db.Integer ,db.ForeignKey('CamLink2.id'))
    message = db.Column(db.String(255),unique = False , nullable = True)
    date = db.Column(db.DateTime)

    def __init__(self , model , CamID , message , date ):
        self.model = model
        self.CamID = CamID
        self.message = message
        self.date = date

