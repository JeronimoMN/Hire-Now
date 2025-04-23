from flask import Flask, session
from flask_mail import Mail
from config import Config
from users.routes import users_bp
from hire_now.routes.base import hire_now_bp
from hire_now.routes.company import company_bp
from hire_now.routes.applicant import applicant_bp
from models import db
from extensions import mail
import os

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(users_bp)
    app.register_blueprint(hire_now_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(applicant_bp)


    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = os.getenv('DEL_EMAIL')
    app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    mail.init_app(app)


    #Database
    db.init_app(app)


    if __name__ == '__main__':
        app.run(debug=True)

    return app