from flask import (Blueprint,
                   request,
                   render_template,
                   url_for,
                   session,
                   redirect)

hire_now_bp = Blueprint('hire', __name__)

@hire_now_bp.route('/home')
def redirect_home():
    role = session.get('role')
    if role == 1:
        return redirect(url_for('hire_applicant.home'))
    elif role == 2:
        return redirect(url_for('company_hire.home'))

