
from asyncio.windows_events import NULL
from email import message
from flask import Blueprint , render_template , request , send_from_directory , session , jsonify , json
from werkzeug.utils import secure_filename
from ..models.image import image
from ..models.myusers import Myvideo , Myvideo2 , image2 , CamLink , CamLink2 , LiveCam , EventVO , EventVE , EventCO ,EventCE
from ..models import db
home = Blueprint('home', __name__)
from .. import app
import os
from os.path import join, dirname, realpath
from flask_session import Session
import validators



UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/..')

# app.config['UPLOAD_FOLDER'] = "/D:/programming/ITI/Flask/alproject/app/static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH
app_root = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(app_root, 'static/uploads/')
target2 = os.path.join(app_root, 'static2/uploads2/')
# target = os.path.join('D:/programming/ITI/Flask/alproject/app/static/uploads')
if not os.path.isdir(target):
    os.makedirs(target)

if not os.path.isdir(target2):
    os.makedirs(target2)

@home.route('/home')
def home_page():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myemail = session['email']
        fullname = session['username']
        firstname = session['firstname']
        return render_template('home/home.html',myemail = myemail , firstname = firstname,fullname = fullname)


@home.route('/')
def welcome_page():
    return render_template('home/welcome.html')

@home.route('/analytics')
def analytic_page():

    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        return render_template('home/Analytics.html',myname = myname,myemail = myemail , firstname = firstname)


@home.route('/object_det')
def object_page():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        return render_template('home/objectDet.html',myname = myname ,myemail = myemail ,firstname = firstname)


@home.route('/emotion_det')
def emotion_page():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        return render_template('home/emotionalDet.html',myname = myname,myemail = myemail ,firstname = firstname)

@app.route('/file/<filename>')
def get_image(filename):
    return send_from_directory(target, filename)

@app.route('/file2/<filename>')
def get_image2(filename):
    return send_from_directory(target2, filename)

# for object detection
@home.route('/upload_image' , methods = ['GET','POST'])
def upload_image():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        if request.method == 'GET':
            myid = 0 
            return render_template('home/uploadImage.html', myid = myid ,myname = myname,myemail = myemail ,firstname = firstname)
        else:
            
            myimage = request.files['image']
            processor = request.form['radio']

            # myimage.save(os.path.join(app.config['UPLOAD_FOLDER'], myimage.filename))


            filename = secure_filename(myimage.filename)
            destination = '/'.join([target, filename])
            print(destination, "destination ...............................")
            myimage.save(destination)
            # myimage.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
            print("image saved")
            print("image id is :",myimage)
            print("image processor is :",processor)
            print("image file name :",myimage.filename)
            print("image mimetype :",myimage.mimetype)
            if not myimage:
                uploadimg = 'please upload an image'
                return render_template('home/uploadImage.html',uploadimg = uploadimg ,myname =myname,myemail = myemail ,firstname = firstname)
            else:
                filename = secure_filename(myimage.filename)
                mimetype = myimage.mimetype
                newimage = image(mimetype= mimetype , name=filename , processor = processor , img =myimage.read())
                db.session.add(newimage)
                db.session.commit()
                idd = newimage.id
                print("newwwwwwwwwwwww id dis :  " ,idd)
                # myid = myimage.id
                uploaded = 'your image uploaded successfully'
                return render_template('home/uploadImage.html', uploaded = uploaded , myid = idd ,myname = myname,myemail = myemail ,firstname = firstname)







