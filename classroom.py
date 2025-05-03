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
    return render_template('Classroom.html')
@app.route('/submit',methods=['POST'])
def submit():
 if request.method== 'POST':
  t1 = request.form['t1']
  t2 = request.form['t2']
  t3 = request.form['t3']
  t4 = request.form['t4']
  t5 = request.form['t5']
  t6 = request.form['t6']
  t7 = request.form['t7']
  btn=request.form['b1']
  if(btn.lower()=="save"):
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO classroom VALUES("+t1+",'"+t2+"',"+t3+",'"+t4+"','"+t5+"','"+t6+"',"+t7+")")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  # To delete  record
  if(btn.lower()=="delete"):
   cur = mysql.connection.cursor()
   cur.execute("delete from classroom where  classroom_id ="+t1+"")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  #end delete 
  if(btn.lower()=="update"):
      cur = mysql.connection.cursor()
      cur.execute("update classroom set  year='"+t2+"',grade_id="+t3+",section='"+t4+"',status='"+t5+"',remarks='"+t6+"',teacher_id="+t7+" where classroom_id="+t1+"")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index'))
  if(btn.lower()=="allsearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from classroom")
      data=cur.fetchall()
      cur.close()
      return render_template('Crsearch.html',data=data)
  if(btn.lower()=="psearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from classroom where classroom_id="+t1+"")
      data=cur.fetchall()
      cur.close()
      return render_template('Crsearch.html',data=data)
  if(btn.lower()=="specialsearch"):
      col=request.form['s']
      tspsrc=request.form['tspsrc']
      cursor=mysql.connection.cursor()
      cursor.execute("select * from classroom where "+col+"="'"+tspsrc+"')
      data=cursor.fetchall()
      cursor.close()
      return render_template('Crsearch.html',data=data)
if __name__=='__main__':
 app.run(debug=True,port=5002)
