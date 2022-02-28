from flask import Flask
from flask_restful import Resource, Api
import sqlite3
con=sqlite3.connect('identifier.sqlite', check_same_thread=False)
cur=con.cursor()


app = Flask(__name__)
api = Api(app)


class Students(Resource):
   def get(self, student_id):
       cur.execute("SELECT * FROM students where id=?", (student_id,))
       return  cur.fetchone()


api.add_resource(Students, '/read/<int:student_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8080)