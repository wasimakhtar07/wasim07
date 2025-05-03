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
    return render_template('Classroomstudent.html')
@app.route('/submit',methods=['POST'])
def submit():
 if request.method== 'POST':
  t1 = request.form['t1']
  t2 = request.form['t2']
  
  btn=request.form['b1']
  if(btn=="Save"):
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO class_room_student VALUES('"+t1+"',"+t2+")")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  # To delete  record
  if(btn=="Delete"):
   cur = mysql.connection.cursor()
   cur.execute("delete from class_room_student where student_id ="+t2+"")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  #end delete 
  if(btn.lower()=="allsearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from class_room_student")
      data=cur.fetchall()
      cur.close()
      return render_template('Crssearch.html',data=data)
  if(btn.lower()=="update"):
      cur = mysql.connection.cursor()
      cur.execute("update class_room_student set student_id= "+t2+" where classroom_id="+t1+"")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index'))
  if(btn.lower()=="psearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from class_room_student where classroom_id="+t1+"")
      data=cur.fetchall()
      cur.close()
      return render_template('Crssearch.html',data=data)
  if(btn.lower()=="specialsearch"):
      col=request.form['s']
      tspsrc=request.form['tspsrc']
      cursor=mysql.connection.cursor()
      cursor.execute("select * from class_room_student where "+col+"="'"+tspsrc+"')
      data=cursor.fetchall()
      cursor.close()
      return render_template('Crssearch.html',data=data)
if __name__=='__main__':
 app.run(debug=True,port=5003)
