from app import app
from flask import jsonify, request

@app.route('/addoriginals', endpoint = 'addoriginals', methods = ['POST'])
def settranslation():
   if request.method == 'POST':
      msg = "error in insert operation"
      try:
         text = request.form['text']
         
         with sql.connect("../database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO original (text) VALUES (?)",(text) )
            
            con.commit()
            msg = "Original added successfully"
      except:
         con.rollback()
      
      finally:
         return jsonify( msg=msg )
         con.close()

@app.route('/settranslation', endpoint = 'settranslation',methods = ['POST'])
def settranslation():
   if request.method == 'POST':
      try:
         original_id = request.form['original_id']
         text = request.form['text']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO translations (text,original_id) VALUES (?,?)",(text,original_id) )
            
            con.commit()
            msg = "Translation added successfully"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return jsonify( msg=msg )
         con.close()

# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#    if request.method == 'POST':
#       try:
#          nm = request.form['nm']
#          addr = request.form['add']
#          city = request.form['city']
#          pin = request.form['pin']
         
#          with sql.connect("database.db") as con:
#             cur = con.cursor()
#             cur.execute("INSERT INTO students (name,addr,city,pin) 
#                VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
#             con.commit()
#             msg = "Record successfully added"
#       except:
#          con.rollback()
#          msg = "error in insert operation"
      
#       finally:
#          return render_template("result.html",msg = msg)
#          con.close()