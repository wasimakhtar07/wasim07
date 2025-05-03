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
    return render_template('Exam.html')
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
   cur.execute("INSERT INTO exam VALUES('"+t1+"','"+t2+"','"+t3+"',"+t4+")")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  # To delete  record
  if(btn=="Delete"):
   cur = mysql.connection.cursor()
   cur.execute(" delete from exam where exam_id='"+t1+"'")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  #end delete 
  # update record
  if(btn.lower()=="update"):
      cur = mysql.connection.cursor()
      cur.execute("update exam  set exam_type_id="+t2+",name='"+t3+"', start_date='"+t4+"'where exam_id="+t1+"")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index'))
  if(btn.lower()=="allsearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from exam")
      data=cur.fetchall()
      cur.close()
      return render_template('Essearch.html',data=data)
  if(btn.lower()=="psearch"): 
      cur = mysql.connection.cursor()
      cur.execute("select * from exam where exam_id="+t1+"")
      data=cur.fetchall()
      cur.close()
      return render_template('Essearch.html',data=data)
  if(btn.lower()=="specialsearch"):
      col=request.form['s']
      tspsrc=request.form['tspsrc']
      cursor=mysql.connection.cursor()
      cursor.execute("select * from exam where "+col+"="'"+tspsrc+"')
      data=cursor.fetchall()
      cursor.close()
      return render_template('Esearch.html',data=data)
if __name__=='__main__':
 app.run(debug=True,port=5005)
