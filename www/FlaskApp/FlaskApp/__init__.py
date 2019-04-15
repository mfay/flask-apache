import os
import cx_Oracle
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    connection = cx_Oracle.connect('system/oracle@oracle/XE')
    cur = connection.cursor()
    cur.execute('SELECT * FROM HR.departments ORDER BY department_id')
    rows = cur.fetchall()
    cur.close()
    connection.close()
    return render_template('hello.html', rows=rows)

if __name__ == "__main__":
    app.run()
