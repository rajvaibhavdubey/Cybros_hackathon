from app import app
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/addoriginals', endpoint='a', methods=['POST'])
def addoriginals():
    if request.method == 'POST':
        try:
            text = request.form['text']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO original (text) VALUES (?)", (text))

                con.commit()
                msg = "Original added successfully"
        except:
            con.rollback()

        finally:
            return jsonify(msg="Insert successful")
            con.close()


@app.route('/settranslation', endpoint='b', methods=['POST'])
def settranslation():
    if request.method == 'POST':
        try:
            original_id = request.form['original_id']
            text = request.form['text']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO translations (text,original_id) VALUES (?,?)", (text, original_id))

                con.commit()
                msg = "Translation added successfully"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return jsonify(msg=msg)
            con.close()


@app.route('/getSentence', endpoint='c', methods=['POST'])
def getSentence():
    if request.method == 'POST':
        msg = "error in insert operation"
        try:
            text = request.form['text']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                print cur.execute("SELECT * from original")

                con.commit()
                msg = "Original added successfully"
        except:
            con.rollback()

        finally:
            return jsonify(msg=msg)
            con.close()


@app.route('/getalldata', endpoint='d', methods=['POST'])
def getalldata():
    if request.method == 'POST':
        try:
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("SELECT * from original")
                rows = cur.fetchall(); 
                con.commit()
                return jsonify(code=200,rows=rows)
        except:
            con.rollback()
            return jsonify(code=500)

        finally:
            con.close()


@app.route('/gettsne', endpoint='e', methods=['POST'])
def gettsne():
    if request.method == 'POST':
        try:
            original_id = request.form['original_id']
            text = request.form['text']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO translations (text,original_id) VALUES (?,?)", (text, original_id))

                con.commit()
                msg = "Translation added successfully"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return jsonify(msg=msg)
            con.close()


if __name__ == '__main__':
    app.run(debug=True)