@home.route('/predict_image/<int:id>')
def predict_image(id):
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        myimage = image.query.filter_by(id=id).first()
        print(myimage.name , "here is your image 2022")
        print(myimage.mimetype , "here is your mimetype 2022")
        filename = myimage.name

        return render_template('home/imagePrediction.html', filename = filename,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/upload_vedio' , methods=['GET','POST'])
def upload_vedio():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
            
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        if request.method == 'GET':
            myid = 0
            return render_template('home/uploadvedio.html', myid = myid ,myname = myname,myemail = myemail ,firstname = firstname)
        else:
            processor = request.form['radio']

            myved = request.files['video']
            filename = secure_filename(myved.filename)
            destination = '../'.join([target, filename])
            print(destination, "destination ...............................")
            myved.save(destination)
            if not myved:
                uploadvedio = 'please upload a video'
                return render_template('home/uploadvedio.html',uploadvedio = uploadvedio ,myname=myname,myemail = myemail ,firstname = firstname)
            else:
                filename = secure_filename(myved.filename)
                # name = myved.name
                newved = Myvideo( name=filename , processor=processor)
                db.session.add(newved)
                db.session.commit()
                idd = newved.id
                print("newwwwwwwwwwwww id dis :  " ,idd)
                # myid = myimage.id
                uploaded = 'your video uploaded successfully'
                return render_template('home/uploadvedio.html', uploaded = uploaded , myid = idd ,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/predict_vedio/<int:id>')
def predict_vedio(id):
    
    if session.get('email') == None:
        return render_template('error/notfound.html')

    else:
            
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        myved = Myvideo.query.filter_by(id=id).first()
        filename = myved.name
        myid = id
        return render_template('home/vedioPrediction.html' ,myid=myid,filename = filename, myname =myname,myemail = myemail ,firstname = firstname)



# for emotional  detection =====================================================================

# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================


@home.route('/upload_image_emo' , methods = ['GET','POST'])
def upload_image_emo():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        if request.method == 'GET':
            myid = 0
            return render_template('home/uploadImageEmo.html', myid = myid ,myname = myname,myemail = myemail ,firstname = firstname)
        else:
            processor = request.form['radio']

            
            myimage = request.files['image']
            # myimage.save(os.path.join(app.config['UPLOAD_FOLDER'], myimage.filename))


            filename = secure_filename(myimage.filename)
            destination = '/'.join([target2, filename])
            print(destination, "destination ...............................")
            myimage.save(destination)
            # myimage.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
            print("image saved")
            print("image id is :",myimage)
            print("image file name :",myimage.filename)
            print("image mimetype :",myimage.mimetype)
            if not myimage:
                uploadimg = 'please upload an image'
                return render_template('home/uploadImageEmo.html',uploadimg = uploadimg ,myname =myname,myemail = myemail ,firstname = firstname)
            else:
                filename = secure_filename(myimage.filename)
                mimetype = myimage.mimetype
                newimage = image2(mimetype= mimetype ,processor=processor ,name=filename , img =myimage.read())
                db.session.add(newimage)
                db.session.commit()
                idd = newimage.id
                print("newwwwwwwwwwwww id dis :  " ,idd)
                # myid = myimage.id
                uploaded = 'your image uploaded successfully'
                return render_template('home/uploadImageEmo.html', uploaded = uploaded , myid = idd ,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/predict_image_Emo/<int:id>')
def predict_image_Emo(id):
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        myimage = image2.query.filter_by(id=id).first()
        print(myimage.name , "here is your image 2022")
        print(myimage.mimetype , "here is your mimetype 2022")
        filename = myimage.name

        return render_template('home/imagePredictionEmo.html', filename = filename , myname = myname,myemail = myemail ,firstname = firstname)



@home.route('/upload_vedio_Emo' , methods=['GET','POST'])
def upload_vedio_Emo():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myemail= session['email']
        firstname= session['firstname']
        myname= session['username']

        if request.method == 'GET':
            myid = 0
            return render_template('home/uploadvedioEmo.html', myid = myid,myname = myname,myemail = myemail ,firstname = firstname)
        else:
            processor = request.form['radio']

            myved = request.files['video']
            filename = secure_filename(myved.filename)
            destination = '/'.join([target2, filename])
            print(destination, "destination ...............................")
            myved.save(destination)
            if not myved:
                uploadvedio = 'please upload a video'
                return render_template('home/uploadvedioEmo.html',uploadvedio = uploadvedio ,myname = myname,myemail = myemail ,firstname = firstname)
            else:
                filename = secure_filename(myved.filename)
                # name = myved.name
                newved = Myvideo2( name=filename ,processor=processor)
                db.session.add(newved)
                db.session.commit()
                idd = newved.id
                print("newwwwwwwwwwwww id dis :  " ,idd)
                # myid = myimage.id
                uploaded = 'your video uploaded successfully'
                return render_template('home/uploadvedioEmo.html', uploaded = uploaded , myid = idd ,myname = myname,myemail = myemail ,firstname = firstname)






@home.route('/predict_vedio_Emo/<int:id>')
def predict_vedio_Emo(id):
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
            
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        myved = Myvideo2.query.filter_by(id=id).first()
        filename = myved.name
        myid = id

        return render_template('home/vedioPredictionEmo.html' ,myid = myid,filename = filename ,myname = myname,myemail = myemail ,firstname = firstname)




# =======================================================================================
# for object detection
@home.route('/upload_link_obj' , methods = ['GET','POST'])
def upload_link_obj():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        flag1 = 0
        if request.method == 'GET':
            return render_template('home/uploadcamobject.html' ,flag1=flag1 ,myname = myname,myemail = myemail ,firstname = firstname)
        else:
            processor = request.form['radio']
            mylink = request.form['link']
            isvalid = validators.url(mylink)
            if not isvalid:
                uploadimg = 'please upload a valid link'
                return render_template('home/uploadcamobject.html',flag1 = flag1 ,uploadimg = uploadimg ,myname =myname,myemail = myemail ,firstname = firstname)
            else:
                newlink = CamLink(email= myemail , link = mylink ,processor=processor)
                db.session.add(newlink)
                db.session.commit()
                print("link added")
                flag1 = 1
                uploaded = 'your link uploaded successfully , add a new one'
                return render_template('home/uploadcamobject.html', flag1 =flag1 ,uploaded = uploaded ,myname = myname,myemail = myemail ,firstname = firstname)


# emotional detection upload link

@home.route('/upload_link_emo' , methods = ['GET','POST'])
def upload_link_emo():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        flag1= 0 


        if request.method == 'GET':
            return render_template('home/uploadcamemo.html' ,myname = myname,flag1=flag1,myemail = myemail ,firstname = firstname)
        else:
            processor = request.form['radio']
            mylink = request.form['link']
            isvalid = validators.url(mylink)
            
            if not isvalid:
                uploadimg = 'please upload a valid link'
                return render_template('home/uploadcamemo.html',uploadimg = uploadimg,flag1=flag1 
                ,myname =myname,myemail = myemail ,firstname = firstname)

            else:
                newlink = CamLink2(email= myemail , link = mylink ,processor=processor)
                db.session.add(newlink)
                db.session.commit()
                print("link added")
                flag1= 1
                uploaded = 'your link uploaded successfully , add a new one'
                return render_template('home/uploadcamemo.html', uploaded = uploaded , flag1=flag1
                 ,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/predict_link_obj')
def predict_link_obj():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        mynumber = [1 , 2 , 3 , 4 , 5 , 6 , 7]

        

        myved = CamLink.query.filter_by(email = myemail)
        # if(myved is not None):
        #     print("it is not none")
        # filename = myved.name

        return render_template('home/predictcamobject.html'  ,myved = myved ,myname = myname,myemail = myemail ,firstname = firstname)



@home.route('/predict_link_Emo')
def predict_link_Emo():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        myved = CamLink2.query.filter_by(email = myemail)
        # filename = myved.name

        return render_template('home/predictcamEmo.html'  ,myved=myved,myname = myname,myemail = myemail ,firstname = firstname)



@home.route('/add_camera' ,methods = ['GET','POST'])
def add_camera():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        if request.method == 'GET':
            return render_template('home/addCamera.html' ,myname = myname,myemail = myemail ,firstname = firstname)
        else:
            link = request.form['ip']
            location = request.form['location']
            type = request.form['type']
            username = request.form['username']
            password = request.form['password']
            isvalid = validators.url(link)
            if not isvalid:
                uploadimg = 'please upload a valid Ip'
                return render_template('home/addCamera.html',uploadimg = uploadimg ,myname =myname,myemail = myemail ,firstname = firstname)
            else:
                newcamera = LiveCam(email= myemail , link = link ,location=location ,type =type , username =username , password = password)
                db.session.add(newcamera)
                db.session.commit()
                print("camera added")
                uploaded = 'your camera uploaded successfully , add a new one'
                return render_template('home/addCamera.html', uploaded = uploaded ,myname = myname,myemail = myemail ,firstname = firstname)




@home.route('/livestream')
def livestream():
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        mycameras = LiveCam.query.filter_by(email = myemail)

        return render_template('home/livestream.html' , mycameras = mycameras ,myname = myname,myemail = myemail ,firstname = firstname)




@home.route('/cameraID/<int:id>')
def cameraID(id):
    
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:

        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']

        mycamera = LiveCam.query.filter_by(id=id).first()
        myid = id

        return render_template('home/cameraID.html'  ,myid = myid,mycamera = mycamera,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/video_events/<int:id>')
def video_events(id):
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        myevnts = EventVO.query.filter_by(id=id)
        myid = id
        return render_template('home/videoEvents.html'  , myid=myid,myevnts = myevnts,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/eventsVOdata/<int:id>')
def eventsVOdata(id):
    myevents = EventVO.query.filter_by(videoID=id)
    # message = myevnts.message
    i=0
    for event in myevents:
        i=i+1
    if( i != 0):
        messages =[]
        models = []
        ids = []
        dates = []
        videoids= []
        for event in myevents:
            messages.append(event.message)
            models.append(event.model)
            ids.append(event.id)
            dates.append(event.date)
            videoids.append(event.videoID)

        mymessages = json.dumps(messages)
        mymodels = json.dumps(models)
        myids = json.dumps(ids)
        newdates = []
        for date in dates:
            if date != None:
                newdates.append(date.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                newdates.append(date)
        print("mydates are : " , newdates)
        mydates = json.dumps(newdates)
        myvideoids = json.dumps(videoids)
        return jsonify({"mymessages":mymessages ,"error":"data" ,"mymodels" :mymodels , "myids" :myids , "mydates" :mydates , "myvideoids" :myvideoids})
    else:
        return jsonify({"error":"no data" })

# emotional models

@home.route('/video_events_Emo/<int:id>')
def video_events_Emo(id):
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        myevnts = EventVE.query.filter_by(id=id)
        myid = id
        return render_template('home/videoEventsEmo.html'  , myid=myid,myevnts = myevnts,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/eventsVEdata/<int:id>')
def eventsVEdata(id):
    myevents = EventVE.query.filter_by(videoID=id)
    i=0
    for event in myevents:
        i=i+1
    if( i != 0):     
        messages =[]
        models = []
        ids = []
        dates = []
        videoids= []
        for event in myevents:
            messages.append(event.message)
            models.append(event.model)
            ids.append(event.id)
            dates.append(event.date)
            videoids.append(event.videoID)

        mymessages = json.dumps(messages)
        mymodels = json.dumps(models)
        myids = json.dumps(ids)
        newdates = []
        for date in dates:
            if date != None:
                newdates.append(date.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                newdates.append(date)

        print("mydates are : " , newdates)
        mydates = json.dumps(newdates)
        myvideoids = json.dumps(videoids)
        return jsonify({"mymessages":mymessages , "mymodels" :mymodels , "myids" :myids , "mydates" :mydates , "myvideoids" :myvideoids , "error":"data"})
    else:
        return jsonify({"error":"no data" })


# camera events ==============================================================
# camera events ==============================================================
# camera events ==============================================================
# camera events ==============================================================
@home.route('/camera_events/<int:id>')
def camera_events(id):
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        myevnts = EventCO.query.filter_by(id=id)
        myid = id
        return render_template('home/cameraEvents.html'  , myid=myid,myevnts = myevnts,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/eventsCOdata/<int:id>')
def eventsCOdata(id):
    myevents = EventCO.query.filter_by(CamID=id)
    # message = myevnts.message
    i=0
    for event in myevents:
        i=i+1
    if( i != 0):
        messages =[]
        models = []
        ids = []
        dates = []
        videoids= []
        for event in myevents:
            messages.append(event.message)
            models.append(event.model)
            ids.append(event.id)
            dates.append(event.date)
            videoids.append(event.CamID)

        mymessages = json.dumps(messages)
        mymodels = json.dumps(models)
        myids = json.dumps(ids)
        newdates = []
        for date in dates:
            if date != None:
                newdates.append(date.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                newdates.append(date)
        print("mydates are : " , newdates)
        mydates = json.dumps(newdates)
        myvideoids = json.dumps(videoids)
        return jsonify({"mymessages":mymessages ,"error":"data" ,"mymodels" :mymodels , "myids" :myids , "mydates" :mydates , "myvideoids" :myvideoids})
    else:
        return jsonify({"error":"no data" })


# camera emotional detection=====================================
# camera emotional detection=====================================
# camera emotional detection=====================================
# camera emotional detection=====================================


@home.route('/camera_events_Emo/<int:id>')
def camera_events_Emo(id):
    if session.get('email') == None:
        return render_template('error/notfound.html')
    else:
        myname= session['username']
        myemail= session['email']
        firstname= session['firstname']
        myevnts = EventCE.query.filter_by(id=id)
        myid = id
        return render_template('home/cameraEventsEmo.html'  , myid=myid,myevnts = myevnts,myname = myname,myemail = myemail ,firstname = firstname)


@home.route('/eventsCEdata/<int:id>')
def eventsCEdata(id):
    myevents = EventCE.query.filter_by(CamID=id)
    # message = myevnts.message
    i=0
    for event in myevents:
        i=i+1
    if( i != 0):
        messages =[]
        models = []
        ids = []
        dates = []
        videoids= []
        for event in myevents:
            messages.append(event.message)
            models.append(event.model)
            ids.append(event.id)
            dates.append(event.date)
            videoids.append(event.CamID)

        mymessages = json.dumps(messages)
        mymodels = json.dumps(models)
        myids = json.dumps(ids)
        newdates = []
        for date in dates:
            if date != None:
                newdates.append(date.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                newdates.append(date)
        print("mydates are : " , newdates)
        mydates = json.dumps(newdates)
        myvideoids = json.dumps(videoids)
        return jsonify({"mymessages":mymessages ,"error":"data" ,"mymodels" :mymodels , "myids" :myids , "mydates" :mydates , "myvideoids" :myvideoids})
    else:
        return jsonify({"error":"no data" })

