from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.update(
    SECRET_KEY='dwij123',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:dwij123@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# @app.route('/hello')
# def hello_name():
#     return render_template('hello.html' )


class Publication(db.Model):
    __tablename__ = 'publications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Publication: {self.name}>'
    

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer,primary_key=True)
    student_name = db.Column(db.String(80), nullable = False)
    std = db.Column(db.Integer)
    phone = db.Column(db.BigInteger)

    def __init__(self,student_id,student_name,std,phone):
        self.student_id = student_id
        self.student_name= student_name
        self.std = std
        self.phone = phone

    def __repr__(self):
        return f'<student: {self.student_name} and id is {self.student_id}>'



if __name__ == '__main__':
    with app.app_context():
        # stud = Student.query.filter_by(student_id = 2).first()
        # stud.student_name = "suhag"
        stud = Student.query.filter_by(student_id = 6).first()
        db.session.delete(stud)
        db.session.commit()
        app.run(debug=True)
