import flask
from flask.globals import session
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import os

app=flask.Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)
SQLALCHEMY_DATABASE_URI = 'postgresql://pg_user:pg_pwd@pg_server/pg_db'
SQLALCHEMY_BINDS = {
    'mssql_bind': 'mssql+pyodbc://msssql_user:mssql_pwd@mssql_server/mssql_schema?driver=FreeTDS'
}

db1=SQLAlchemy(app)
class MySQL(db1.Model):
    id = db1.Column(db1.Integer, primary_key=True)
    name =  db1.Column(db1.String(150), unique = True, nullable=False)
    

db2=SQLAlchemy(app)
class MyTable(db2.Model):
    __bind_key__ = 'mssql_bind'
    __tablename__ = 'my_table'
    
    id = db2.Column(db2.Integer, nullable=False, primary_key=True)
    val = db2.Column(db2.String(50), nullable=False)
    
    
@app.route("/")
def main():
    return "Welcome"

@app.route('/MySql')
def MySql():
    # data=app(id=22)
    # session.add(data)
    # session.commit()
    return "MySql"

@app.route('/PosterSql')
def PosterSql():
    return "PosterSql"

if __name__=='__main__':
    app.run(host='localhost',port=5000,debug=True)
    db1.create_all()
    db2.create_all()
    