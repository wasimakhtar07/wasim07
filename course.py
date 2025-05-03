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
    return render_template('Course.html')
@app.route('/submit',methods=['POST'])
def submit():
 if request.method== 'POST':
  t1 = request.form['t1']
  t2 = request.form['t2']
  t3 = request.form['t3']
  t4 = request.form['t4']
  btn=request.form['b1']
  if(btn=="Save"):
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO course VALUES('"+t1+"','"+t2+"','"+t3+"',"+t4+")")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  # To delete  record
  if(btn.lower()=="delete"):
   cur = mysql.connection.cursor()
   cur.execute(" delete from course where course_id='"+t1+"'")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  #end delete 
  if(btn.lower()=="update"):
      cur = mysql.connection.cursor()
      cur.execute(" update course set name='"+t2+"',desc1='"+t3+"',grade_id="+t4+" where course_id="+t1+"")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index'))
  if(btn.lower()=="allsearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from course")
      data=cur.fetchall()
      cur.close()
      return render_template('Csearch.html',data=data)
  if(btn.lower()=="psearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from course where course_id="+t1+"")
      data=cur.fetchall()
      cur.close()
      return render_template('Csearch.html',data=data)
  if(btn.lower()=="specialsearch"):
      col=request.form['s']
      tspsrc=request.form['tspsrc']
      cursor=mysql.connection.cursor()
      cursor.execute("select * from course where "+col+"="'"+tspsrc+"')
      data=cursor.fetchall()
      cursor.close()
      return render_template('Csearch.html',data=data)
if __name__=='__main__':
 app.run(debug=True,port=5004)