#app.py
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb 
import urllib
import pyodbc
app = Flask(__name__)
        
app.secret_key = "usmanadridiaskdpqwdp"
        
params = urllib.parse.quote_plus('DRIVER=  {ODBC Driver 17 for SQL Server}; SERVER= DESKTOP-D92VUND\SQLEXPRESS; Database=documenthendler; TRUSTED_CONNECTION=yes')
      
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    conx = pyodbc.connect('DRIVER=  {ODBC Driver 17 for SQL Server}; SERVER= DESKTOP-D92VUND\SQLEXPRESS; Database=documenthendler; TRUSTED_CONNECTION=yes')
    cur = conx.cursor();
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        
   
        query = "SELECT title from pdfdocuments where content like '%{}%' ".format(search_word)
        cur.execute(query);
        
        employee = cur.fetchall()
        numrows = int(len(employee))
        print(numrows)
        
    else:
        None
    return jsonify({'htmlresponse': render_template('response.html', employee=employee, numrows=numrows)})
     
if __name__ == "__main__":
    app.run(debug=True)