from flask import Flask,request
import pymysql
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime 
import requests
import threading
lock = threading.Lock()

app = Flask(__name__)

UPLOAD_FOLDER = 'static/files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)
app.secret_key = 'any random string'

def dbConnection():
    try:
        # connection = pymysql.connect(host="localhost", user="root", password="root", database="shikshana")
        connection = pymysql.connect(host="admin.cylnoaugrdrq.us-east-1.rds.amazonaws.com", user="rootadmin", password="rootadmin", database="shikshana")
        return connection
    except:
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

con = dbConnection()
cursor = con.cursor()

"----------------------------------------------------------------------------------------------------"

@app.route('/userRegister', methods=['GET', 'POST'])
def userRegister():
    if request.method == 'POST':
        data = request.get_json()
        
        username = data.get('username')
        email = data.get('email')
        mobile = data.get('mobile')
        password = data.get('password')
        standard = data.get('standard')
        
        cursor.execute('SELECT * FROM users WHERE username = %s AND standard = %s', (username,standard))
        count = cursor.rowcount
        if count == 1:        
            return "fail"
        else:
            sql1 = "INSERT INTO users(username, email, mobile, password, standard) VALUES (%s, %s, %s, %s, %s);"
            val1 = (username, email, mobile, password, standard)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
    return "fail"

@app.route('/userLogin', methods=['GET', 'POST'])
def userLogin():
    if request.method == 'POST':
        data = request.get_json()
        
        username = data.get('username')
        password = data.get('password')
        standard = data.get('standard')
        
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s AND standard = %s', (username, password, standard))
        count = cursor.rowcount
        if count == 1:        
            return "success"
        else:
            return "fail"
    return "fail"

@app.route('/uploadTimeTable', methods=['GET', 'POST'])
def uploadTimeTable():
    if request.method == 'POST':
        print("POST")
        f1 = request.files["File"]
        title = request.form["title"]
        standard = request.form["standard"]
        
        filename_secure1 = secure_filename(f1.filename)
        
        cursor.execute('SELECT * FROM timetabledata WHERE titleoftt = %s AND standard = %s', (title,standard))
        count = cursor.rowcount
        if count == 1:        
            return "exist"
        else:
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'],"timetable",filename_secure1)) 
            
            current_time = datetime.now()  
            time_stamp = current_time.timestamp() 
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
            
            sql1 = "INSERT INTO timetabledata(filename,titleoftt,standard,timestamp) VALUES (%s, %s, %s, %s);"
            val1 = ("static/files/timetable/"+filename_secure1,title,standard,str_date_time)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
        
    return "fail"

@app.route('/uploadSyllabus', methods=['GET', 'POST'])
def uploadSyllabus():
    if request.method == 'POST':
        print("POST")
        f1 = request.files["File"]
        title = request.form["title"]
        standard = request.form["standard"]
        
        filename_secure1 = secure_filename(f1.filename)
        
        cursor.execute('SELECT * FROM syllabusdata WHERE titleofs = %s AND standard = %s', (title,standard))
        count = cursor.rowcount
        if count == 1:        
            return "exist"
        else:
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'],"syllabus",filename_secure1)) 
            
            current_time = datetime.now()  
            time_stamp = current_time.timestamp() 
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
            
            sql1 = "INSERT INTO syllabusdata(filename,titleofs,standard,timestamp) VALUES (%s, %s, %s, %s);"
            val1 = ("static/files/syllabus/"+filename_secure1,title,standard,str_date_time)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
        
    return "fail"

@app.route('/uploadAssignment', methods=['GET', 'POST'])
def uploadAssignment():
    if request.method == 'POST':
        print("POST")
        f1 = request.files["File"]
        title = request.form["title"]
        standard = request.form["standard"]
        
        filename_secure1 = secure_filename(f1.filename)
        
        cursor.execute('SELECT * FROM assignmentdata WHERE titleofam = %s AND standard = %s', (title,standard))
        count = cursor.rowcount
        if count == 1:        
            return "exist"
        else:
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'],"assignment",filename_secure1)) 
            
            current_time = datetime.now()  
            time_stamp = current_time.timestamp() 
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
            
            sql1 = "INSERT INTO assignmentdata(filename,titleofam,standard,timestamp) VALUES (%s, %s, %s, %s);"
            val1 = ("static/files/assignment/"+filename_secure1,title,standard,str_date_time)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
        
    return "fail"

@app.route('/uploadAssignmentGform', methods=['GET', 'POST'])
def uploadAssignmentGform():
    if request.method == 'POST':
        
        data = request.get_json()
        
        link = data.get('link')
        title = data.get('title')
        standard = data.get('standard')
        
        cursor.execute('SELECT * FROM assignmentdata WHERE titleofam = %s AND standard = %s', (title,standard))
        count = cursor.rowcount
        if count == 1:        
            return "exist"
        else:
            
            current_time = datetime.now()  
            time_stamp = current_time.timestamp() 
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
            
            sql1 = "INSERT INTO assignmentdata(filename,titleofam,standard,timestamp) VALUES (%s, %s, %s, %s);"
            val1 = (link,title,standard,str_date_time)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
        
    return "fail"


