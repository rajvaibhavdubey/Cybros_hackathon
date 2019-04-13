from app import app
from flask import jsonify, request

@app.route('/getSentence', endpoint = 'getSentence', methods = ['POST'])
def settranslation():
   if request.method == 'POST':
      msg = "error in insert operation"
      try:
         text = request.form['text']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            print cur.execute("SELECT * from original")
            
            con.commit()
            msg = "Original added successfully"
      except:
         con.rollback()
      
      finally:
         return jsonify( msg=msg )
         con.close()

@app.route('/getalldata', endpoint = 'getalldata', methods = ['POST'])
def settranslation():
   if request.method == 'POST':
      msg = "error in insert operation"
      try:
         text = request.form['text']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            print cur.execute("SELECT * from original")
            
            con.commit()
            msg = "Original added successfully"
      except:
         con.rollback()
      
      finally:
         return jsonify( msg=msg )
         con.close()

@app.route('/gettsne', endpoint = 'gettsne',methods = ['POST'])
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