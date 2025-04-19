from flask import (Blueprint,
                   render_template,
                   request, jsonify, session,
                   )
from models import Posts, Applications, db

applicant_bp = Blueprint('hire_applicant', __name__)

@applicant_bp.route('/home_applicant', methods= ['GET', 'POST'])
def home():
    offers = Posts.query.all()
    return render_template('aspirant/home.html', offers = offers)

@applicant_bp.route('/accept_offer', methods = ['POST'])
def accept_offer():
    rq = request.get_json()
    offer_id = rq.get('id_offer')

    apply = Applications(
        user_id = session.get('user_id'),
        post_id = offer_id ,
        created_at = db.func.now(),
        status = 'pending'
    )

    db.session.add(apply)
    db.session.commit()

    return jsonify({"message": "Solicitud recibida"}), 200