@app.route('/getSyllabus/<stdard>', methods=['GET', 'POST'])
def getSyllabus(stdard):
    try:
        lock.acquire()
        cursor.execute('SELECT * FROM syllabusdata WHERE standard = %s', (stdard))
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/getTimetable/<stdard>', methods=['GET', 'POST'])
def getTimetable(stdard):
    try:
        lock.acquire()
        cursor.execute('SELECT * FROM timetabledata WHERE standard = %s', (stdard))
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/getAssignment/<username>/<stdard>', methods=['GET', 'POST'])
def getAssignment(username,stdard):
    try:
        lock.acquire()
        # cursor.execute('SELECT * FROM assignmentdata WHERE standard = %s', (stdard))
        cursor.execute('SELECT t1.id,t1.filename,t1.titleofam,t1.standard,t1.timestamp,t2.username,t2.assignmentpath,t2.marksobt FROM assignmentdata t1 LEFT JOIN submitedassignment t2 ON t1.titleofam = t2.title and t1.standard = t2.standard and t2.username = %s WHERE t1.standard = %s', (username,stdard))
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/submitAssignment', methods=['GET', 'POST'])
def submitAssignment():
    if request.method == 'POST':
        print("POST")
        f1 = request.files["File"]
        title = request.form["title"]
        username = request.form["username"]
        standard = request.form["standard"]
        
        filename_secure1 = secure_filename(f1.filename)
        
        cursor.execute('SELECT * FROM submitedassignment WHERE username = %s AND standard = %s AND title = %s', (username,standard,title))
        count = cursor.rowcount
        if count == 1:        
            return "exist"
        else:
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'],"submittedAssignment",filename_secure1)) 
            
            sql1 = "INSERT INTO submitedassignment(username,standard,title,assignmentpath) VALUES (%s, %s, %s, %s);"
            val1 = (username,standard,title,"static/files/submittedAssignment/"+filename_secure1)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
        
    return "fail"

@app.route('/submitAssignmentGoogleForm', methods=['GET', 'POST'])
def submitAssignmentGoogleForm():
    if request.method == 'POST':
        data = request.get_json()
        
        title = data.get('title')
        username = data.get('username')
        standard = data.get('standard') 
        
        cursor.execute('SELECT * FROM submitedassignment WHERE username = %s AND standard = %s AND title = %s', (username,standard,title))
        count = cursor.rowcount
        if count == 1:        
            return "exist"
        else:            
            sql1 = "INSERT INTO submitedassignment(username,standard,title,assignmentpath) VALUES (%s, %s, %s, %s);"
            val1 = (username,standard,title,"Marked")
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
        
    return "fail"

@app.route('/getSubmitedAssignment', methods=['GET', 'POST'])
def getSubmitedAssignment():
    try:
        lock.acquire()
        # cursor.execute('SELECT * FROM assignmentdata WHERE standard = %s', (stdard))
        cursor.execute('SELECT * from submitedassignment')
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/updateMarks', methods=['GET', 'POST'])
def updateMarks():
    if request.method == 'POST':
        data = request.get_json()
        
        idof = data.get('id')
        username = data.get('username')
        std = data.get('std')
        title = data.get('title')
        marks = data.get('marks')
        
        sql1 = "UPDATE submitedassignment SET marksobt = %s WHERE id = %s AND username = %s AND standard = %s AND title = %s;"
        val1 = (marks,idof,username,std,title)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
    return "fail"

@app.route('/uploadElearning', methods=['GET', 'POST'])
def uploadElearning():
    if request.method == 'POST':
        print("POST")
        f1 = request.files["File"]
        topic = request.form["topic"]
        title = request.form["title"]
        standard = request.form["standard"]
        
        filename_secure1 = secure_filename(f1.filename)
        
        cursor.execute('SELECT * FROM elearningdata WHERE titleofam = %s AND standard = %s', (title,standard))
        count = cursor.rowcount
        if count == 1:        
            return "exist"
        else:
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'],"elearning",filename_secure1)) 
            
            current_time = datetime.now()  
            time_stamp = current_time.timestamp() 
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
            
            sql1 = "INSERT INTO elearningdata(link,filename,titleofam,standard,timestamp) VALUES (%s, %s, %s, %s, %s);"
            val1 = (topic,"static/files/elearning/"+filename_secure1,title,standard,str_date_time)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
        
    return "fail"

@app.route('/getElearning/<stdard>', methods=['GET', 'POST'])
def getElearning(stdard):
    try:
        lock.acquire()
        cursor.execute('SELECT * FROM elearningdata WHERE standard = %s', (stdard))
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""

@app.route('/chatBot', methods=['GET', 'POST'])
def chatBot():
    if request.method == 'POST':
        data = request.get_json()
        
        query = data.get('texttosend')
        username = data.get('username')
        standard = data.get('standard')
        
        current_time = datetime.now()  
        time_stamp = current_time.timestamp() 
        date_time = datetime.fromtimestamp(time_stamp)
        str_date_time = date_time.strftime("%H:%M")
        
        sql1 = "INSERT INTO chatdata(chat,username,std,time) VALUES (%s, %s, %s, %s);"
        val1 = (query,username,standard,str_date_time)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
    return "fail"

@app.route('/getAllChats', methods=['GET', 'POST'])
def getAllChats():
    try:
        lock.acquire()
        # cursor.execute('SELECT * FROM assignmentdata WHERE standard = %s', (stdard))
        cursor.execute('SELECT * from chatdata')
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
 
"----------------------------------------------------------------------------------------------------"   

    
if __name__ == "__main__":
    app.run("0.0.0.0")
    
    
