from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= '1234'
app.config['MYSQL_DB']= 'student'
mysql = MySQL(app)
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/submit',methods=['POST'])
def submit():
     t1 = request.form['t1']
     t2 = request.form['t2']
     b1=request.form['b1']
     if(b1=="Login"):
      cur = mysql.connection.cursor()
      cur.execute("select * from login")
      data=cur.fetchall()
      cur.close()
      return render_template("login.html",data=data,t1=t1,t2=t2)
@app.route('/menu')
def mymenu():
    return render_template('menu.html')  
@app.route("/loginsubmit",methods=['POST'])
@app.route('/classroom')
def classroom():
    return render_template('classroom.html')

@app.route('/course')
def course():
    return render_template('course.html')  
@app.route('/class_room_student')
def class_room_student():
    return render_template('Classroomstudent.html')
@app.route('/attendance')
def attendance():
    return render_template('Attendance.html')
@app.route('/exam')
def exam():
    return render_template('exam.html')
@app.route('/exam_type')
def exam_type():
    return render_template('exam_type.html')
@app.route('/exam_result')
def exam_result():
    return render_template('exam_result.html')
@app.route('/grade')
def grade():
    return render_template('grade.html')
@app.route('/parent')
def parent():
    return render_template('parent.html')
@app.route('/student')
def student():
    return render_template('student.html')
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')


if __name__=='__main__':
 app.run(debug=True)
