
from flask import Blueprint , render_template , request , session
from flask_wtf.csrf import CSRFProtect
import re
from werkzeug.utils import secure_filename
import os
from ..models.myusers import myusers , CamLink ,CamLink2
from ..models.myusers import db
from ..models.image import image
from flask_session import Session

from .. import app

auth = Blueprint('auth',__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = "D:/programming/ITI/Flask/alproject/app/static/uploads"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@auth.route('/login', methods=['GET','POST'])
def login():
    title='Login'
    if request.method == 'GET':
        return render_template('auth/login2.html',title=title)
    else:
        email = request.form['email']
        password = request.form['password']
        myresult1 = myusers.query.filter_by(email=email , password= password).first()
        # print("my result is here pls",myresult1.firstname)
        if(myresult1 != None):
            firstname = myresult1.firstname
            email = myresult1.email
            username = myresult1.username
            lastname = myresult1.lastname
            fullname = firstname + ' ' + lastname
            session['username'] = fullname
            session['email'] = email
            # session['user'] = user
            session['firstname'] = firstname
            return render_template('home/home.html',fullname = fullname)           
        else:
            emailpass = 'email and/or password are not correct'
            return render_template('auth/login2.html',emailpass=emailpass)


        


@auth.route('/register', methods=['GET','POST'])
def register():
    # app_root = os.path.dirname(os.path.abspath(__file__))
    # target = os.path.join(app_root, 'static/uploads/')
    # target = os.path.join('D:/programming/ITI/Flask/alproject/app/static/uploads')
    # if not os.path.isdir(target):
    #     os.makedirs(target)

    title='Register'
    if request.method == 'GET':
        return render_template('auth/register.html',title=title)

    else:
        # image = request.files['image']
        # filename = secure_filename(image.filename)
        # destination = '/'.join([target, filename])
        # image.save(destination)
        # image.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))

        username=request.form['username']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        password1=request.form['password']
        address=request.form['address']
        country=request.form['country']
        bdate=request.form['bdate']
        print(username,firstname,lastname,password1,email,bdate,address,country)
        name_regex = r"^[a-zA-Z ,.'-]+$"
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

        myresult1 = myusers.query.filter_by(email=email).first()
        
        myresult2 = myusers.query.filter_by(username=username).first()
        if(myresult2):
            print(myresult1,"my result 1 ")
            userxists = 'this username  already exists'
            print("username already exists")
            return render_template('auth/register.html', userxists=userxists)

        elif(myresult1 != None):

            emailexists = 'this email  already exists'
            print("username already exists")

            return render_template('auth/register.html', emailexists=emailexists)


        if (re.search(name_regex, request.form['firstname']) == None):
            
            errorfname = 'This First Name Is Not Valid Enter Valid Name'
            return render_template('auth/register.html', errorfname=errorfname)
        else:
            print("firstname is valid")
        if (re.search(name_regex, request.form['username']) == None):
          
            errorusername = 'This userName Is Not Valid Enter Valid userName'
            return render_template('auth/register.html', errorusername=errorusername)
        else:
            print("username is valid")
        if (re.search(name_regex, request.form['lastname']) == None):
          
            errorlastname = 'This lastname Is Not Valid Enter Valid lastname'
            return render_template('auth/register.html', errorlastname=errorlastname)
        else:
            print("lastname is valid")
        if (re.search(email_regex, request.form['email']) == None):
          
            erroremail = 'This email Is Not Valid Enter Valid email'
            return render_template('auth/register.html', erroremail=erroremail)
        else:
            print("email is valid")
        if (request.form['password'] == request.form['confirm']):
            # if image:
            #     filename = secure_filename(image.filename)
            #     image.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))

            newuser = myusers(username = username , firstname = firstname , lastname = lastname , password = password1
            , email = email , country = country , Address = address , bdate = bdate )
            db.session.add(newuser)
            db.session.commit()
            fullname = firstname + ' ' + lastname
            return render_template('auth/login2.html',fullname = fullname)
        else:
            
            notequal = "password must be identical"
            return render_template('auth/register.html', notequal=notequal)



@auth.route('/logout')
def logout():
    myemail= session['email']
    CamLink.query.filter_by(email=myemail).delete()
    CamLink2.query.filter_by(email=myemail).delete()
    db.session.commit()
    session.clear()
    return render_template('home/welcome.html')


