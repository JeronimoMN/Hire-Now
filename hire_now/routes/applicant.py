from flask import (Blueprint,
                   render_template,
                   request,
                   )
from models import Posts

applicant_bp = Blueprint('hire_applicant', __name__)

@applicant_bp.route('/home_applicant', methods= ['GET', 'POST'])
def home():
    offers = Posts.query.all()
    return render_template('home.html', offers = offers)