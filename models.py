from codecs import replace_errors

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    #Applicant and Company
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(64))

#Instancias
role1 = Role(name="Aspirant", description="Applicant user role")
role2 = Role(name="Company", description="Company user role")

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __init__(self, name, last_name, password, email, role):
        self.name = name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.role = role

    def __repr__(self):
        return f'<User {self.id} - {self.name} - {self.email} - {self.role}>'

    @staticmethod
    def get_by_email(email):
        return Users.query.filter_by(email = email).first()

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skills = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, db.ForeignKey('cities.id'), nullable=False)

class Cities(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
