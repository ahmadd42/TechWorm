from flask import Flask, jsonify, render_template, request, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'OnlineStore'

mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/newuser/")
def signup():
    return render_template("signup.html")

@app.route("/navigateto/")
def nav():
    return render_template("nav.html")

@app.route("/catalogmain/")
def catalog():
    cfrname = request.args.get('cfname', 0)
    cfrname = cfrname.strip('"')
    return render_template("catalog.html", frname = cfrname)


@app.route("/api/logauth")
def add():
    nam = request.args.get('usname', 0)
    pas = request.args.get('uspass', 0)
    mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    mycursor.execute('SELECT * FROM Users WHERE UserId = %s AND Password = %s', (nam, pas,))
    auth = ""
    if int(mycursor.rowcount) > 0:
        result = mycursor.fetchone()
        auth = result['FirstName']
    else:
        auth = "No"

    return jsonify({"astatus" : auth})


@app.route("/api/ins", methods=['POST'])
def regUser():
    newnam = request.args.get('nusname', 0)
    newfname = request.args.get('nfname', 0)
    newlname = request.args.get('nlname', 0)
    newaddress = request.args.get('naddress', 0)
    newphone = request.args.get('nphone', 0)
    newpas = request.args.get('nuspass', 0)

    mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    mycursor.execute('INSERT INTO Users VALUES (%s, %s, %s, %s, %s, %s)', (newnam, newfname, newlname, newaddress, newphone, newpas,))
    mysql.connection.commit()

    return jsonify({"registered" : "true"})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
